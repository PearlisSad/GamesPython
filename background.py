# "http://www.cs.rhul.ac.uk/courses/CS1830/sprites/runnerSheet.png"

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Background():
    def __init__(self, imgurl, width, height, columns, rows, frame_duration):
        # Why load here and not in the draw method?
        self.img = simplegui.load_image(imgurl)
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows

        self.frame_width = width / columns
        self.frame_height = height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_duration = frame_duration

        self.frame_index = [0, 0]

    def next_frame(self):
        # self.draw(canvas)
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

    def draw(self, canvas):
        # self.next_frame()
        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)
        dest_centre = (400, 250)
        # doesn't have to be same aspect ratio as frame!
        dest_size = (800, 500)  # (100, 100)

        canvas.draw_image(self.img,
                          source_centre,
                          source_size,
                          dest_centre,
                          dest_size)


class ClockBackground():
    def __init__(self, time):
        self.time = time

    def tick(self):
        self.time = self.time+1

    def transition(self, frame_duration):
        if self.time % frame_duration == 0:
            return True
        return False
