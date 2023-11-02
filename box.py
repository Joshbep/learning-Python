class Box:
    """This class creates a box with length, width and height"""
    def __init__(self, _length, _width, _height):
        self._length = _length
        self._width = _width
        self._height = _height
    def volume(self):
        return self._length * self._width * self._height
    def surface_area(self):
        l = self._length
        w = self._width
        h = self._height
        return (2 * ((l*w)+(l*h)+(w*h)))