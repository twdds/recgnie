# -*- coding: utf-8 -*-
from aip import AipOcr
import tkinter as tk
from tkinter import filedialog
import pyperclip
import pygetwindow as gw
import pyautogui
from configparser import ConfigParser #用于解析配置文件，尤其是INI文件格式。
def baidu_shibie(file_path):
    config = ConfigParser()  # 创建了一个ConfigParser的实例，用于后续解析配置文件。
    if config.read('ID配置.ini'):  # 使用read方法尝试读取名为ID配置.ini的配置文件
        百度app_id = config['API_KEYS']['百度app_id']
        百度api_key = config['API_KEYS']['百度api_key']
        百度secret_key = config['API_KEYS']['百度secret_key']
    else:
        messagebox.showerror("错误", "未配置API Key和Secret Key")
        return None
    # 你的 APPID AK SK
    APP_ID = 百度app_id
    API_KEY = 百度api_key
    SECRET_KEY = 百度secret_key

    # 如果有可选参数
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "false"
    options["language_type"] = "auto_detect"
    options["paragraph"] = "true"
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    if file_path != '':
        image = get_file_content(file_path)
        res_image = client.basicGeneral(image)

    result_text = wordschange(res_image)
    return result_text



def get_file_content(file_path):
    with open(file_path, "rb") as fp:
        return fp.read()
def wordschange(res_image):
    # 检查是否存在'words_result'键
    if 'words_result' in res_image:
        # 获取'words_result'对应的值
        words_result = res_image['words_result']

        # 创建一个空列表用于存储每个段落
        paragraphs_list = []

        # 循环遍历每个'words_result'元素
        for result in words_result:
            # 检查是否存在'words'键
            if 'words' in result:
                # 获取'words'对应的值
                words = result['words']

                # 按换行符分割文本内容，实现分段显示
                paragraphs = words.split('\n')

                # 将每个段落添加到列表中
                paragraphs_list.extend(paragraphs)

        # 将列表中的段落连接起来并返回
        full_text = '\n'.join(paragraphs_list)
        return full_text







if __name__ == "__main__":
    baidu_shibie()