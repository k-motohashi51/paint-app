import tkinter as tk
from tkinter import ttk

class Menu:
    def __init__(self):
        self.menubar = None
        self.file = None

    def create_menu(self, root):
        self.menubar = tk.Menu(root)
        root.config(menu = self.menubar)

        self.file = tk.Menu(self.menubar)
        self.menubar.add_cascade(label = 'File', menu = self.file)
        self.file.add_command(label = 'New File')
        self.file.add_command(label = 'Save as ...')
        self.file.add_separator()
        self.file.add_command(label = 'Exit')
