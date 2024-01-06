# -*- coding: utf-8 -*-

from time import sleep
from PIL import Image, ImageGrab
import tkinter
import ctypes
import subprocess

class CTkPrScrn:
    def __init__(self):
        # 初始化一些变量，包括起始坐标、缩放比例等
        self.__start_x, self.__start_y = 0, 0
        self.__scale = 1
        self.image_path = None  # 添加image_path变量

        # 创建一个 tkinter 窗口对象
        self.__win = tkinter.Tk()
        self.__win.attributes("-alpha", 0.5)
        self.__win.attributes("-fullscreen", True)
        self.__win.attributes("-topmost", True)

        # 获取屏幕的宽度和高度
        self.__width, self.__height = self.__win.winfo_screenwidth(), self.__win.winfo_screenheight()

        # 创建一个画布对象，填充为灰色，大小与屏幕一致
        self.__canvas = tkinter.Canvas(self.__win, width=self.__width, height=self.__height, bg="gray")

        # 绑定鼠标事件（左键点击、释放和移动），以及 Esc 键退出事件
        self.__win.bind('<Button-1>', self.xFunc1)
        self.__win.bind('<ButtonRelease-1>', self.xFunc1)
        self.__win.bind('<B1-Motion>', self.xFunc2)
        self.__win.bind('<Escape>', lambda e: self.__win.destroy())

        # 使用 ctypes 库获取屏幕分辨率相关信息
        user32 = ctypes.windll.user32
        gdi32 = ctypes.windll.gdi32
        dc = user32.GetDC(None)
        widthScale = gdi32.GetDeviceCaps(dc, 8)
        heightScale = gdi32.GetDeviceCaps(dc, 10)
        width = gdi32.GetDeviceCaps(dc, 118)
        height = gdi32.GetDeviceCaps(dc, 117)
        self.__scale = width / widthScale
        print(self.__width, self.__height, widthScale, heightScale, width, height, self.__scale)

        self.__win.mainloop()

    def get(self):
        self.__win.update()
        sleep(0.5)
        self.__win.destroy()
        print(self.image_path)

        # 打开文件夹
        folder_path = r'C:\Screen_Capture'
        subprocess.Popen(f'explorer {folder_path}')  # 使用系统默认的文件管理器打开文件夹

        return self.image_path

    def xFunc1(self, event):
        if event.state == 8:
            self.__start_x, self.__start_y = event.x, event.y
        elif event.state == 264:
            if event.x == self.__start_x or event.y == self.__start_y:
                return
            im = ImageGrab.grab((self.__scale * self.__start_x, self.__scale * self.__start_y,
                                 self.__scale * event.x, self.__scale * event.y))
            imgName = '截屏.jpg'
            save_path = r'C:\Screen_Capture\{}'.format(imgName)
            im.save(save_path)
            print('保存成功:', save_path)
            # 将完整路径赋予image_path
            self.image_path = save_path

            self.get()  # 使用 get 函数获取截屏图片的地址

    def xFunc2(self, event):
        if event.x == self.__start_x or event.y == self.__start_y:
            return
        self.__canvas.delete("prscrn")
        self.__canvas.create_rectangle(self.__start_x, self.__start_y, event.x, event.y,
                                       fill='white', outline='red', tag="prscrn")
        self.__canvas.pack()


if __name__ == '__main__':
    prScrn = CTkPrScrn()
