# おおひら担当:Tool
import tkinter as tk

#################################################

def main():
    app = Application()
    app.run()

#################################################

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
        self.menu = Menu()
        self.canvas = Canvas()
        self.tool = Tool()

        self.menu.create_menu(self.root)
        self.canvas.create_canvas(self.root)
        self.tool.create_tool(self.root)

    def run(self):
        self.create_main_window()
        self.create_widgits()
        self.root.mainloop()

#################################################

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
    
#################################################

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

# 現状のデータを格納
class Data:
    def __init__(self):
        self.tool_color = None
        self.cursor_x = None    # ポインタの位置（Canvas内）
        self.cursor_y = None
        self.cursor_color = None
        # etc

#################################################

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

class Image:
    def __init__(self):
        self.f_img = None
    
    def create_img(self, root):
        self.create_frame(root)
    
    def create_frame(self, root):
        self.f_img = tk.Frame(root)
        # etc

#################################################

if __name__ == '__main__':
    main()