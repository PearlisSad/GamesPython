try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
from VectorClass.vectorClass import Vector
from ball import Keyboard, Wheel, Platform
from background import Background, Clock

CANVAS_DIMS = (800, 500)
space_timer = 0
SHEET_URL = "https://cdn.discordapp.com/attachments/932691213721694358/950287598386036756/Untitled-5.png"
SHEET_WIDTH = 11520#1440
SHEET_HEIGHT = 5400#1480
SHEET_COLUMNS = 6
SHEET_ROWS = 5

frame_duration=15 #frame duration = number of ticks the frame should show for
time=0


class Interaction:
    def __init__(self, wheel, keyboard,background,clock):
        self.wheel = wheel
        self.keyboard = keyboard
        self.platform_list = []
        self.to_delete = []
        self.platform_count = 0
        self.background=background
        self.clock=clock

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
        
        self.clock.tick()
        self.background.draw(canvas)  
        if self.clock.transition(self.background.frame_duration):
            self.background.next_frame() 


    def draw(self, canvas):
        self.update()
        self.delete()
        wheel.update()
        wheel.draw(canvas)
        self.background.draw(canvas)
        print(len(self.platform_list))
        #print(len(self.to_delete))
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
        self.platform_count+=1

        
        

def randomPlatform():
    lenght = random.randint(100,200)
    y1 = random.randint(5, CANVAS_DIMS[1]-30)
    y2 = y1 + lenght
    return (y1, y2, lenght)




kbd = Keyboard()
wheel = Wheel(Vector(CANVAS_DIMS[1] / 2.7, CANVAS_DIMS[0]), 40)
clock=Clock(time)
sheet = Background(
    SHEET_URL,
    SHEET_WIDTH, SHEET_HEIGHT,
    SHEET_COLUMNS, SHEET_ROWS,
    frame_duration
)
inter = Interaction(wheel, kbd, sheet, clock)

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
