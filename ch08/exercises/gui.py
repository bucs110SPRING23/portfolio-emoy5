import random
class MysteryBlock:
  def __init__(self):
    """
    Initialize the mystery block object
    args: 
    """
    self.not_hit = True
    powerups = ["mushroom", "coin", "life"]
    self.has_power_up = random.randint(len(powerups))
    self.height = 15

class Enemy:
  def __init__(self):
    """
    Initialize the Goomba enemy object
    args: 
    """
    self.is_alive = True
    self.speed = 3
    self.height = 13 

class Pipe:
  def __init__(self):
    """
    Initialize the pipe object
    args: 
    """
    self.is_on_top = False
    self.height = 10
    self.color = "green"

#Other possible classes
class Text:
    def __init__(self, msg):
        self.font
        self.size
        self.color
        self.msg

class Block:
    def __init__(self):
        #blocks in general
        self.x
        self.y
    
    
class PowerUp(Block):
    def __init__(self):
       #using the created class, a more specific type of block
       self.power