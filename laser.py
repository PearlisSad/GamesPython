try:
    import simplegui

except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
from VectorClass.vectorClass import Vector

VERICAL_LASER_SHEET_URL = r"https://raw.githubusercontent.com/PearlisSad/GamesPython/2e8519b36333ed145682b317282ab35c97ef7219/texture_laser.png"
HORIZONTAL_LASER_SHEET_URL = r"https://raw.githubusercontent.com/PearlisSad/GamesPython/b03bf9ecfddb01277edbbcd5263115c70a9ef02c/texture_laser_horizontal.png"
LASER_SHEET_WIDTH = 2048
LASER_SHEET_HEIGHT = 2048
VERTICAL_LASER_SHEET_COLUMNS = 4
VERTICAL_LASER_SHEET_ROWS = 3
HORIZONTAL_LASER_SHEET_COLUMNS = 3
HORIZONTAL_LASER_SHEET_ROWS = 4

CANVAS_DIMS = (800, 400)


class Laser_spritesheet:
    def __init__(self):
        self.width = LASER_SHEET_WIDTH
        self.height = LASER_SHEET_HEIGHT

        self.clock = Clock_laser()
        self.frame_duration = 0.5
        self.dims = randomLaser()
        self.dest_size = self.dims[1]
        if self.dims[2] == "vertical":
            self.img = simplegui.load_image(VERICAL_LASER_SHEET_URL)
            self.columns = VERTICAL_LASER_SHEET_COLUMNS
            self.rows = VERTICAL_LASER_SHEET_ROWS
        else:
            self.img = simplegui.load_image(HORIZONTAL_LASER_SHEET_URL)
            self.columns = HORIZONTAL_LASER_SHEET_COLUMNS
            self.rows = HORIZONTAL_LASER_SHEET_ROWS

        self.frame_width = self.width / self.columns
        self.frame_height = self.height / self.rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.dest_centre = (CANVAS_DIMS[0] + 5, self.dims[0])

    def update_index(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

    def draw(self, canvas):
        self.clock.tick()
        if self.clock.transition(self.frame_duration):
            self.update_index()

        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)
        pos_list = list(self.dest_centre)
        pos_list[0] -= 4
        self.dest_centre = tuple(pos_list)
        # doesn't have to be same aspect ratio as frame!

        canvas.draw_image(self.img,
                          source_centre,
                          source_size,
                          self.dest_centre,
                          self.dest_size)

    def done(self):
        return self.num_frames > 12

    def hit_vertical(self, player):
        player_pos = player.pos
        return player_pos.x > self.dest_centre[0] and player_pos.y > self.dims[3] and player_pos.y < self.dims[4]

    def hit_horizontal(self, player):
        player_pos = player.pos
        return player_pos.y < self.dims[0] + 3 and player_pos.y > self.dims[0] - 3 and player_pos.x > self.dest_centre[0] - self.dims[1][1]


def randomLaser():
    size = random.randint(150, 210)
    size_touple = (size, size)
    centre = random.randint(5, CANVAS_DIMS[1] - int((size/2)))
    start_point = centre - size/2
    end_point = centre + size/2
    orientation = "vertical"
    if size > 200:
        orientation = "horizontal"
    return (centre, size_touple, orientation, start_point, end_point)

#


class Clock_laser:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        return self.time % frame_duration == 0
