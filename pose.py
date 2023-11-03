import random
# from PIL import Image

#pose class stores all the information about each pose
#and appends itself to a library

class Pose:
    def __init__(self, name, sanskrit, cat1, cat2, library):
        self._name = name
        self._sanskrit = sanskrit
        self._cat1 = cat1
        self._cat2 = cat2
        self.visited = 0
        self._desc = None
        # self._image = Image.open(f"images/{name}.png")
        if cat2 not in library._poses[cat1]:
            library._poses[cat1][cat2] = []
        library._poses[cat1][cat2].append(self)
    
    def __repr__(self):
        return self._name


#upon innit sequence class creates a randomized sequence of 5 poses
#it is passed the first pose, and assigns the next 4
#the category of the next sequence randomly chosen and passed into the get_next function
#to ensure each sequence flows into the next

class Sequence:
    def __init__(self, pose1, cat1, lib):
        self._order = [pose1]
        start_cat = cat1
        pose = pose1
        #populate list if starting in a standing pose
        if start_cat == 'standing':
            self._next_cat1 = random.choice(['standing', 'prone', 'seated'])
            for i in range(0, 4): 
                pose = lib.standing_get_next(pose, i)
                self._order.append(pose)

        #populate list if starting in an arm & leg pose
        if start_cat == 'arm & leg':
            next_cat1 = random.choice(['standing', 'prone', 'seated'])
            self._next_cat1 = next_cat1
            for i in range(0, 4): 
                pose = lib.arm_leg_get_next(pose, i, next_cat1)
                self._order.append(pose)

        #populate list if starting in a seated pose
        if start_cat == 'seated':
            next_cat1 = random.choice(['arm & leg', 'prone', 'supine'])
            self._next_cat1 = next_cat1
            for i in range(0, 4): 
                pose = lib.seated_get_next(pose, i, next_cat1)
                self._order.append(pose)

        #populate list if starting in a prone pose
        if start_cat == 'prone':
            next_cat1 = random.choice(['seated', 'supine', 'arm & leg'])
            self._next_cat1 = next_cat1
            for i in range(0, 4): 
                pose = lib.prone_get_next(pose, i, next_cat1)
                self._order.append(pose)
        
        #populate list if starting in a supine pose
        if start_cat == 'supine':
            next_cat1 = random.choice(['seated', 'prone'])
            self._next_cat1 = next_cat1
            for i in range(0, 4): 
                pose = lib.supine_get_next(pose, i, next_cat1)
                self._order.append(pose)    
    
    #create a sister list of hold lengths for each sequence

    def assign_hold(self, length):
            h1 = random.randint(8, 15)
            h2 = random.randint(8, 15)
            h3 = random.randint(8, 15)
            h4 = random.randint(8, 15)
            return [h1, h2, h3, h4, 60 - (h1+h2+h3+h4)]
 