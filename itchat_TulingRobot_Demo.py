"""user:huangtianwei1988@163.com password:huangtianwei1988@163.com's password"""
"""
import requests
apiul="http://www.tuling123.com/openapi/api"
#data={"key":"3b04f75866084b30bede0d341c98c3db","info":"深圳天气","userId":"TulingRobot"}
data={"key":"024848ea750a46f993eba7975330dd1d","info":"厦门天气","userId":"TulingRobot"}
r=requests.post(apiul,data=data).json()
print(type(r))
print(r)
print(r["text"])
"""

import requests
def requests_weather(city="深圳"):
    cityID_dict={"深圳":"101280601","厦门":"101230201"}
    r = requests.get('http://www.weather.com.cn/data/cityinfo/%s.html'%cityID_dict[city])
    r.encoding = 'utf-8'
    print(r.json()['weatherinfo']['city'],
          r.json()['weatherinfo']['weather'],
          r.json()['weatherinfo']['temp1'],
          "~",
          r.json()['weatherinfo']['temp2'])
    return r.json()['weatherinfo']['city'],r.json()['weatherinfo']['weather'],\
           r.json()['weatherinfo']['temp1'],"~",r.json()['weatherinfo']['temp2']
requests_weather("厦门")
#reply_weather=requests_weather()
#print(type(reply_weather))
#print(reply_weather)

"""
import requests
#http://www.weather.com.cn/data/sk/*.html
#http://www.weather.com.cn/data/cityinfo/*.html
#http://m.weather.com.cn/data/*.html

#cityid:101280601-深圳
#r_Shenzhen = requests.get('http://www.weather.com.cn/data/sk/101280601.html')
r_Shenzhen = requests.get('http://www.weather.com.cn/data/cityinfo/101280601.html')
#r_Shenzhen = requests.get('http://m.weather.com.cn/data/101280601.html')
#cityid:101230201-厦门
#r_Xiamen = requests.get('http://www.weather.com.cn/data/sk/101230201.html')
r_Xiamen = requests.get('http://www.weather.com.cn/data/cityinfo/101230201.html')
#r_Xiamen = requests.get('http://m.weather.com.cn/data/101230201.html')

r_Shenzhen.encoding = 'utf-8'
r_Xiamen.encoding = 'utf-8'
#print(r_Shenzhen.content)
#print(r_Xiamen.content)
#print(r_Shenzhen.json())
#print(r_Xiamen.json())
print(r_Shenzhen.json()['weatherinfo']['city'],
      r_Shenzhen.json()['weatherinfo']['weather'],
      r_Shenzhen.json()['weatherinfo']['temp1'],
      "~",
      r_Shenzhen.json()['weatherinfo']['temp2'])
print(r_Xiamen.json()['weatherinfo']['city'],
      r_Xiamen.json()['weatherinfo']['weather'],
      r_Xiamen.json()['weatherinfo']['temp1'],
      "~",
      r_Xiamen.json()['weatherinfo']['temp2'])
"""