from tkinter import *

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2)

    def animate_ball(self):
        delta_x = 3
        delta_y = 3
        self.canvas.move(self.ball, delta_x, delta_y)
        self.canvas.after(50, self.animate_ball)

# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

ball = Ball(canvas, 10, 10, 30, 30)
ball.animate_ball()

root.mainloop()