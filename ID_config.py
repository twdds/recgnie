# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser
import os

# 全局变量
config_window = None
config_file_path = "C:\\Screen_Capture\\ID配置.ini"

# 配置窗口的函数
def configure():
    global config_window
    config = ConfigParser()

    if config.read(config_file_path):
        有道id = config['API_KEYS']['有道id']
        有道secret = config['API_KEYS']['有道secret']
        百度app_id = config['API_KEYS']['百度app_id']
        百度api_key = config['API_KEYS']['百度api_key']
        百度secret_key = config['API_KEYS']['百度secret_key']

    else:
        config_window = tk.Tk()
        config_window.title("配置")
        config_window.attributes('-topmost', True) # 将窗口置顶
        # 有道配置
        label_id = tk.Label(config_window, text="有道API Key：")
        label_id.grid(row=0, column=0, padx=10, pady=5)
        entry_id = tk.Entry(config_window)
        entry_id.grid(row=0, column=1, padx=10, pady=5)

        label_secret = tk.Label(config_window, text="有道Secret Key：")
        label_secret.grid(row=1, column=0, padx=10, pady=5)
        entry_secret = tk.Entry(config_window)
        entry_secret.grid(row=1, column=1, padx=10, pady=5)

        # 百度配置
        label_app_id = tk.Label(config_window, text="百度APP_ID：")
        label_app_id.grid(row=2, column=0, padx=10, pady=5)
        entry_app_id = tk.Entry(config_window)
        entry_app_id.grid(row=2, column=1, padx=10, pady=5)

        label_api_key = tk.Label(config_window, text="百度API_KEY：")
        label_api_key.grid(row=3, column=0, padx=10, pady=5)
        entry_api_key = tk.Entry(config_window)
        entry_api_key.grid(row=3, column=1, padx=10, pady=5)

        label_secret_key = tk.Label(config_window, text="百度SECRET_KEY：")
        label_secret_key.grid(row=4, column=0, padx=10, pady=5)
        entry_secret_key = tk.Entry(config_window)
        entry_secret_key.grid(row=4, column=1, padx=10, pady=5)

        button_confirm = tk.Button(config_window, text="确认",
                                   command=lambda: update_config(entry_id, entry_secret, entry_app_id, entry_api_key, entry_secret_key))
        button_confirm.grid(row=5, column=0, columnspan=2, pady=10)

        config_window.mainloop()

    return

# 更新配置信息的函数
def update_config(entry_id, entry_secret, entry_app_id, entry_api_key, entry_secret_key):
    有道id = entry_id.get()
    有道secret = entry_secret.get()
    百度app_id = entry_app_id.get()
    百度api_key = entry_api_key.get()
    百度secret_key = entry_secret_key.get()

    if not (有道id and 有道secret and 百度app_id and 百度api_key and 百度secret_key):
        messagebox.showerror("错误", "所有API Key和Secret Key不能为空")
        return

    config = ConfigParser()
    config['API_KEYS'] = {
        '有道id': 有道id,
        '有道secret': 有道secret,
        '百度app_id': 百度app_id,
        '百度api_key': 百度api_key,
        '百度secret_key': 百度secret_key
    }

    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

    messagebox.showinfo("提示", "配置已更新")

# 更新当前配置的函数
def update_existing_config():
    config = ConfigParser()

    if config.read(config_file_path):
        有道id = config['API_KEYS']['有道id']
        有道secret = config['API_KEYS']['有道secret']
        百度app_id = config['API_KEYS']['百度app_id']
        百度api_key = config['API_KEYS']['百度api_key']
        百度secret_key = config['API_KEYS']['百度secret_key']

        config_window = tk.Tk()
        config_window.title("更新配置")

        label_id = tk.Label(config_window, text="有道API Key：")
        label_id.grid(row=0, column=0, padx=10, pady=5)
        entry_id = tk.Entry(config_window)
        entry_id.insert(0, 有道id)
        entry_id.grid(row=0, column=1, padx=10, pady=5)

        label_secret = tk.Label(config_window, text="有道Secret Key：")
        label_secret.grid(row=1, column=0, padx=10, pady=5)
        entry_secret = tk.Entry(config_window)
        entry_secret.insert(0, 有道secret)
        entry_secret.grid(row=1, column=1, padx=10, pady=5)

        label_app_id = tk.Label(config_window, text="百度APP_ID：")
        label_app_id.grid(row=2, column=0, padx=10, pady=5)
        entry_app_id = tk.Entry(config_window)
        entry_app_id.insert(0, 百度app_id)
        entry_app_id.grid(row=2, column=1, padx=10, pady=5)

        label_api_key = tk.Label(config_window, text="百度API_KEY：")
        label_api_key.grid(row=3, column=0, padx=10, pady=5)
        entry_api_key = tk.Entry(config_window)
        entry_api_key.insert(0, 百度api_key)
        entry_api_key.grid(row=3, column=1, padx=10, pady=5)

        label_secret_key = tk.Label(config_window, text="百度SECRET_KEY：")
        label_secret_key.grid(row=4, column=0, padx=10, pady=5)
        entry_secret_key = tk.Entry(config_window)
        entry_secret_key.insert(0, 百度secret_key)
        entry_secret_key.grid(row=4, column=1, padx=10, pady=5)

        button_confirm = tk.Button(config_window, text="确认",
                                   command=lambda: update_config(entry_id, entry_secret, entry_app_id, entry_api_key, entry_secret_key))
        button_confirm.grid(row=5, column=0, columnspan=2, pady=10)

        config_window.mainloop()
    else:
        messagebox.showerror("错误", "配置文件不存在")

# 检查目录是否存在，不存在则创建
if not os.path.exists("C:\\Screen_Capture"):
    os.makedirs("C:\\Screen_Capture")








