from tkinter import *
from tkinter import ttk
import tkinter as tk


def main():
    app = Application()
    app.create_window()
    app.create_widget()
    app.run()


class Application:
    def __init__(self):
        self.root = Tk()
        self.canvas = None 
        self.menu = None
        self.tool = None

    def create_window(self):
        self.root.title('paint-app-test')
        self.root.attributes('-zoomed', '1')

    def create_widget(self):
        self.canvas = Canvas(self.root)
        self.menu = Menu(self.root)
        self.tool = Tool(self.root)

    def run(self):
        self.root.mainloop()

class Canvas:
    def __init__(self, root):
        self.frame = ttk.Frame(root, padding = 8)
        self.frame.pack()

    def create_canvas(self, img = None):
        # if self.canvas != None:
        #   canvas delete
        if img == None:
            self.canvas = tk.Canvas(self.frame, bg = 'white')

        self.canvas.pack()

    def destroy_canvas(self):
        self.canvas.destroy()


class Menu:
    def __init__(self, root):
        self.frame = ttk.Frame(root, padding = 8)


class Tool:
    def __init__(self, root):
        self.frame = ttk.Frame(root, padding = 8)


if __name__ == '__main__':
    main()
