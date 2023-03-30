class Rectangle:
    
    def __init__(self, x, y, h, w):
        """
        Contains the data to create a rectangle
        args: (int) x and y coordinates of the rectangle and its width and height
        return: (None) 
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

    def __str__(self):
        """
        Prints out the x and y coordinates of the rectangle and its width and height
        args: (rectangle obj) the rectangle object in the __init__ method
        return: (str) states the x,y coordinates + height and width of the rectangle created
        """
        return 'x: {self.x}, y: {self.y}, height: {self.height}, width: {self.width}'
