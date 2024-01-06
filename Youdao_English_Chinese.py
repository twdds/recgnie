# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document
import requests
import time
import hashlib
import uuid
import requests
from configparser import ConfigParser #用于解析配置文件，尤其是INI文件格式。


def ying_yi_han(text):
    config = ConfigParser() #创建了一个ConfigParser的实例，用于后续解析配置文件。
    if config.read('ID配置.ini'): #使用read方法尝试读取名为ID配置.ini的配置文件
        有道id = config['API_KEYS']['有道id']
        有道secret = config['API_KEYS']['有道secret']
    else:
        messagebox.showerror("错误", "未配置API Key和Secret Key")
        return None

    youdao_url = 'https://openapi.youdao.com/api'  # 有道api地址

    # 需要翻译的文本'
    translate_text = text  # 直接使用传入的文本参数
    print("需要翻译的文本：" + translate_text)

    # 翻译文本生成sign前进行的处理
    input_text = translate_text if len(translate_text) <= 20 else translate_text[:10] + str(
        len(translate_text)) + translate_text[-10:]
    time_curtime = int(time.time())  # 秒级时间戳获取
    app_id = 有道id  # 应用id
    uu_id = uuid.uuid4()  # 随机生成的uuid数
    app_key = 有道secret  # 应用密钥

    sign = hashlib.sha256(
        (app_id + input_text + str(uu_id) + str(time_curtime) + app_key).encode('utf-8')).hexdigest()  # sign生成

    data = {
        'q': translate_text,  # 翻译文本
        'from': "en",  # 源语言
        'to': "zh-CHS",  # 翻译语言
        'appKey': app_id,  # 应用id
        'salt': uu_id,  # 随机生产的uuid码
        'sign': sign,  # 签名
        'signType': "v3",  # 签名类型，固定值
        'curtime': time_curtime,  # 秒级时间戳
    }

    r = requests.get(youdao_url, params=data).json()  # 获取返回的json()内容
    result = r["translation"][0]     # 获取翻译内容
    return result





