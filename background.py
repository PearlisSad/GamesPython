try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from VectorClass.vectorClass import Vector
background_img = simplegui.load_image(
    'https://raw.githubusercontent.com/PearlisSad/GamesPython/main/backgroundSmaller.png')
#https://cdn.discordapp.com/attachments/932691213721694358/951996954848661504/backgroundSmaller.png
background_centre = (800, 200)
background_dims = (1600, 400)
background_reset = Vector(800, 200)
background_counter = 0


class Background:

    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector()

    def draw(self, canvas):
        self.pos.add(Vector(-5, 0))
        # self.pos.add(self.vel)
        # self.vel.multiply(-0.85)
        self.vel.multiply(0.9)

        canvas.draw_image(background_img,
                          background_centre,
                          background_dims,
                          (self.pos.x, self.pos.y),
                          (1600, 400))
        # print(self.pos.get_p())
        # print(self.pos.x)

    def update(self):
        # print(self.pos.get_p())
        if self.pos.x < 1:
            # print("haha")
            self.pos = Vector(800, 200)  # (background_reset)