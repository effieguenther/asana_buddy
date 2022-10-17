from PIL import Image

class Pose:
    def __init__(self, name, sanskrit, cat1, cat2):
        self._name = name
        self._sanskrit = sanskrit
        self._cat1 = cat1
        self._cat2 = cat2
        self._image = Image.open(f"images/{name}.png")

class Library:
    def __init__(self, name):
        self._name = name
        self._poses = []