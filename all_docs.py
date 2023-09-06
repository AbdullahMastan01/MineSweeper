"""
@IMPORTS:
from tkinter import *

@CODE
1. Instantiate `TK()` as root -> Creates the window
2. Set the window size (root.geometry("WxH"))
3. Give the title (root.title)
4. Block window maximize (root.resizable(False,False))
5. Create Frames i.e divide the `window` into frames/segments
    a. Instantiate `Frame()` -> This is the top frame
    *Args: root, width, height

    b. Place the frame -> x-axis=0, y_axis=0 (top_frame.place())
    *Args: x, y

    c. Instantiate `Frame()` -> This is the left frame

    d. Place the frame -> Place after a+x_axis pixels

    e Instantiate `Frame()` -> This is the center frame



6. File: Cell.py
a. Create a class Cell
*Args: is_mine=False
**Prog:
-Create `self.cell_btn_obj = None` so that button objects can be
stored in it later. This will help us modify its properties
later on!

METHOD:
a. create_btn_object()
**Args: frame
**Prog:
-Instantiate `Button()`  as `btn` and pass `frame` to it | Pass
width and height
-Assign the obj to `self.cell_btn_obj` | 
-use the `bind` method of the `btn` and pass `'<Button-1>'`, (i.e.
Left Mouse Click) `self.left_click_action` (NOTE: Dont call the method
instead just pass its ref)
-Do the same for `'<Button-3>'` (i.e. Right Mouse Click)

b. left_clikc_action()
*Args: event (Not of any use, its meta data that tkinter passes when
`bind` is called)

c right_click_action()
*Args: event

root.mainloop() --> Make the Window

7. Create a nested for loop to iterate over the `grid_size` (from
`settings.py`) | Instantiate `Cell()` | Call the `create_btn_obj` |
use the `self.cell_btn_obj` attr to customize the location of the
button (i.e. cell) -> Use `.grid()` method
    >>`grid()`
    *Args: rows, columns

8. Modify the `Cell` __init__ and pass 2 more args --> x, y (i.e.
the position of the cell) and save them

9. In Main.py pass row, columns from the nested for loop to the
instantiated Cell()

10. Create a static method in `Cell`
--Name: randomize_mines()

11. Create a class attribute
-- all = [] -> store all cell attrs

12. Append all the instans to `all`

13. Cell:
- In randommize_mines();
--- select random cell from `Cell.all`
--- Use for loop to change `self.is_mine` to True

14. In `left_mouse_clikc` method
--Check is cell is a mine | ture: Call `show_mines` | Fales: call
`show_cell`


15. Create a method to show mines
--> The player has lost the game

16. Create a method to surrounding cells
NOTE: The code within should be unmutable. thus use @property decorator
NOTE: @property converts a method into an attribute

--> Create list to store all the surrounding cells of a given cell
NOTE: Edges, Corners, Others will have 5,3,8 surrounders respectivly
--> Add the formula to make fetch the surrounding cells
    --> pass the formula to `get_cell_by_axis`

17. Create a method to return the called cell:
**Name: get_cell_by_axis
**Args: row, column
**For Loop:
--> loop `all` | Compare the row and column args with the
attrs of `all` i.e. cell.row = row nd cell.col == col
**Returns: The cell instance


@property
18. Create a mehtod surrounded cell mines length
**For loop
--> Itreate over surrounded cells
--> Check if its a mine
--> Incremetn a counter
**Retuns: Counter

19. Create a method show cells:
Docs: Reveal the cell (basically its surrounding cell count if its not
a mine)
**Prog:
--> Configure the cell's text and
pass text as the surrounded cell mines length attr


20 if surrounding mine count is 0, reveal them:
**Prog: IF condition:
- Check if surroungind mine count is 0
- Ture -> get surrounding cells
- Pass those cells to `show_cell`

21. Create a method `create cell cout label`
**Args: frame
**Prog:
-Instantiate `Label` as lbl
    @Args: frame, text
-Assing lbl to the class attr `cell_count`

22. Create a class attr `cell_count`

23. In method`show_cell`
**Prog:
- Check if cell is not open,
- True| Decrease the cell_count
- If the `cell_count` is not None
- Ture | Congif the label
- Change is_open to True

24. In init:
-> Create an atttr is_open | set it to False

25. Make Mine Candidate:
**Docs: Mark a cell as to be a mine candidate/ unmark it
-- Make a is_mine_candidate  (instance attr) (Type -> Bool)
-- In the `right_click` method
--IF: Check if is_mine_candidate is false:
-- True | Congif cell to desired color & update is_mine_candidate
--ELSE: Config cell colo to `SystemButtonFace` & update is_mine_candidate
-- In in `show_cell` method
-- Config cell instant to `SystemButtomFace`


EXTRA:
-- Cancel all events for cells that have been revealed
**Prog: `unbind` the cell instances that have been revealed

26. Game Lost:
*Import ctypes , sys
**Prog:
-- In game_lost method, `ctypes.windll.user32.MessageBoxW(0, Body, Title, 0)
-- sys.exit()

27. Game Won:
-- In show cell method:
**Prog:
--IF : cell.cell_count == settings.mine_count
-- True: ctypes.windll.user32.MessageBoxW(0,Body, Title, 0) & sys.exit()

28. Make the Title
-- Use `Label` and place it

@FILES
1. Main.py

2. Settings.py
-- Will contain all the Constantes
a. Widht
b. Height
c. Grid_size
d. Mine_Count
e. Total_cells


3. Utils.py
-- Will contain all functions to calculate different values

4. Cell.py
-- Will contain all the cell for the game
"""
