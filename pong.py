from tkinter import *
from Ball import *

canvas_width = 600
canvas_height = 300

root = Tk()
root.title("Balls!")
root.resizable(False, False)
canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

ball = Ball(canvas, canvas_width, canvas_height, x=20, y=20, radius=10)

def initiate_game_loop():
    ball.update()
    canvas.after(10, initiate_game_loop)
initiate_game_loop()

root.mainloop()
