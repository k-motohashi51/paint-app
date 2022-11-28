import tkinter as tk
from tkinter import ttk

class Canvas:
    def __init__(self):
        self.f_canvas = None    # frame_canvas
        self.w_canvas = None    # widgit_canvas
        # self.w_canvas_size = None  # 拡大縮小など
        self.is_clicked = None  # クリックされたか
        self.is_being_dragged = None    # ドラッグされているか

    def create_canvas(self, root):
        self.create_frame(root)
        self.create_widgits()
    
    def create_frame(self, root):
        # フレームやwidgitのサイズはroot画面の大きさに応じて変わるといいよね
        self.f_canvas = tk.Frame(root, bg = '#CCFF99', pady = 10, padx = 10)
        self.f_canvas.pack(side = tk.LEFT, fill = tk.Y)

    def create_widgits(self):
        self.w_canvas = tk.Canvas(self.f_canvas, bg = 'white')
        self.w_canvas.pack()

    #def イベントハンドラ関数():
