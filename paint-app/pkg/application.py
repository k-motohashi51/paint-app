import tkinter as tk
from pkg import menu
from pkg import canvas
from pkg import tool
from pkg import image

class Application:
    def __init__(self):
        self.root = None
        self.menu = None
        self.canvas = None
        self.tool = None

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.title('paint-app')
        self.root.attributes('-zoomed', '1')
    
    def create_widgits(self):
        self.menu = menu.Menu()
        self.canvas = canvas.Canvas()
        self.tool = tool.Tool()

        self.menu.create_menu(self.root)
        self.canvas.create_canvas(self.root)
        self.tool.create_tool(self.root)

    def run(self):
        self.create_main_window()
        self.create_widgits()
        self.root.mainloop()