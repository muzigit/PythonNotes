# 图形界面

# python支持的图形界面的第三方库,如:Tk/wxWidgets/Qt/GTK等
# python自带的库是支持Tk的Tkinter,无需安装任何包,即可使用

# 示例:
# 使用Tkinter进行GUI编程,编写一个GUI版本的'Hello,world!'
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # pack()方法把widget加入到父容器中,并实现布局
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 设置输入框
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        # self.nameInput.get()获得用户输入的文本
        name = self.nameInput.get() or 'world'
        # tkMessageBox.showinfo()可以弹出消息对话框
        messagebox.showinfo('Message', 'Hello, %s' % name)


# 测试:
ui = Application()
# 设置窗口标题
ui.master.title('Hello World')
# 主消息循环
ui.mainloop()
