"""
import requests
apiul="http://www.tuling123.com/openapi/api"
#data={"key":"3b04f75866084b30bede0d341c98c3db","info":"我是谁?","userId":"TulingRobot"}
data={"key":"024848ea750a46f993eba7975330dd1d","info":"你是谁?","userId":"TulingRobot"}
r=requests.post(apiul,data=data).json()
print(type(r))
print(r)
print(r["text"])
"""
import requests
#cityID:101280601-深圳
r_Shenzhen = requests.get('http://www.weather.com.cn/data/sk/101280601.html')
#cityID:101230201-厦门
r_Xiamen = requests.get('http://www.weather.com.cn/data/sk/101230201.html')
#print(type(r))
#print(r)
r_Shenzhen.encoding = 'utf-8'
r_Xiamen.encoding = 'utf-8'
#print(type(r.json()))
print(r_Shenzhen.json())
print(r_Xiamen.json())
print(r_Shenzhen.content)
print(r_Xiamen.content)

