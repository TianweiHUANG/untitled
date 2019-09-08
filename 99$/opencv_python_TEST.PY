"""
#IP摄像头App：http://app.mi.com/details?id=com.shenyaocn.android.WebCam
import cv2
#cv2.namedWindow("camera",1 )
cap = cv2.VideoCapture(0)
f, frame = cap.read()#此刻拍照
#print(f)
#print(frame)
cv2.imwrite("example.png", frame)# 将拍摄内容保存为png图片
cap.release()# 关闭调用的摄像头
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#将照片的颜色去掉，变成黑白照片。
"""
"""
import cv2#导入模块
cap = cv2.VideoCapture(0)#摄像头捕获
cv2.imwrite('img.jpg',cap.read()[1]) #读取图像，并存入图片
"""
import time
#显示画面，按s拍照，按空格退出
import cv2

#捕获摄像头，0代表笔记本内置摄像头，外置摄像头改为1
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("http://admin:admin@192.168.1.101:8081/")
i = 0

while True:
    # 读取图像，ret表示当前帧是否捕获正确，返回布尔值
    ret, frame = cap.read()
    if ret:
        # 将图像显示出来
        cv2.imshow("capture", frame)
    # 画面暂停制定毫秒，期间按了键盘则返回按键的ASCII码，否则返回-1
    k = cv2.waitKey(1)
    # 参数为0表示无线等待，代码会阻塞
    # 不调用waitKey，画面只有一片灰色，而且一闪而过
    # 按空格键退出，ord()函数把字母转化为ASCII码
    if k == ord(' '):
        break
    # 按s键保存
    elif k == ord('s'):

        #localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #localtime = localtime.replace('-', '')
        #localtime = localtime.replace(' ', '')
        #localtime = localtime.replace(':', '')
        localtime = time.strftime("%Y%m%d%H%M%S", time.localtime())

        # 把图像写入图片
        #cv2.imwrite(str(i)+'.jpg', frame)
        cv2.imwrite(localtime+'.jpg', frame)
        i += 1
# # 关闭视频捕获器
cap.release()
# 销毁所有窗口
cv2.destroyAllWindows()