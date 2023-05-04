from rectangle import Rectangle
class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Takes the rectangle and puts on the screen?
        args: (str) filename and (int) x, y, width, and height of rectangle
        return: None
        """
        self.rect = Rectangle(x, y, h, w)
        self.image = str(filename)
    
    def getRect(self):
        """
        Takes the rectangle and puts on the screen?
        args: None
        return: (Rectangle) a rectangle on a surface?
        """
        return self.rect



