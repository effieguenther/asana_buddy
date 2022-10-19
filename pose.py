from PIL import Image
import random

class Pose:
    def __init__(self, name, sanskrit, cat1, cat2, library):
        self._name = name
        self._sanskrit = sanskrit
        self._cat1 = cat1
        self._cat2 = cat2
        self.visited = 0
        self.hold = 0
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