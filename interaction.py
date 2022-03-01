try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
from VectorClass.vectorClass import Vector
from ball import Keyboard, Wheel , Platform


CANVAS_DIMS = (800, 600)
space_timer = 0


class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

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

    def draw(self, canvas):
        self.update()
        wheel.update()
        wheel.on_ground()
        wheel.draw(canvas)
        platform.draw(canvas)
        platform.update()


def randomPlatform():
    lenght = random.randint(25,100)
    y1 = random.randint(5, CANVAS_DIMS[1]-30)
    y2 = y1 + lenght
    return (y1, y2)




kbd = Keyboard()
wheel = Wheel(Vector(CANVAS_DIMS[1] / 2.7, CANVAS_DIMS[0]), 40)
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
frame.start()
