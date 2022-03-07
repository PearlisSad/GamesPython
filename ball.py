try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from VectorClass.vectorClass import Vector

CANVAS_DIMS = (800, 500)

SHEET_IMG = "D:\GamesPython\Spritesheet.jpg"

SHEET_WIDTH = 564
SHEET_HEIGHT = 240

SHEET_COLUMNS = 5
SHEET_ROWS = 2

space_timer = 0


class Wheel:
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
<<<<<<< HEAD
<<<<<<< HEAD
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, self.pos.get_p(),
                          (self.radius*2, self.radius*2))
=======
=======
>>>>>>> parent of ed2d146 (Revert "Merge remote-tracking branch 'origin/main'")
        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)

        canvas.draw_image(
            self.img,
            source_centre, source_size, self.pos.get_p(),
            (self.radius*2, self.radius*2))

    def frame_update(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows
<<<<<<< HEAD
>>>>>>> parent of ed2d146 (Revert "Merge remote-tracking branch 'origin/main'")
=======
>>>>>>> parent of ed2d146 (Revert "Merge remote-tracking branch 'origin/main'")

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.9)
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


class Clock:
    def __init__(self):
        self.frame_duration = None
        self.time = 0

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        self.frame_duration = frame_duration
        return self.time % self.frame_duration == 0


class Platform:
    def __init__(self, orientation, dimentions):
        self.orientation = orientation
        self.dimentions = dimentions
        self.x = CANVAS_DIMS[0]

    def draw(self, canvas):
        if self.orientation == "vertical":
            canvas.draw_line(
                (self.x, self.dimentions[0]), (self.x, self.dimentions[1]), 10, 'Red')
        elif self.orientation == "horizontal":
            canvas.draw_line(
                (self.x, self.dimentions[0]), (self.x + self.dimentions[2], self.dimentions[0]), 10, 'Red')
        self.x -= 3

    def update(self):
        return None
