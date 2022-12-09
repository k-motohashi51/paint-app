# おおひら担当:Tool
import tkinter as tk
   
class Tool:
    def __init__(self):
      self.pen = Pen()
      self.eraser = Eraser()
      self.f_tool = None
      self.radio1 = None
      self.size = None
      self.w_b_pen = None
      self.w_b_eraser = None
      self.pen_small_img = None
      self.eraser_small_img = None
      self.chickness = 0
      self.color = '0x000000'
      self.hand = 1
        
    def create_tool(self, root):
      self.create_frame(root)
      self.create_widgits()
      Pen.create_widgits(self)
      Eraser.create_widgits(self)
        
    def create_frame(self, root):
      self.f_tool = tk.Frame(root, bg = '#383838', pady = 10, padx = 10)
      self.f_tool.pack(fill = tk.X)

    def create_widgits(self):   
      def showchoice(): # radio1の選択肢をクリックした時の処理
        for language, self.get_size in self.size: # ループ開始
          self.get_size = self.select_var.get()
          break
        return self.get_size
        
      
      # radio1ウィジェット
      self.select_var = tk.IntVar() # ウィジェット変数select_varを作成
      self.select_var.set(1) # select_var変数に数値をセット
 
      self.size = [("小",1),("中",2),("大",3)] # リストを定義

      for language, val in self.size: # ループ開始
          self.radio1 = tk.Radiobutton(self.f_tool, text=language, value=val, variable=self.select_var,width = 7,command=showchoice) # リストを選択肢とするradio1ウィジェットを生成
          self.radio1.pack(side=tk.BOTTOM) # radio1ウィジェットを配置

# 親クラス
class Hand:
  def __init__(self):
    pass

# 子クラス(継承)
class Pen(Hand):
  def __init__(self):
    self.w_b_pen = None
    self.pen_small_img = None

  def create_widgits(self):
    def tool_choice(s):
      return s
    self.pen_img = tk.PhotoImage(file="img/p.png")
    self.pen_small_img = self.pen_img.subsample(5, 5)
    self.w_b_pen = tk.Button(self.f_tool,text = "ペン",bg="white",image = self.pen_small_img,compound="top",command=tool_choice(1))
    self.w_b_pen.pack(side = tk.TOP)
  def color():
    Hand.color = '0x000000'
  def size():
    Hand.size = 20

# 子クラス(継承)
class Eraser(Hand):
  def __init__(self):
    self.w_b_eraser = None
    self.eraser_small_img = None

  def create_widgits(self):
    def tool_choice(s):
      return s
    self.eraser_img = tk.PhotoImage(file="img/e.png")
    self.eraser_small_img = self.eraser_img.subsample(5, 5)

    self.w_b_eraser = tk.Button(self.f_tool,text = "消しゴム",bg="white",image = self.eraser_small_img,compound="top",command = tool_choice(2))
    self.w_b_eraser.pack(side = tk.TOP)

  def size():
    Hand.size = 10