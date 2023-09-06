#This script contains the functionality for all the cells
from tkinter import Button, Label
import random
import ctypes
import settings

class Cell:
    all_cells = []
    total_cells = settings.TOTAL_CELLS
    created_label_obj = None
    
    def __init__(self, cell_row, cell_column, is_mine=False):
        self.is_mine = is_mine
        self.cell_row = cell_row
        self.cell_column = cell_column
        self.created_btn_obj = None
        self.is_open = False
        self.is_mine_candidate = False
       

        Cell.all_cells.append(self)
        
    def create_btn_obj(self, frame):
        btn = Button(
            frame,
            width = 10,
            height = 5,
            )

        #Left Mouse Click
        btn.bind('<Button-1>', self.left_mouse_click)

        #Right Mouse Click
        btn.bind('<Button-3>', self.right_mouse_click)
        
        self.created_btn_obj = btn

    @staticmethod
    def create_label_obj(frame):
        lbl = Label(
            frame,
            text = f'TotalCells: {Cell.total_cells}',
            font=("",30))

        Cell.created_label_obj = lbl
        return lbl

    def left_mouse_click(self,event):
        print('Left Clikc')
        if self.is_mine:
            self.game_over()
        else:
            self.surrounded_cells
            self.get_surrounding_mine_count
            
            if self.get_surrounding_mine_count == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.reveal_cell()
            self.reveal_cell()
            
        

    def right_mouse_click(self, event):
        if not self.is_mine_candidate:
            self.created_btn_obj.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.created_btn_obj.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        random_cells = random.sample(
            Cell.all_cells,
            9)

        for cell in random_cells:
            cell.is_mine = True

    def game_over(self):
        self.created_btn_obj.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,"Better Luck Next Time", "Game Over", 0)
        
            
        

    def reveal_cell(self):
        if not self.is_open:
            Cell.total_cells -= 1

        if self.is_mine_candidate:
            self.created_btn_obj.configure(bg='SystemButtonFace')

        if Cell.total_cells == settings.MINE_COUNT:
            ctypes.windll.user32.MessageBoxW(0,"Youv'e Won!","Congratulations",0)
            
            
        self.created_btn_obj.configure(text = self.get_surrounding_mine_count)
        
        Cell.created_label_obj.configure(text=f'Remaining Cells: {Cell.total_cells}')

        self.created_btn_obj.unbind('<Button-3>')
        self.created_btn_obj.unbind('<Button-1>')
                
        self.is_open = True

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.cell_row - 1 , self.cell_column - 1),
            self.get_cell_by_axis(self.cell_row - 1, self.cell_column),
            self.get_cell_by_axis(self.cell_row - 1 , self.cell_column + 1),
            self.get_cell_by_axis(self.cell_row , self.cell_column - 1),
            self.get_cell_by_axis(self.cell_row, self.cell_column + 1),
            self.get_cell_by_axis(self.cell_row + 1 , self.cell_column - 1),
            self.get_cell_by_axis(self.cell_row + 1 , self.cell_column),
            self.get_cell_by_axis(self.cell_row + 1 , self.cell_column + 1)
            ]

        cells = [cell for cell in cells if cell is not None]
        return cells
        
    
    def get_cell_by_axis(self,row, column):
        for cell in Cell.all_cells:
            if cell.cell_row == row and cell.cell_column == column:
                return cell

    @property
    def get_surrounding_mine_count(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
                

    def __repr__(self):
        return f"Cell({self.cell_row},{self.cell_column})"

    
    
            

        

