from tkinter import *
from cells import Cell
import settings #Contains all the Constants
import utils

# Instantiate the Window
root = Tk()
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")

#Title to the window
root.title("MINESWEEPER")

#Block the window maximize function
root.resizable(False, False)



#Segment the entire window into 3 frames
#Top-Frame (Frame-1)
top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_prct(percentage=25))

top_frame.place(
    x=0,
    y=0)

# Create the Title
game_title = Label(
    top_frame,
    font=('',30),
    text="Mine-Sweeper")

game_title.place(
    x=utils.width_prct(50),
    y=utils.height_prct(10)
    )

#Left-Frame (Frame-2)
left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(percentage=25),
    height=utils.height_prct(percentage=75))

left_frame.place(
    x=0,
    y=utils.height_prct(25))

# Center-Frame (Frame-3)
center_frame= Frame(
    root,
    bg="black",
    width=utils.width_prct(percentage=75),
    height=utils.height_prct(percentage=75))

center_frame.place(
    x=utils.width_prct(percentage=25),
    y=utils.height_prct(percentage=25))


#Create the Cells
for row in range(settings.GRID_SIZE):
    for column in range(settings.GRID_SIZE):

        c = Cell(row, column)
        c.create_btn_obj(center_frame)
        c.created_btn_obj.grid(
            row = row,
            column=column)
        
Cell.randomize_mines()

Cell.create_label_obj(left_frame)
Cell.created_label_obj.place(x=0, y=0)



root.mainloop()
