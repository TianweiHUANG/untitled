#minNeighbors:→太小误检→太大漏检
##################################################-01-##################################################
"""
# 十行代码完成人脸识别-注释版
# bilibili:同济子豪兄
# 20190516

# 导入opencv-python
import cv2

# 读入一张图片，引号里为图片的路径，需要你自己手动设置
img = cv2.imread('image_1.png',1)
img = cv2.imread('image_2.jpg',1)
img = cv2.imread('image_3.png',1)
img = cv2.imread('image_4.jpg',1)
img = cv2.imread('image_5.jpg',1)
img = cv2.imread('image_6.png',1)

# 导入人脸级联分类器引擎，'.xml'文件里包含训练出来的人脸特征
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# 用人脸级联分类器引擎进行人脸识别，返回的faces为人脸坐标列表，1.3是放大比例，5是重复识别次数
faces = face_engine.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)

# 对每一张脸，进行如下操作
for (x,y,w,h) in faces:
    # 画出人脸框，蓝色（BGR色彩体系），画笔宽度为2
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# 在"img2"窗口中展示效果图
cv2.imshow('img2',img)
# 监听键盘上任何按键，如有按键即退出并关闭窗口，并将图片保存为output.jpg
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('image_output.jpg',img)
"""
##################################################-02-##################################################
"""
# 单张图片人脸+眼睛识别
# bilibili视频教程:同济子豪兄
# 2019-5-16

# 导入opencv
import cv2

# 导入人脸级联分类器引擎，'.xml'文件里包含训练出来的人脸特征，cv2.data.haarcascades即为存放所有级联分类器模型文件的目录
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# 导入人眼级联分类器引擎吗，'.xml'文件里包含训练出来的人眼特征
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 读入一张图片，引号里为图片的路径，需要你自己手动设置
img = cv2.imread('image_3.png')

# 用人脸级联分类器引擎进行人脸识别，返回的faces为人脸坐标列表，1.3是放大比例，5是重复识别次数
faces = face_cascade.detectMultiScale(img, 1.3, 5)

# 对每一张脸，进行如下操作
for (x, y, w, h) in faces:
    # 画出人脸框，蓝色（BGR色彩体系），画笔宽度为2
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
    face_area = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(face_area)
    # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
    for (ex, ey, ew, eh) in eyes:
        # 画出人眼框，绿色，画笔宽度为1
        cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

# 在"img2"窗口中展示效果图
cv2.imshow('img2', img)
# 监听键盘上任何按键，如有案件即退出并关闭窗口，并将图片保存为output.jpg
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('image_output.jpg', img)
"""
##################################################-03-##################################################
"""
# 调用电脑摄像头进行实时人脸+眼睛识别，可直接复制粘贴运行
# bilibili视频教程:同济子豪兄
# 2019-5-16
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# 调用摄像头摄像头
cap = cv2.VideoCapture(0)

while (True):
    # 获取摄像头拍摄到的画面
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    img = frame
    for (x, y, w, h) in faces:
        # 画出人脸框，蓝色，画笔宽度微
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
        face_area = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_area)
        # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        for (ex, ey, ew, eh) in eyes:
            # 画出人眼框，绿色，画笔宽度为1
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

    # 实时展示效果画面
    cv2.imshow('frame2', img)
    # 每5毫秒监听一次键盘动作
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 最后，关闭所有窗口
cap.release()
cv2.destroyAllWindows()
"""
##################################################-04-##################################################

# 调用电脑摄像头进行实时人脸+眼睛+微笑识别，可直接复制粘贴运行
# bilibili视频教程:同济子豪兄
# 2019-5-16
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
# 调用摄像头摄像头
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("http://admin:admin@192.168.1.101:8081/")

while (True):
    # 获取摄像头拍摄到的画面
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 2)
    img = frame
    for (x, y, w, h) in faces:
        # 画出人脸框，蓝色，画笔宽度微
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print(faces,type(faces))
        print(x,y,w,h,type(x),type(y),type(w),type(h))
        # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
        face_area = img[y:y + h, x:x + w]

        ## 人眼检测
        # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        eyes = eye_cascade.detectMultiScale(face_area, 1.3, 10)
        for (ex, ey, ew, eh) in eyes:
            # 画出人眼框，绿色，画笔宽度为1
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

        ## 微笑检测
        # 用微笑级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        smiles = smile_cascade.detectMultiScale(face_area, scaleFactor=1.16, minNeighbors=65, minSize=(25, 25),
                                                flags=cv2.CASCADE_SCALE_IMAGE)
        for (ex, ey, ew, eh) in smiles:
            # 画出微笑框，红色（BGR色彩体系），画笔宽度为1
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)
            cv2.putText(img, 'Smile', (x, y - 7), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)

    # 实时展示效果画面
    cv2.imshow('frame2', img)
    # 每5毫秒监听一次键盘动作
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 最后，关闭所有窗口
cap.release()
cv2.destroyAllWindows()

