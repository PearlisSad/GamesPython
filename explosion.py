try:
    import simplegui

except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

EXPLOSION_SHEET_URL = r"https://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png"

EXPLOSION_SHEET_WIDTH = 900
EXPLOSION_SHEET_HEIGHT = 900

EXPLOSION_SHEET_COLUMNS = 9
EXPLOSION_SHEET_ROWS = 9

CANVAS_DIMS = (800, 400)



class Explosion_spritesheet:
    def __init__(self, pos):
        self.width = EXPLOSION_SHEET_WIDTH
        self.height = EXPLOSION_SHEET_HEIGHT

        self.clock = Clock_laser()
        self.frame_duration = 0.5
        self.num_frames = 0

        self.dest_size = (100,100)
        self.img = simplegui.load_image(EXPLOSION_SHEET_URL)
        self.columns = EXPLOSION_SHEET_COLUMNS
        self.rows = EXPLOSION_SHEET_ROWS

        self.frame_width = self.width / self.columns
        self.frame_height = self.height / self.rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.dest_centre = pos

    def update_index(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0 and not self.done():
            self.frame_index[1] = (self.frame_index[1] + 1)

    def draw(self, canvas):
        self.clock.tick()
        if self.clock.transition(self.frame_duration):
            self.update_index()
            self.num_frames = (self.num_frames + 1)

        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)
        # doesn't have to be same aspect ratio as frame!

        canvas.draw_image(self.img,
                            source_centre,
                            source_size,
                            self.dest_centre,
                            self.dest_size)

    def done(self):
        return self.num_frames > 81


class Clock_laser:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        return self.time % frame_duration == 0