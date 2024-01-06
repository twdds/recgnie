# -*- coding: utf-8 -*-
import os  # 导入系统
import tkinter as tk
from tkinter import scrolledtext
import subprocess
import tkinter as tk
import pyperclip
from tkinter import filedialog, messagebox
from Baidu_Image_Recognition import baidu_shibie
from screen_capture import CTkPrScrn
from Youdao_English_Chinese import ying_yi_han
from tkinter import messagebox  # 导入 messagebox 模块
from ID_config import configure
from ID_config import update_config
from ID_config import update_existing_config
from datetime import datetime


#以下定义类
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("识图翻译")

        # 设置初始界面的长和宽
        self.root.geometry("900x600")

        # 计算屏幕中央位置
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - 900) // 2
        y_coordinate = (screen_height - 600) // 2

        # 设置界面居中
        self.root.geometry(f"900x600+{x_coordinate}+{y_coordinate}")

        # 使用 Grid 布局
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # 创建按钮框架
        buttons_frame = tk.Frame(root)
        buttons_frame.grid(row=0, column=0, sticky="ns")

        button_names = ["打开图片", "截取屏幕", "翻译英文", "复制原文", "复制译文", "更新ID"]
        button_commands = [
            lambda cmd=cmd: cmd() for cmd in
            [self.call_A, self.call_B, self.call_C, self.call_D, self.call_E, self.call_F]
        ]

        for i, (name, command) in enumerate(zip(button_names, button_commands)):
            button = tk.Button(buttons_frame, text=name, command=command, height=2, width=10,
                               relief=tk.GROOVE, font=("Helvetica", 10), bg="#66c2ff", fg="white")
            button.grid(row=i, column=0, pady=2, padx=5, sticky="ew")

        # 创建文本框框架
        text_frame = tk.Frame(root)
        text_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        original_label = tk.Label(text_frame, text="原文", font=("Helvetica", 12, "bold"))
        original_label.grid(row=0, column=0, sticky="w")

        self.original_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=40, height=8)
        self.original_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        text_frame.grid_rowconfigure(1, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)

        translated_label = tk.Label(text_frame, text="译文", font=("Helvetica", 12, "bold"))
        translated_label.grid(row=2, column=0, sticky="w")

        self.translated_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=40, height=8)
        self.translated_text.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        text_frame.grid_rowconfigure(3, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)

    def call_A(self):
        image_path = open_file_dialog()
        if image_path is None:
            image_path = ''
        result = baidu_shibie(image_path)
        self.original_text.delete(1.0, tk.END)  # 清空原文文本框内容
        self.original_text.insert(tk.END, result)  # 插入新的内容
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 构造要写入日志文件的内容
        log_content = f"\n{current_time} \n {result}\n"
        # 指定日志文件路径
        log_file_path = "C:\\Screen_Capture\\日志.txt"
        # 将内容写入日志文件末尾，并指定编码为UTF-8
        with open(log_file_path, "a") as log_file:
            log_file.write(log_content)

    def call_B(self):
        prScrn = CTkPrScrn()

    def call_C(self):
        原文 = self.original_text.get("1.0", tk.END)
        # 判断原文是否为空或不包含英文字母
        if not 原文.strip() or not any(char.isalpha() for char in 原文):
            # 提示用户保证原文包含英文
            messagebox.showinfo("提示", "请保证原文包含英文")
            return
        译文 = ying_yi_han(原文)
        # 将翻译结果显示在第二个文本框中
        self.translated_text.delete(1.0, tk.END)  # 清空译文文本框内容
        self.translated_text.insert(tk.END, 译文)  # 插入新的翻译结果
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 构造要写入日志文件的内容
        log_content = f"\n{current_time} \n {原文}\n{译文}\n"
        # 指定日志文件路径
        log_file_path = "C:\\Screen_Capture\\日志.txt"
        # 将内容写入日志文件末尾，并指定编码为UTF-8
        with open(log_file_path, "a") as log_file:
            log_file.write(log_content)

    def call_D(self):
        # 获取原文文本框中的文本
        原文 = self.original_text.get("1.0", tk.END)

        # 将文本复制到粘贴板
        pyperclip.copy(原文)

        # 弹出消息框提示复制成功
        messagebox.showinfo("成功", "复制成功")

    def call_E(self):
        # 获取译文文本框中的文本
        译文 = self.translated_text.get("1.0", tk.END)
        # 将文本复制到粘贴板
        pyperclip.copy(译文)
        # 弹出消息框提示复制成功
        messagebox.showinfo("成功", "复制成功")

    def call_F(self):
        update_existing_config()


#以下定义函数
def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    file_path = filedialog.askopenfilename(
        title="选择图片文件",
        filetypes=[("JPEG files", "*.jpg;*.jpeg"), ("PNG files", "*.png"), ("Bitmap files", "*.bmp"), ("All files", "*.*")]
    )

    if file_path:
        # 检查文件类型是否为所需类型
        allowed_extensions = (".jpg", ".jpeg", ".png", ".bmp")
        if not file_path.lower().endswith(allowed_extensions):
            # 弹出消息框显示提示信息
            messagebox.showinfo("提示", "请选择图片文件（jpg、jpeg、png、bmp）！")
            return None  # 返回 None 或者其他合适的值表示未选择合适的文件类型

    return file_path


def check_and_create_log_file(directory_path):
    # 检查目录是否存在
    if not os.path.exists(directory_path):
        # 如果不存在，创建目录
        os.makedirs(directory_path)

    # 拼接日志文件的完整路径
    log_file_path = os.path.join(directory_path, "日志.txt")

    # 检查日志文件是否存在
    if not os.path.exists(log_file_path):
        # 如果不存在，创建日志文件
        with open(log_file_path, 'w') as log_file:
            log_file.write("日志文件已创建\n")
        print(f"日志文件已在 {directory_path} 中创建。")
    else:
        print(f"日志文件已存在于 {directory_path} 中。")


if __name__ == "__main__":
    folder_path = "C:\\Screen_Capture"
    check_and_create_log_file(folder_path)
    root = tk.Tk()
    app = MyApp(root)
    configure()
    root.mainloop()




