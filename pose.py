from PIL import Image
import random

library = __import__('library')


class Pose:
    def __init__(self, name, sanskrit, cat1, cat2, library):
        self._name = name
        self._sanskrit = sanskrit
        self._cat1 = cat1
        self._cat2 = cat2
        self.visited = 0
        self._desc = None
        #self._image = Image.open(f"images/{name}.png")
        if cat2 not in library._poses[cat1]:
            library._poses[cat1][cat2] = []
        library._poses[cat1][cat2].append(self)
    
    def __repr__(self):
        return self._name


class Sequence:
    def __init__(self, pose1, cat1, lib):
        self._order = [pose1]
        start_cat = cat1
        self._next_cat1 = None
        pose = pose1
        #populate list if starting in a standing pose
        if start_cat == 'standing':
            self._next_cat1 = 'arm & leg' #random.choice['standing', 'prone', 'sitting']
            for i in range(0, 4): 
                pose = lib.standing_get_next(pose, i)
                self._order.append(pose)

        #populate list if starting in an arm & leg pose
        if start_cat == 'arm & leg':
            next_cat1 = 'standing' #random.choice['standing', 'prone', 'sitting']
            self._next_cat1 = next_cat1
            for i in range(0, 4): 
                pose = lib.arm_leg_get_next(pose, i, next_cat1)
                self._order.append(pose)

    #assign hold lenghts to each pose in the sequence
    def assign_hold(self, length, pace):
        #each sequence is 3 min long
        if length % 3 == 0 and pace == 'slow':
            h1 = random.randint(15, 36)
            h2 = random.randint(h1, 72)
            h3 = random.randint(h2, 108)
            h4 = random.randint(h3, 144)
            return [h1, h2 - h1, h3 - h2, h4 - h3, 180 - h4]

        #each sequence is 4 min long
        if length % 4 == 0 and pace == 'slow':
            h1 = random.randint(20, 48)
            h2 = random.randint(h1, 96)
            h3 = random.randint(h2, 144)
            h4 = random.randint(h3, 192)
            return [h1, h2 - h1, h3 - h2, h4 - h3, 240 - h4]

        #each sequence is 5 min long
        if length % 5 == 0 and pace == 'slow':
            h1 = random.randint(20, 60)
            h2 = random.randint(h1, 120)
            h3 = random.randint(h2, 180)
            h4 = random.randint(h3, 240)
            return [h1, h2 - h1, h3 - h2, h4 - h3, 240 - h4]
        
        #each sequence is 1 min long
        if pace == 'fast':
            h1 = random.randint(5, 12)
            h2 = random.randint(h1, 24)
            h3 = random.randint(h2, 36)
            h4 = random.randint(h3, 48)
            return [h1, h2 - h1, h3 - h2, h4 - h3, 60 - h4]
        


class Library:
    def __init__(self, cat1, cat2, cat3, cat4, cat5):
        self._poses = {
            cat1: {},
            cat2: {},
            cat3: {},
            cat4: {},
            cat5: {}
        }
        
    #figure out which pose will be next in the standing sequence
    def standing_get_next(self, pose, i):
        if  i == 0 or i == 1 or i == 2:
            while True:
                next_cat2 = random.choice(list(self._poses['standing']))
                next_pose = random.choice(list(self._poses['standing'][next_cat2]))
                if next_pose != pose:
                    return next_pose
        if i == 3: 
            while True:
                next_pose = random.choice(list(self._poses['standing']['forward bend']))
                if next_pose != pose:
                    return next_pose

    #figure out which pose will be next in the arm & leg sequence
    def arm_leg_get_next(self, pose, i, next_cat1):
        if  i == 0 or i == 1 or i == 2:            
            while True:
                next_cat2 = random.choice(list(self._poses['arm & leg']))
                next_pose = random.choice(list(self._poses['arm & leg'][next_cat2]))
                if next_pose != pose:
                    return next_pose
        
        if i == 3 and next_cat1 == 'prone': 
            while True:
                next_pose = random.choice(list(self._poses['arm & leg']['forward bend']))
                if next_pose != pose:
                    return next_pose
        
        if i == 3 and next_cat1 == 'sitting': 
           while True:
                next_pose = random.choice(list(self._poses['arm & leg']['neutral']))
                if next_pose != pose:
                    return next_pose

        if i == 3 and next_cat1 == 'standing': 
            while True:
                next_pose = random.choice(list(self._poses['arm & leg']['forward bend']))
                if next_pose != pose:
                    return next_pose

    def get_start(self, next_cat1):
        next_cat2 = random.choice(list(self._poses['arm & leg']))
        return random.choice(list(self._poses['arm & leg']['neutral']))

    #build a list of sequences
    def _build_routine(self, start, length, pace):
        l = 0
        routine = []

        seq1 = Sequence(start, start._cat1, library.lib)
        routine.append(seq1)
        next_start = library.lib.get_start(seq1._next_cat1)
        next_seq = Sequence(next_start, seq1._next_cat1, library.lib)
        if length % 3 == 0 and pace == 'slow':
            l += 3
        if length % 4 == 0 and pace == 'slow':
            l += 4
        if length % 5 == 0 and pace == 'slow':
            l += 5
        if pace == 'fast':
            l += 1

        while l < length:
            routine.append(next_seq)
            next_start = library.lib.get_start(next_seq._next_cat1)
            next_seq = Sequence(next_start, next_seq._next_cat1, library.lib)
            if length % 3 == 0 and pace == 'slow':
                l += 3
            if length % 4 == 0 and pace == 'slow':
                l += 4
            if length % 5 == 0 and pace == 'slow':
                l += 5
            if pace == 'fast':
                l += 1
        return routine

    def _get_routine_timing(self, routine, length, pace):
        timing = []
        for i in range(0, len(routine)):
            timing.append((routine[i]).assign_hold(length, pace))
        return timing
