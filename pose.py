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
        self._image = Image.open(f"images/{name}.png")
        if library._poses[cat1][cat2] == None:
            library._poses[cat1][cat2] = []
        library._poses[cat1][cat2].append(self)


class Sequence:
    def __init__(self, pose1, lib):
        self._order = []
        pose = pose1
        start_cat = pose1._cat1
        if start_cat == 'standing':
            for i in range(0, 5): 
                self._order.append(pose)
                pose = lib.standing_get_next(pose, i)
        if start_cat == 'arm & leg':
            next_cat1 = random.choice('standing', 'prone', 'sitting')
            for i in range(0, 5): 
                self._order.append(pose)
                pose = lib.arm_leg_get_next(pose, i, next_cat1)

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
        if i == 1 or i ==2:
            while True:
                next_cat2 = random.choice(self._poses['standing'])
                next_pose_index = random.randrange(0, len(self._poses['standing'][next_cat2]))
                if self._poses['standing'][next_cat2][next_pose_index] != pose:
                    return self._poses['standing'][next_cat2][next_pose_index]
        if i == 3:
            next_pose_index = random.randrange(0, len(self._poses['standing']['forward fold']))
            if self._poses['standing'][next_cat2][next_pose_index] != pose:
                return self._poses['standing'][next_cat2][next_pose_index]   
        if i == 4: 
            next_pose_index = random.randrange(0, len(self._poses['arm & leg']['forward bend']))
            return self._poses['arm & leg']['forward bend'][next_pose_index]

    #figure out which pose will be next in the arm & leg sequence
    def arm_leg_get_next(self, pose, i, next_cat1):
        if i == 1 or i ==2:
            while True:
                next_cat2 = random.choice(self._poses['arm & leg'])
                next_pose_index = random.randrange(0, len(self._poses['arm & leg'][next_cat2]))
                if self._poses['arm & leg'][next_cat2][next_pose_index] != pose:
                    return self._poses['arm & leg'][next_cat2][next_pose_index]
        if i == 3 and next_cat1 == 'prone':
            next_pose_index = random.randrange(0, len(self._poses['arm & leg']['forward bend']))
            return self._poses['arm & leg']['forward bend'][next_pose_index]
        if i == 4 and next_cat1 == 'prone':
            next_pose_index = random.randrange(0, len(self._poses['prone']['forward bend']))
            return self._poses['prone']['forward bend'][next_pose_index]

    #build a list of sequences