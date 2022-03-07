try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
from VectorClass.vectorClass import Vector
from ball import Keyboard, Wheel, Platform, Clock


CANVAS_DIMS = (800, 500)
SHEET_IMG = "D:\GamesPython\Spritesheet.jpg"

SHEET_WIDTH = 564
SHEET_HEIGHT = 240

SHEET_COLUMNS = 5
SHEET_ROWS = 2

space_timer = 0


class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard
        self.platform_list = []
        self.to_delete = []
        self.platform_count = 0

    def update(self):
        if self.keyboard.space and wheel.on_ground():
            self.wheel.vel.y = -10
            global space_timer
            space_timer = 0
        if self.keyboard.space:
            space_timer += 5
            print(space_timer)
            if space_timer > 10:
                self.wheel.vel.y -= 5
                space_timer = 0
        if not self.keyboard.space and wheel.on_top():
            self.wheel.vel.y = 1

    def draw(self, canvas):
        self.update()
        self.delete()
        wheel.update()
        wheel.draw(canvas)
        clock.tick()
        if clock.transition(4):
            wheel.frame_update()
        print(len(self.platform_list))
        # print(len(self.to_delete))
        for platform in self.platform_list:
            platform.draw(canvas)
            if platform.x < -platform.dimentions[2]:
                self.to_delete.append(platform)

    def delete(self):
        for platform in self.to_delete:
            self.to_delete.remove(platform)
            self.platform_list.remove(platform)

    def add_platform(self):
        if self.platform_count % 4 == 0:
            self.platform_list.append(Platform("vertical", randomPlatform()))
        else:
            self.platform_list.append(Platform("horizontal", randomPlatform()))
        self.platform_count += 1


def randomPlatform():
    lenght = random.randint(100, 200)
    y1 = random.randint(5, CANVAS_DIMS[1]-30)
    y2 = y1 + lenght
    return (y1, y2, lenght)


kbd = Keyboard()
wheel = Wheel(
    SHEET_IMG,
    Vector(CANVAS_DIMS[1] / 2.7, CANVAS_DIMS[0]),
    SHEET_WIDTH, SHEET_HEIGHT,
    SHEET_COLUMNS, SHEET_ROWS,
    40)
clock = Clock()
inter = Interaction(wheel, kbd)

print(randomPlatform())
platform = Platform("horizontal", randomPlatform())


# def draw(canvas):
#     inter.update()
#     wheel.update()
#     wheel.on_ground()
#     wheel.draw(canvas)


frame = simplegui.create_frame('Interactions', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('#bfcf46')
frame.set_draw_handler(inter.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
timer = simplegui.create_timer(2000, inter.add_platform)
timer.start()
frame.start()
