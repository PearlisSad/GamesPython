try:
    import simplegui

except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
from VectorClass.vectorClass import Vector

SHEET_URL = r"C:\Users\ngano\PycharmProjects\pythonProject\game\texture_laser.png"
SHEET_WIDTH = 2048
SHEET_HEIGHT = 2048
SHEET_COLUMNS = 4
SHEET_ROWS = 3

CANVAS_DIMS = (800, 400)



class Laser_spritesheet:
    def __init__(self, imgurl, width, height, columns, rows, clock):
        self.img = simplegui.load_image(imgurl)
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.clock = clock
        self.frame_duration = 0.5

        self.frame_width = width / columns
        self.frame_height = height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]

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
        dest_centre = (300, 150)
        # doesn't have to be same aspect ratio as frame!
        dest_size = (100, 100)

        canvas.draw_image(self.img,
                            source_centre,
                            source_size,
                            dest_centre,
                            dest_size)


    def done(self):
        return self.num_frames > 12
       # return (self.frame_index[0] == 8 and self.frame_index[1] == 8)

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

class Clock:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        return self.time % frame_duration == 0

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
            # if explosion.done() and explosion not in self.to_delete:
            #     self.to_delete.append(explosion)
            #     self.score -= 1

    # def score_update(self, canvas):
    #     if self.score > 0:
    #         canvas.draw_text(str(self.score), (CANVAS_WIDTH / 2, 50), 33, 'Red', 'serif')
    #     else:
    #         canvas.draw_text("Game over", (CANVAS_WIDTH / 2, 50), 33, 'Red', 'serif')
    # def update(self):
    #     last_click = self.mouse.click_pos()
    #     if last_click is not None:
    #         for explosion in self.explosion_list:
    #             if last_click.copy().subtract(Vector(explosion.dest_centre[0],explosion.dest_centre[1])).length() <= explosion.dest_size[0]:
    #                 self.to_delete.append(explosion)
    #
    #
    # def delete(self):
    #     for explosion in self.to_delete:
    #         self.explosion_list.remove(explosion)
    #         self.to_delete.remove(exploion)

    # def add_explosion(self):
    #     if 1 == random.randrange(1, 80):
    #         self.explosion_list.append(Spritesheet(SHEET_URL, SHEET_WIDTH, SHEET_HEIGHT,
    #                                           SHEET_COLUMNS, SHEET_ROWS, Clock(), rand_pos(), rand_frame_duration(),
    #                                           rand_scale()))

laser = Laser_spritesheet(SHEET_URL,SHEET_WIDTH, SHEET_HEIGHT,
                                SHEET_COLUMNS, SHEET_ROWS,Clock())
# interaction = Interaction(laser)#explosion_list)
#
# frame = simplegui.create_frame("Sprite", CANVAS_DIMS[0], CANVAS_DIMS[1])
# frame.set_draw_handler(interaction.draw)
# #frame.set_mouseclick_handler(mouse.click_handler)
# frame.start()
#Spritesheet(SHEET_URL,SHEET_WIDTH, SHEET_HEIGHT,
                                #SHEET_COLUMNS, SHEET_ROWS,Clock(), rand_pos(),rand_frame_duration(),rand_scale()),
