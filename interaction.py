try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
#from user305_o32FtUyCKk_0 import Vector
from background import *  # Background, ClockBackground
from ball import *  # Keyboard, Wheel, Platform, Clock
from laser import Laser_spritesheet

CANVAS_DIMS = (800, 400)
SHEET_IMG = "https://github.com/PearlisSad/GamesPython/blob/main/Spritesheet.png?raw=true"  # "D:\GamesPython\Spritesheet.png"
# "https://github.com/PearlisSad/GamesPython/blob/main/Spritesheet_bird.jpg?raw=true"

SHEET_WIDTH = 564
SHEET_HEIGHT = 240

SHEET_COLUMNS = 5
SHEET_ROWS = 2

space_timer = 0
SHEET_URL = "https://raw.githubusercontent.com/PearlisSad/GamesPython/aeebe682ce8a4c45eb1e982eed622973b5e06cda/backgroundSprite.png"  # "https://cdn.discordapp.com/attachments/932691213721694358/950287598386036756/Untitled-5.png"
BACK_WIDTH = 11520  # 1440
BACK_HEIGHT = 5400  # 1480
BACK_COLUMNS = 6
BACK_ROWS = 5

frame_duration = 15  # frame duration = number of ticks the frame should show for
time = 0

counter = 0
pos = [700, 50]
size = 30
color = "red"


class Interaction:
    def __init__(self, wheel, keyboard, background, clock):
        self.wheel = wheel
        self.keyboard = keyboard
        self.platform_list = []
        self.to_delete = []
        self.platform_count = 0
        self.background = background
        self.clock = clock
        self.game_over = False
        self.score = 0

    def update(self):
        if self.keyboard.space and wheel.on_ground():
            self.wheel.vel.y = -10
            global space_timer
            space_timer = 0
        if self.keyboard.space:
            space_timer += 5
            if space_timer > 10:
                self.wheel.vel.y -= 5
                space_timer = 0
        if not self.keyboard.space and wheel.on_top():
            self.wheel.vel.y = 1

    def draw(self, canvas):
        self.background.draw(canvas)
        self.update()
        self.delete()
        self.wheel.update()

        time_score()
        if counter % 10 == 0:
            self.score += 1
        canvas.draw_text(str(self.score), pos, size, color)
        clock.tick()
        if clock.transition(4):
            wheel.frame_update()
        for platform in self.platform_list:
            platform.draw(canvas)
            # print(self.wheel.hit(platform))
            if platform.hit(self.wheel):
                self.game_over = True
            # print(self.wheel.hit(platform))
            # print(self.game_over)
            if platform.dest_centre[0] < -200:
                self.to_delete.append(platform)

        self.wheel.draw(canvas)
        if self.game_over:
            canvas.draw_text('GAME OVER', (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2), 50, 'Red')

    def delete(self):
        for platform in self.to_delete:
            self.to_delete.remove(platform)
            self.platform_list.remove(platform)

    def add_platform(self):
        self.platform_list.append(Laser_spritesheet())
        self.platform_count += 1


def time_score():
    global counter
    counter = counter + 1


kbd = Keyboard()
wheel = Wheel(
    SHEET_IMG,
    Vector(CANVAS_DIMS[1] / 2.7, CANVAS_DIMS[1]),
    SHEET_WIDTH, SHEET_HEIGHT,
    SHEET_COLUMNS, SHEET_ROWS,
    40)
clock = Clock()

background =  Background(Vector(800, 200))
inter = Interaction(wheel, kbd, background, clock)

frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('#bfcf46')
frame.set_draw_handler(inter.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
timer = simplegui.create_timer(2000, inter.add_platform)
timer.start()

frame.start()
