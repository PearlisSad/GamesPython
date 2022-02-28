try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from VectorClass.vectorClass import Vector

CANVAS_DIMS = (800, 600)

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
        else:
            self.vel.y += 0.5

    def on_ground(self):
        return self.pos.y >= CANVAS_DIMS[1] - self.radius


class Keyboard:
    def __init__(self):
        self.space = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['space']:
            self.space = False


class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.space and wheel.on_ground():
            self.wheel.vel.y = -10
            global space_timer
            space_timer = 0
        if self.keyboard.space:
            space_timer += 5
            print(space_timer)
            if space_timer > 10:
                self.wheel.vel.y -= 5
                space_timer = 0


kbd = Keyboard()
wheel = Wheel(Vector(CANVAS_DIMS[1] / 2.7, CANVAS_DIMS[0]), 40)
inter = Interaction(wheel, kbd)


def draw(canvas):
    inter.update()
    wheel.update()
    wheel.on_ground()
    wheel.draw(canvas)


frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('#2C6A6A')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
