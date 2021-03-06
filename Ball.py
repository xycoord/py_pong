class Ball:
    def __init__(self, canvas, canvas_width, canvas_height, x, y, radius):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.velx = 1.7
        self.vely = 1.2
        self.canvas = canvas
        self.ball = canvas.create_oval(x-radius, y-radius, x+radius, y+radius)

    def update(self):
        left, top, right, bottom = self.canvas.coords(self.ball)

        #write collision detection here by setting the velocites
        if right > self.canvas_width or left < 0: self.velx = self.velx - 2*self.velx
        if top > self.canvas_height or bottom < 0: self.vely = self.vely - 2*self.vely

        self.canvas.move(self.ball, self.velx, self.vely)