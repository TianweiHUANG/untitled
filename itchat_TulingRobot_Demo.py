"""
import requests

def requests_weather(city="深圳"):
    cityID_dict = {"深圳": "101280601", "厦门": "101230201"}

    #http://www.weather.com.cn/data/sk/*.html
    #http://www.weather.com.cn/data/cityinfo/*.html
    #http://m.weather.com.cn/data/*.html

    #r = requests.get('http://www.weather.com.cn/data/sk/%s.html'%cityID_dict[city])
    r = requests.get('http://www.weather.com.cn/data/cityinfo/%s.html'%cityID_dict[city])
    #r = requests.get('http://m.weather.com.cn/data/%s.html'%cityID_dict[city])

    r.encoding = 'utf-8'

    print(r.json())
    print(r.json()['weatherinfo']['city'],
          r.json()['weatherinfo']['weather'],
          r.json()['weatherinfo']['temp1'],
          "~",
          r.json()['weatherinfo']['temp2'])

    return r.json()['weatherinfo']['city']+" "+r.json()['weatherinfo']['weather']+" "+\
           r.json()['weatherinfo']['temp1']+"~"+r.json()['weatherinfo']['temp2']
requests_weather("厦门")
"""
"""user:huangtianwei1988@163.com password:huangtianwei1988@163.com's password"""
"""
import requests
apiul="http://www.tuling123.com/openapi/api"
#data={"key":"3b04f75866084b30bede0d341c98c3db","info":"深圳天气","userId":"TulingRobot"}
data={"key":"024848ea750a46f993eba7975330dd1d","info":"翻译","userId":"TulingRobot"}
r=requests.post(apiul,data=data).json()
print(type(r))
print(r)
print(r["text"])
"""

import itchat
import requests

def login_func():
    print('Wechat Login ...')
def exit_func():
    print('Wechat Exit ...')

def get_message(message):
    #apiul = "http://openapi.tuling123.com/openapi/api/v2"
    apiul = "http://www.tuling123.com/openapi/api"
    #data={"key":"3b04f75866084b30bede0d341c98c3db","info":message,"userId":"TulingRobot"}
    data = {"key": "024848ea750a46f993eba7975330dd1d", "info": message, "userId": "TulingRobot"}
    try:
        r = requests.post(apiul, data=data).json()
        print("Reply From TulingRobot:%s" %r["text"])
        return r["text"]
    except:
        return "TulingRobot_Error"

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    my_friend = itchat.search_friends(name=u'武萍萍')
    WuPingping_UserName = my_friend[0]["UserName"]

    print("Message to TulingRobot:%s"%msg['Text'])
    if msg['FromUserName'] == WuPingping_UserName:
        itchat.send_msg(get_message(msg['Text']) or "额..出错啦...",toUserName=WuPingping_UserName)

if __name__ == '__main__':
    itchat.auto_login(hotReload=True, loginCallback=login_func, exitCallback=exit_func)
    itchat.run()