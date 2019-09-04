"""
import requests

def requests_weather(city="深圳"):
    city_IDdict = {"深圳": "101280601", "厦门": "101230201"}

    #r = requests.get('http://www.weather.com.cn/data/sk/%s.html'%city_IDdict[city])
    r = requests.get('http://www.weather.com.cn/data/cityinfo/%s.html'%city_IDdict[city])
    #r = requests.get('http://m.weather.com.cn/data/%s.html'%city_IDdict[city])
    r.encoding = 'utf-8'
    print(r.json())

    return r.json()['weatherinfo']['city']+" "+r.json()['weatherinfo']['weather']+" "+\
           r.json()['weatherinfo']['temp1']+"~"+r.json()['weatherinfo']['temp2']

print(requests_weather("厦门"))
"""
"""
import requests
apiul="http://www.tuling123.com/openapi/api"
while True:
    date_info=input("Date_info:")
    data={"key":"3b04f75866084b30bede0d341c98c3db","info":date_info,"userId":"TulingRobot"}
    #data={"key":"024848ea750a46f993eba7975330dd1d","info":date_info,"userId":"TulingRobot"}
    reply=requests.post(apiul,data=data).json()
    #<class 'dict'>{'code': 100000, 'text': '厦门:周三 09月04日,小雨 东北风,最低气温25度，最高气温31度。'}
    print("Reply:",reply["text"])
"""
#########################-itchat_TulingRobot_Dome-#########################

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
