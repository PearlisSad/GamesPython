#try:
    #import simplegui
#except ImportError:
    #import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
#import random
from VectorClass.vectorClass import Vector

#CANVAS_DIMS = (800, 600)

class Platform:
    def __init__(self, platform):
        self.platform = platform
        self.velocity = Vector(1,0)

    def draw(self, canvas):
        canvas.draw_line(self.platform.x, self.platform.y, 10, 'Red')

    def update(self):
        self.platform.x[0] -= 1
        self.platform.y[0] -= 1

#



