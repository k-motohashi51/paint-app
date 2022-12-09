import tkinter as tk
from enum import Enum
from tkinter import filedialog
from PIL import ImageTk, Image

def main():
    app = Application()
    app.run()


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

        self.canvas.create_canvas(self.root)
        self.menu.create_menu(self.root, self.canvas)
        self.tool.create_tool(self.root)

    def run(self):
        self.create_main_window()
        self.create_widgits()
        self.root.mainloop()

class Menu:
    def __init__(self):
        self.menu_bar = None
        self.file = None

    def create_menu(self, root, canvas_class):
        self.menu_bar = tk.Menu(root)
        root.config(menu = self.menu_bar)

        self.file = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label = "File", menu = self.file)
        self.file.add_command(label = "New File", command = lambda: canvas_class.new_canvas())
        self.file.add_command(label = "Open Image", command = lambda: self.open_image(canvas_class))
        self.file.add_command(label = "Save as ...", command = lambda: self.file_save_as(canvas_class))
        self.file.add_separator()
        self.file.add_command(label = "Exit")
    
    def open_image(self, canvas_class, event = None):
        file_name = filedialog.askopenfilename(title = "Open file", defaultextension = '.png')
        print(file_name)
        #read_image = Image.open(file_name)
        #photo_image = tk.PhotoImage(image = read_image)
        #canvas_class.open_image_on_canvas(photo_image)
        img = ImageTk.PhotoImage(file = file_name)
        canvas_class.open_image_on_canvas(img)
    
    def file_save_as(self, canvas_class, event = None):
        file_name = filedialog.asksaveasfilename(title = "Save with filename", defaultextension = '.ps')
        canvas_class.save_file(file_name)
    

class Canvas:
    def __init__(self):
        self.f_canvas = None    # frame_canvas
        self.w_canvas = None    # widgit_canvas
        # self.is_clicked = None
        # self.is_being_dragged = None
        self.current_id = -1    # 操作中の図形のID
        self.color = "black"
        self.thickness = None
        self.mode = Mode.PEN
        self.image = None
    
    def create_canvas(self, root):
        self.create_frame(root)
        self.create_widgits()
    
    def create_frame(self, root):
        self.f_canvas = tk.Frame(root, bg = "#CCFF99", pady = 10, padx = 10)
        self.f_canvas.place(relx = 0.0, rely = 0.0, relwidth = 0.7, relheight = 1.0)
    
    def create_widgits(self):
        print("created")
        self.w_canvas = tk.Canvas(self.f_canvas, bg = "white")
        self.w_canvas.place(relx = 0.0, rely = 0.1, relwidth = 1.0, relheight = 0.8)
        self.w_canvas.bind("<Button-1>", self.on_key_left)
        self.w_canvas.bind("<B1-Motion>", self.on_key_left_dragging)
    
    def set_mode(self, mode):
        self.mode = mode

    def on_key_left(self, event):
        if Tool.mode == Mode.PEN or Tool.mode == Mode.ERASER:
            self.current_id = self.w_canvas.create_line(event.x, event.y, event.x, event.y, fill = Tool.color, width = Tool.thickness)
        
    
    def on_key_left_dragging(self, event):
        points = self.w_canvas.coords(self.current_id)
        points.extend([event.x, event.y])
        self.w_canvas.coords(self.current_id, points)

    # Canvasの内容をファイルとして保存
    def save_file(self, file_name):
        print("file_name = " + file_name)
        self.w_canvas.postscript(file = file_name, colormode = "color")
    
    def open_image_on_canvas(self, img):
        print("display Img:" , self.w_canvas.winfo_width()/2 , " : ", self.w_canvas.winfo_height()/2)
        #self.w_canvas.create_image(50, 50, image = img)
        self.image = self.image = img
        self.w_canvas.create_image(0,0, image = self.image, anchor = tk.NW)

        # 無地の新しいキャンバスに遷移
    def new_canvas(self):
        self.w_canvas.destroy()
        self.create_widgits()


class Mode(Enum):
    NONE = 0
    PEN = 1
    ERASER = 2

class Tool:
    # マングリング？
    mode = None
    color = "black"
    thickness = 10

    def __init__(self):
        # ウィジェット
        self.f_tool = None
        self.w_b_pen = None

        # プロパティ
        #self.thickness = None
    
    def create_tool(self, root):
        self.create_frame(root)
        self.create_widgits()

    def create_frame(self, root):
        self.f_tool = tk.Frame(root, bg = "#FFFF99", pady = 10, padx = 10)
        self.f_tool.place(relx = 0.7, rely = 0.0, relwidth = 0.3, relheight = 0.6)
    
    def create_widgits(self):
        self.w_b_pen = tk.Button(self.f_tool, text = "Pen", command = lambda: self.on_button_click(Mode.PEN))
        self.w_b_eraser = tk.Button(self.f_tool, text = "Eraser", command = lambda: self.on_button_click(Mode.ERASER))
        self.w_b_pen.pack(side = tk.TOP)
        self.w_b_eraser.pack(side = tk.TOP)
    
    #@staticmethod
    #def get_mode(self):
    #    return Tool.mode
    
    # ツールの選択状態を設定
    #@staticmethod
    #def get_property(self):
    #    if self.mode == Mode.PEN:
    #        return (color, self.thickness)
    #    if self.mode == Mode.ERASER:
    #        return (self.color, self.thickness)
    
    def on_button_click(self, mode):
        self.mode = mode

        if mode == Mode.PEN:
            Tool.mode = Mode.PEN
            Tool.color = "black"
            self.w_b_pen["state"] = tk.DISABLED
            self.w_b_eraser["state"] = tk.NORMAL
        elif mode == Mode.ERASER:
            Tool.mode = Mode.ERASER
            Tool.color = "white"
            self.w_b_eraser["state"] = tk.DISABLED
            self.w_b_pen["state"] = tk.NORMAL
            # 色ボタンの無効化

        else:
            print("Argue Error")


if __name__ == "__main__":
    main()
