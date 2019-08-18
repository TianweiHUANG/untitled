import requests
apiul="http://www.tuling123.com/openapi/api"
#data={"key":"3b04f75866084b30bede0d341c98c3db","info":"我是谁?","userId":"TulingRobot"}
data={"key":"024848ea750a46f993eba7975330dd1d","info":"你是谁?","userId":"TulingRobot"}
r=requests.post(apiul,data=data).json()
print(r["text"])
