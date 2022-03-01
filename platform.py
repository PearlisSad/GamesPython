try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
from VectorClass.vectorClass import Vector

CANVAS_DIMS = (800, 600)

class Platform:
    def __init__(self, platform):
        self.platform = platform
        self.velocity = Vector(1,0)

    def draw(self, canvas):
        #canvas.draw_line(platform)

def randomVerticalPlatform():
    lenght = random.randint(15,25)
    y1 = random.randint(5, CANVAS_DIMS[1]-30)
    y2 = y1 + lenght
    return(Vector((CANVAS_DIMS[0]+10,y1),(CANVAS_DIMS[0]+10,y2)))




