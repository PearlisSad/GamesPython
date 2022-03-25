try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
# importing the classes needed from the files used
from background import *  # Background, ClockBackground
from sprite import *  # Keyboard, Sprite, Platform, Clock
from laser import Laser_spritesheet
from explosion import Explosion_spritesheet

# defining background parameters
background_img = simplegui.load_image(
    'https://raw.githubusercontent.com/PearlisSad/GamesPython/main/backgroundSmaller.png')
background_centre = (800, 200)
background_dims = (1600, 400)
background_reset = Vector(800, 200)
background_counter = 0

# defining main menu and end screen image
main_menu_img = simplegui.load_image(
    'https://raw.githubusercontent.com/PearlisSad/GamesPython/main/mainmenu.png')
endscreen_img = simplegui.load_image(
    'https://github.com/PearlisSad/GamesPython/blob/main/endscreen_New.jpg?raw=true')

# defining canvas dimentions
CANVAS_DIMS = (800, 400)
# defining the spritesheet for the main hero
SHEET_IMG = "https://github.com/PearlisSad/GamesPython/blob/main/Spritesheet.png?raw=true"
sheet_still = simplegui.load_image(
    "https://raw.githubusercontent.com/PearlisSad/GamesPython/main/Spritesheet%20for%20jumping.png")
SHEET_WIDTH = 564
SHEET_HEIGHT = 240
SHEET_COLUMNS = 5
SHEET_ROWS = 2

space_timer = 0
# defining background dimentions and origin
SHEET_URL = "https://raw.githubusercontent.com/PearlisSad/GamesPython/aeebe682ce8a4c45eb1e982eed622973b5e06cda/backgroundSprite.png"
BACK_WIDTH = 11520  # 1440
BACK_HEIGHT = 5400  # 1480
BACK_COLUMNS = 6
BACK_ROWS = 5

frame_duration = 15  # frame duration = number of ticks the frame should show for
time = 0

# defining the meters counter
counter = 0

game_over = False

# the Interaction class - combines all interactions from the other files


class Interaction:
    def __init__(self, sprite, keyboard, background, clock):
        self.sprite = sprite
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
        self.game_started = False

    def update(self):
        if self.keyboard.space and sprite.on_ground():
            self.sprite.changeVel(Vector(0, -10))
            #self.sprite.vel.y = -10
            global space_timer
            space_timer = 0
        if self.keyboard.space:
            space_timer += 5
            if space_timer > 10:
                #self.sprite.vel.y -= 5
                self.sprite.changeVel(Vector(0, -5))
                space_timer = 0
        if not self.keyboard.space and sprite.on_top():
            self.sprite.vel.y = 1

        self.background.update()
        self.sprite.update()
        self.delete()

        clock.tick()
        if clock.transition(4):
            sprite.frame_update()

        for platform in self.platform_list:
            if platform.dims[2] == "vertical":
                if platform.hit_vertical(self.sprite) and platform not in self.not_in_game_platform:
                    if lives.get_text() == "Lives: 1":
                        self.game_over = True
                        self.explosion = Explosion_spritesheet(
                            sprite.pos.get_p())
                        lives.set_text("Lives: 0")
                    else:
                        lives.set_text("Lives: 1")
            else:
                if platform.hit_horizontal(self.sprite) and platform not in self.not_in_game_platform:
                    if lives.get_text() == "Lives: 1":
                        self.game_over = True
                        self.explosion = Explosion_spritesheet(
                            sprite.pos.get_p())
                        lives.set_text("Lives: 0")
                    else:
                        lives.set_text("Lives: 1")

            if platform.dims[4] < -210:
                self.to_delete.append(platform)

            if platform.dest_centre[0] < CANVAS_DIMS[1] / 2.7:
                self.not_in_game_platform.append(platform)

    def draw(self, canvas):
        if self.game_over and self.explosion.done():
            # DRAW THE ENDSCREEN HERE
            canvas.draw_image(endscreen_img,
                              (400, 200),
                              (800, 400),
                              (400, 200),
                              (800, 400))
            # IF NEW GAME CLICKED MAKE self.game_over = FALSE
            canvas.draw_text(
                'GAME OVER', (CANVAS_DIMS[0] / 5, CANVAS_DIMS[1] / 2), 50, 'White')
            canvas.draw_text('The Flyy Man travelled ' + str(self.score) +
                             " metres!", (CANVAS_DIMS[0] / 5, 300), 30, 'White')
        elif self.game_over:
            self.background.draw(canvas)
            for platform in self.platform_list:
                platform.draw(canvas)
            #canvas.draw_text('GAME OVER', (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2), 50, 'Red')
            self.explosion.draw(canvas)
        else:
            self.background.draw(canvas)
            time_score()
            if counter % 10 == 0:
                self.score += 1
            if self.score < 50:
                canvas.draw_text(
                    'Press Space to jump', (200, 380), 25, 'White')
            #canvas.draw_text(str(self.score), pos, size, color)
            distance.set_text("Distance: " + str(self.score) + "M")
            for platform in self.platform_list:
                platform.draw(canvas)
            if self.sprite.on_ground():
                self.sprite.draw(canvas)
            else:
                self.sprite.draw_jump(canvas)

    def main_menu(self, canvas):
        if self.game_started == False:
            canvas.draw_image(main_menu_img,
                              (400, 200),
                              (800, 400),
                              (400, 200),
                              (800, 400))
            if self.keyboard.space:
                self.game_started = True
                self.game_restart()
        else:
            self.draw(canvas)

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
        self.game_started = False
        self.score = 0
        distance.set_text("Distance: " + str(self.score) + "M")
        lives.set_text("Lives: 2")
        # self.game_restart()

    def game_restart(self):
        self.platform_list.clear()
        self.not_in_game_platform.clear()
        self.to_delete.clear()


def time_score():
    global counter
    counter = counter + 1


def game_handler(canvas):
    inter.update()
    # inter.draw(canvas)
    inter.main_menu(canvas)


kbd = Keyboard()
sprite = Sprite(
    SHEET_IMG,
    Vector(CANVAS_DIMS[1] / 2.7, CANVAS_DIMS[1]),
    SHEET_WIDTH, SHEET_HEIGHT,
    SHEET_COLUMNS, SHEET_ROWS,
    40)
clock = Clock()


background = Background(Vector(800, 200))
inter = Interaction(sprite, kbd, background, clock)

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
