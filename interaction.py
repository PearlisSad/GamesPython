try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

from background import *  # Background, ClockBackground
from ball import *  # Keyboard, Wheel, Platform, Clock
from laser import Laser_spritesheet
from explosion import Explosion_spritesheet
background_img = simplegui.load_image(
    'https://raw.githubusercontent.com/PearlisSad/GamesPython/main/backgroundSmaller.png')
#https://cdn.discordapp.com/attachments/932691213721694358/951996954848661504/backgroundSmaller.png
background_centre = (800, 200)
background_dims = (1600, 400)
background_reset = Vector(800, 200)
background_counter = 0

CANVAS_DIMS = (800, 400)
SHEET_IMG = "https://github.com/PearlisSad/GamesPython/blob/main/Spritesheet.png?raw=true"#"D:\GamesPython\Spritesheet.png"
# "https://github.com/PearlisSad/GamesPython/blob/main/Spritesheet_bird.jpg?raw=true"
sheet_still =simplegui.load_image("https://raw.githubusercontent.com/PearlisSad/GamesPython/main/megaman%20standing%20still.png")
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

game_over = False


class Interaction:
    def __init__(self, wheel, keyboard, background, clock):
        self.wheel = wheel
        self.keyboard = keyboard
        self.platform_list = []
        self.to_delete = []
        self.not_in_game_platform = []
        self.platform_count = 0
        self.background = background
        self.clock = clock
        self.game_over = False
        self.score = 0
        self.explosion = None

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

        self.background.update()
        self.wheel.update()
        self.delete()

        clock.tick()
        if clock.transition(4):
            wheel.frame_update()

        for platform in self.platform_list:
            if platform.dims[2] == "vertical":
                if platform.hit_vertical(self.wheel) and platform not in self.not_in_game_platform:
                    if lives.get_text() == "Lives: 1":
                        self.game_over = True
                        self.explosion = Explosion_spritesheet(wheel.pos.get_p())
                        lives.set_text("Lives: 0")
                    else:
                        lives.set_text("Lives: 1")
            else:
                if platform.hit_horizontal(self.wheel) and platform not in self.not_in_game_platform:
                    if lives.get_text() == "Lives: 1":
                        self.game_over = True
                        self.explosion = Explosion_spritesheet(wheel.pos.get_p())
                        lives.set_text("Lives: 0")
                    else:
                        lives.set_text("Lives: 1")

            if platform.dims[4] < -210:
                self.to_delete.append(platform)

            if platform.dest_centre[0] < CANVAS_DIMS[1] / 2.7:
                self.not_in_game_platform.append(platform)

    def draw(self, canvas):
        if self.game_over and self.explosion.done():
            canvas.draw_text('END SCREEN', (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2), 50, 'Red')
            # DRAW THE ENDSCREEN HERE
            #IF NEW GAME CLICKED MAKE self.game_over = FALSE
        elif self.game_over:
            self.explosion.draw(canvas)
            canvas.draw_text('GAME OVER', (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2), 50, 'Red')
        else:
            self.background.draw(canvas)

            time_score()
            if counter % 10 == 0:
                self.score += 1
            canvas.draw_text(str(self.score), pos, size, color)
            distance.set_text("Distance: " + str(self.score) + "M")
            for platform in self.platform_list:
                platform.draw(canvas)
            if self.wheel.on_ground()==False:
                self.wheel.draw(canvas)
            else:
                self.wheel.draw_jump(canvas)


    def delete(self):
        for platform in self.to_delete:
            self.to_delete.remove(platform)
            self.platform_list.remove(platform)
            if platform.dest_centre[0] < -210:
                self.not_in_game_platform.remove(platform)


    def add_platform(self):
        self.platform_list.append(Laser_spritesheet())
        self.platform_count += 1

    def button_handler(self):
        self.game_over = False


def time_score():
    global counter
    counter = counter +  1

def game_handler(canvas):
    inter.update()
    inter.draw(canvas)


kbd = Keyboard()
wheel = Wheel(
    SHEET_IMG,
    Vector(CANVAS_DIMS[1] / 2.7, CANVAS_DIMS[1]),
    SHEET_WIDTH, SHEET_HEIGHT,
    SHEET_COLUMNS, SHEET_ROWS,
    40)
clock = Clock()


background = Background(Vector(800, 200))
inter = Interaction(wheel, kbd, background, clock)

frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('#bfcf46')
frame.set_draw_handler(game_handler)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
timer = simplegui.create_timer(2000, inter.add_platform)
timer.start()

distance = frame.add_label("Distance" + str(counter) + "M")
lives = frame.add_label("Lives: 2")
button2 = frame.add_button('New game', inter.button_handler, 70)

frame.start()
