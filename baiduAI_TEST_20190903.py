"""
from aip import AipOcr
# 你的 APPID AK SK
APP_ID = '17169607'
API_KEY = 'jGoQmgTGKYFZOzOP5vhh2igD'
SECRET_KEY = input('Secret_Key:')
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image_path = 'baiduai_licensePlate.jpg'
#image_path = 'baiduai_licensePlate-1.jpeg'
image = get_file_content(image_path)

# 调用车牌识别
licensePlate_msg=client.licensePlate(image)
print(licensePlate_msg)
print(licensePlate_msg['words_result']['color'],licensePlate_msg['words_result']['number'])
# 如果有可选参数
#options = {}
#options["multi_detect"] = "true"
# 带参数调用车牌识别
#client.licensePlate(image, options)
"""

# -*- coding: utf-8 -*-
# !/usr/bin/env python
import urllib
import urllib.parse
import urllib.request
import base64
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
client_id = 'jGoQmgTGKYFZOzOP5vhh2igD'
# client_secret = '**************'
client_secret = input("Secret_Key:")

# 获取token
def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    token_content = response.read()
    if token_content:
        token_info = json.loads(token_content.decode("utf-8"))
        token_key = token_info['access_token']
    return token_key

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 获取车牌号信息
def get_license_plate(path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
    f = get_file_content(path)
    access_token = get_token()
    img = base64.b64encode(f)
    params = {"custom_lib": False, "image": img}
    params = urllib.parse.urlencode(params).encode('utf-8')
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        license_plates = json.loads(content.decode("utf-8"))
        strover = '识别结果：'
        words_result = license_plates['words_result']
        number = words_result['number']
        strover += '车牌号：{} \n '.format(number)
        # print (content)
        print(strover)
        return content
    else:
        return ''

image_path = 'baiduai_licensePlate.jpg'
get_license_plate(image_path)
image_path = 'baiduai_licensePlate-1.jpeg'
get_license_plate(image_path)
