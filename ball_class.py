try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vectorClass import Vector

CANVAS_DIMS = (500, 500)

IMG = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/coach_wheel-512.png')
IMG_CENTRE = (256, 256)
IMG_DIMS = (512, 512)

space_timer = 0

# Global variables
img_dest_dim = (28,28)
img_pos = [CANVAS_DIMS[0]/2, 2*CANVAS_DIMS[1]/3.]
#img_rot = 0


class Wheel:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.colour = 'White'
        self.img_rot = 0
        #self.step = 0

    def draw(self, canvas):
        pos1 = self.pos.copy()
        pos2 = self.pos.copy()
        pos1.x += CANVAS_DIMS[0]
        pos2.x -= CANVAS_DIMS[0]

        #global img_rot
        #self.img_rot += self.step
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, self.pos.get_p(), (self.radius*2,self.radius*2), self.img_rot)
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, pos1.get_p(), (self.radius*2,self.radius*2), self.img_rot)
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, pos2.get_p(), (self.radius*2,self.radius*2), self.img_rot)

    def update(self):
        if self.pos.x >= CANVAS_DIMS[0] + self.radius:
            self.pos.x -= CANVAS_DIMS[0]
        elif self.pos.x <= -self.radius:
            self.pos.x += CANVAS_DIMS[0]
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        if self.on_ground():
            self.vel.y = 0
            self.pos.y = CANVAS_DIMS[1]-self.radius
        else:
            self.vel.y += 1.5

    def on_ground(self):
        return self.pos.y >= CANVAS_DIMS[1]-self.radius



class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.space = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        elif key == simplegui.KEY_MAP['left']:
            self.left = True
        elif key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        elif key == simplegui.KEY_MAP['left']:
            self.left = False
        elif key == simplegui.KEY_MAP['space']:
            self.space = False


class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
            self.wheel.img_rot += 0.1
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
            self.wheel.img_rot -= 0.1
        if self.keyboard.space and wheel.on_ground():
            self.wheel.vel.y = -30
            global space_timer
            space_timer = 0
        if self.keyboard.space:
            space_timer+=1
            print(space_timer)
            if space_timer >7:
                self.wheel.vel.y -= 10
                self.keyboard.space = False
                space_timer = 0



kbd = Keyboard()
wheel = Wheel(Vector(CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] - 40), 40)
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
