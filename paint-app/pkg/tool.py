# おおひら担当:Tool
import tkinter as tk

class Tool:
    def __init__(self):
        self.f_tool = None
        self.w_b_hand = None    # widgit_button_hand -> 新たにボタンクラスをつくって，そこで生成する
        self.w_b_pen = None

    def create_tool(self, root):
        self.create_frame(root)
        self.create_widgits()
        
    def create_frame(self, root):
        self.f_tool = tk.Frame(root, bg = '#FFFF99', pady = 10, padx = 10)
        self.f_tool.pack(fill = tk.X)

    def create_widgits(self):
        self.w_b_hand = tk.Button(self.f_tool, text = 'Hand')   # アイコン画像をいれるといいかもね
        self.w_b_pen = tk.Button(self.f_tool, text = 'Pen')

        self.w_b_hand.pack(side = tk.TOP)
        self.w_b_pen.pack(side = tk.TOP)

# class Button
#   | 継承      |
#   V 　　      V
# class Hand, class Pen, ...

#################################################