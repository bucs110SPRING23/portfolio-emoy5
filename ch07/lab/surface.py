from rectangle.py import rectangle
class Surface:
    def __init__(self, filename, x, y, h, w):
        self.rect = rectangle.Rectangle()
        self.image = str(filename)
        self.rect.x = x
        self.rect.y = y
        self.rect.height = h
        self.rect.width = w
    
    def getRect(self):
        return self.rect



