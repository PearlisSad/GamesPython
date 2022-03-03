try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from VectorClass.vectorClass import Vector

CANVAS_DIMS = (800, 500)

IMG = simplegui.load_image(
    'http://www.cs.rhul.ac.uk/courses/CS1830/sprites/coach_wheel-512.png')
IMG_CENTRE = (256, 256)
IMG_DIMS = (512, 512)

space_timer = 0


class Wheel:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)

    def draw(self, canvas):
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, self.pos.get_p(),
                          (self.radius*2, self.radius*2))

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.95)
        if self.on_ground():
            self.vel.y = 0
            self.pos.y = CANVAS_DIMS[1] - self.radius
        elif self.on_top():
            self.vel.y = 0
            self.pos.y = self.radius
        else:
            self.vel.y += 0.5

    def on_ground(self):
        return self.pos.y >= CANVAS_DIMS[1] - self.radius
    def on_top(self):
        return self.pos.y <= self.radius

class Keyboard:
    def __init__(self):
        self.space = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['space']:
            self.space = False


class Platform:
    def __init__(self, orientation, dimentions):
        self.orientation = orientation
        self.dimentions = dimentions
        self.x = CANVAS_DIMS[0]


    def draw(self, canvas):
        if self.orientation == "vertical":
            canvas.draw_line((self.x, self.dimentions[0]), (self.x, self.dimentions[1]), 10, 'Red')
        elif self.orientation == "horizontal":
            canvas.draw_line((self.x, self.dimentions[0]), (self.x + self.dimentions[2], self.dimentions[0]), 10, 'Red')
        self.x -= 3

    def update(self):
        return None

