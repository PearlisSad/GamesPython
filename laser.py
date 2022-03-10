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
        dest_size = self.dims[1]

        canvas.draw_image(self.img,
                            source_centre,
                            source_size,
                            self.dest_centre,
                            dest_size)


    def done(self):
        return self.num_frames > 12

def randomLaser():
    size = random.randint(150, 210)
    size_touple = (size, size)
    y1 = random.randint(5, CANVAS_DIMS[1] - int((size/2)))
    orientation = "vertical"
    if size > 200:
        orientation = "horizontal"
    return (y1, size_touple, orientation)

# class Platform:
#     def __init__(self, orientation, dimentions):
#         self.orientation = orientation
#         self.dimentions = dimentions
#         self.x = CANVAS_DIMS[0]
#
#
#     def draw(self, canvas):
#         if self.orientation == "vertical":
#             canvas.draw_line((self.x, self.dimentions[0]), (self.x, self.dimentions[1]), 10, 'Red')
#         elif self.orientation == "horizontal":
#             canvas.draw_line((self.x, self.dimentions[0]), (self.x + self.dimentions[2], self.dimentions[0]), 10, 'Red')
#         self.x -= 3
#
#     def update(self):
#         return None
#
class Clock_laser:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        return self.time % frame_duration == 0
#
# class Interaction:
#
#     def __init__(self, laser):#explosion_list):
#         #self.explosion_list = explosion_list
#         #self.to_delete = []
#         #self.score = 10
#         self.laser = laser
#
#     def draw(self, canvas):
#         #self.delete()
#         #self.update()
#         #self.score_update(canvas)
#         # if self.score > 0:
#         #     self.add_explosion()
#         # else:
#         #     self.score = 0
#         # for explosion in self.explosion_list:
#         self.laser.draw(canvas)
#             # if explosion.done() and explosion not in self.to_delete:
#             #     self.to_delete.append(explosion)
#             #     self.score -= 1
#
#     # def score_update(self, canvas):
#     #     if self.score > 0:
#     #         canvas.draw_text(str(self.score), (CANVAS_WIDTH / 2, 50), 33, 'Red', 'serif')
#     #     else:
#     #         canvas.draw_text("Game over", (CANVAS_WIDTH / 2, 50), 33, 'Red', 'serif')
#     # def update(self):
#     #     last_click = self.mouse.click_pos()
#     #     if last_click is not None:
#     #         for explosion in self.explosion_list:
#     #             if last_click.copy().subtract(Vector(explosion.dest_centre[0],explosion.dest_centre[1])).length() <= explosion.dest_size[0]:
#     #                 self.to_delete.append(explosion)
#     #
#     #
#     # def delete(self):
#     #     for explosion in self.to_delete:
#     #         self.explosion_list.remove(explosion)
#     #         self.to_delete.remove(exploion)
#
#     # def add_explosion(self):
#     #     if 1 == random.randrange(1, 80):
#     #         self.explosion_list.append(Spritesheet(SHEET_URL, SHEET_WIDTH, SHEET_HEIGHT,
#     #                                           SHEET_COLUMNS, SHEET_ROWS, Clock(), rand_pos(), rand_frame_duration(),
#     #                                           rand_scale()))
#
# laser = Laser_spritesheet(SHEET_URL,SHEET_WIDTH, SHEET_HEIGHT,
#                                 SHEET_COLUMNS, SHEET_ROWS,Clock())
# interaction = Interaction(laser)#explosion_list)
#
# frame = simplegui.create_frame("Sprite", CANVAS_DIMS[0], CANVAS_DIMS[1])
# frame.set_draw_handler(interaction.draw)
# #frame.set_mouseclick_handler(mouse.click_handler)
# frame.start()
# #Spritesheet(SHEET_URL,SHEET_WIDTH, SHEET_HEIGHT,
#                                 #SHEET_COLUMNS, SHEET_ROWS,Clock(), rand_pos(),rand_frame_duration(),rand_scale()),