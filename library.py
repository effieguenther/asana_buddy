import random
from pose import Sequence

#the library class is a nested dictionary
#the outer key is the main category (seated, standing, etc...)
#the inner key is the sub category (neutral, balancing, etc...)
#each inner key stores a list of poses that fit each main + sub category
#upon innit, each pose instance will append itself to a library

class Library:
    def __init__(self, cat1, cat2, cat3, cat4, cat5):
        self._poses = {
            cat1: {},
            cat2: {},
            cat3: {},
            cat4: {},
            cat5: {}
        }
        
    #decide which pose will be next in the standing sequence
    
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


    #decide which pose will be next in the arm & leg sequence
   
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


    #decide which pose will be next in the seated sequence
    
    def seated_get_next(self, pose, i, next_cat1):
        if  i == 0 or i == 1 or i == 2:            
            while True:
                next_cat2 = random.choice(list(self._poses['seated']))
                next_pose = random.choice(list(self._poses['seated'][next_cat2]))
                if next_pose != pose:
                    return next_pose
        
        if i == 3 and next_cat1 == 'prone': 
            while True:
                next_pose = random.choice(list(self._poses['seated']['neutral']))
                if next_pose != pose:
                    return next_pose
        
        if i == 3 and next_cat1 == 'arm & leg': 
           while True:
                next_pose = random.choice(list(self._poses['seated']['forward bend']))
                if next_pose != pose:
                    return next_pose

        if i == 3 and next_cat1 == 'supine': 
            while True:
                next_pose = random.choice(list(self._poses['seated']['balancing']))
                if next_pose != pose:
                    return next_pose 


    #decide which pose will be next in the prone sequence

    def prone_get_next(self, pose, i, next_cat1):
        if  i == 0 or i == 1 or i == 2:            
            while True:
                next_cat2 = random.choice(list(self._poses['prone']))
                next_pose = random.choice(list(self._poses['prone'][next_cat2]))
                if next_pose != pose:
                    return next_pose
        
        if i == 3 and next_cat1 == 'seated': 
            while True:
                next_pose = random.choice(list(self._poses['prone']['backbend']))
                if next_pose != pose:
                    return next_pose
        
        if i == 3 and next_cat1 == 'arm & leg': 
           while True:
                next_pose = random.choice(list(self._poses['seated']['forward bend']))
                if next_pose != pose:
                    return next_pose

        if i == 3 and next_cat1 == 'supine': 
            while True:
                next_pose = random.choice(list(self._poses['seated']['neutral']))
                if next_pose != pose:
                    return next_pose

    #decide which pose will be next in the supine sequence

    def supine_get_next(self, pose, i, next_cat1):
        if  i == 0 or i == 1 or i == 2:            
            while True:
                next_cat2 = random.choice(list(self._poses['supine']))
                next_pose = random.choice(list(self._poses['supine'][next_cat2]))
                if next_pose != pose:
                    return next_pose
        
        if i == 3 and next_cat1 == 'seated': 
            while True:
                next_pose = random.choice(list(self._poses['supine']['balancing']))
                if next_pose != pose:
                    return next_pose

        if i == 3 and next_cat1 == 'prone': 
            while True:
                next_pose = random.choice(list(self._poses['supine']['neutral']))
                if next_pose != pose:
                    return next_pose
   
   #get the starting pose for the next sequence

    def get_start(self, next_cat1):
        next_cat2 = random.choice(list(self._poses[next_cat1]))
        return random.choice(list(self._poses[next_cat1]['neutral']))

   
    #build a list of sequences as the main routine
    
    def _build_routine(self, start, length):
        l = 0
        routine = []
        asanas = __import__('asanas')

        seq1 = Sequence(start, start._cat1, asanas.lib)
        routine.append(seq1)
        next_start = asanas.lib.get_start(seq1._next_cat1)
        next_seq = Sequence(next_start, seq1._next_cat1, asanas.lib)
        l += 1

        while l < length:
            routine.append(next_seq)
            next_start = asanas.lib.get_start(next_seq._next_cat1)
            next_seq = Sequence(next_start, next_seq._next_cat1, asanas.lib)
            l += 1
        return routine

    def _get_routine_timing(self, routine, length):
        timing = []
        for i in range(0, len(routine)):
            timing.append(routine[i].assign_hold(length))
        return timing
