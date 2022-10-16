from PIL import Image

class Pose:
    def __init__(self, name, sanskrit):
        self._name = name
        self._sanskrit = sanskrit
        self._image = Image.open(f"/images/{name}.png")