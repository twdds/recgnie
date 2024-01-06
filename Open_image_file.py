# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog, messagebox

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

# 调用函数并获取文件路径
image_path = open_file_dialog()

if image_path:
    print("选择的文件路径:", image_path)
