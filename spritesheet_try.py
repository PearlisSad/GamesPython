try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from VectorClass.vectorClass import Vector
from ball import Keyboard

CANVAS_DIMS = (800, 600)
SHEET_IMG = "D:\GamesPython\Spritesheet.jpg"

SHEET_WIDTH = 564
SHEET_HEIGHT = 240

SHEET_COLUMNS = 5
SHEET_ROWS = 2

space_timer = 0


class Spritesheet:
    def __init__(self,
                 img, pos,
                 width, height,
                 columns, rows,
                 radius=10):
        self.img = simplegui.load_image(img)

        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)

        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows

        self.frame_width = width / columns
        self.frame_height = height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]

    def draw(self, canvas):
        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)
        dest_centre = (CANVAS_DIMS[1]/3, CANVAS_DIMS[1] - self.radius)
        dest_size = (100, 100)

        canvas.draw_image(
            self.img,
            source_centre, source_size,
            dest_centre, dest_size)

    def frame_update(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

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


class Clock:
    def __init__(self):
        self.frame_duration = None
        self.time = 0

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        self.frame_duration = frame_duration
        return self.time % self.frame_duration == 0


class Interaction:
    def __init__(self, sheet, keyboard):
        self.sheet = sheet
        self.keyboard = keyboard

    def inter_update(self):
        if self.keyboard.space and sheet.on_ground():
            self.sheet.vel.y = -10
            global space_timer
            space_timer = 0
        if self.keyboard.space:
            space_timer += 5
            print(space_timer)
            if space_timer > 10:
                self.sheet.vel.y -= 5
                space_timer = 0


kbd = Keyboard()
clock = Clock()
sheet = Spritesheet(
    SHEET_IMG,
    Vector(CANVAS_DIMS[1] / 2.7, CANVAS_DIMS[0]),
    SHEET_WIDTH, SHEET_HEIGHT,
    SHEET_COLUMNS, SHEET_ROWS,
    40)
interaction = Interaction(sheet, kbd)


def draw(canvas):
    interaction.inter_update()
    sheet.update()
    sheet.on_ground()
    sheet.draw(canvas)
    clock.tick()
    if clock.transition(4):
        sheet.frame_update()


frame = simplegui.create_frame('Interaction', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('Aqua')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)

frame.start()
