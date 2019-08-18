"""深入理解Python装饰器的装饰过程"""
"""
def func_1():
    print("func_1已实现的功能")
def func_1_add(func):
    print("func_1新增加的功能")
    func()

func_1_add(func_1)
"""
"""
def func_1_add(func):
    def func_add():
        print("func_1新增加的功能")
        func()
    return func_add
#@func_1_add
def func_1():
    print("func_1已实现的功能")

func_1=func_1_add(func_1)
func_1()
"""
"""
def func_1_add(func):
    def func_add():
        print("func_1新增加的功能")
        func()
    return func_add
@func_1_add
def func_1():
    print("func_1已实现的功能")

#func_1=func_1_add(func_1)
func_1()
"""
"""
def func_1_add(func):
    def func_add(*args,**kwargs):
        print("func_1新增加的功能")
        func(*args,**kwargs)
    return func_add
@func_1_add
def func_1():
    print("func_1已实现的功能")
@func_1_add
def func_2(num1,num2):
    print("func_1已实现的功能:",num1+num2)

func_1()
func_2(99,199)
"""
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######
"""——itchat_Test_20190816.py——"""
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######
"""
import itchat
itchat.auto_login(hotReload=True)
my_friend = itchat.search_friends(name=u'武萍萍')
WuPingping_UserName = my_friend[0]["UserName"]
itchat.send("Hello PingpingWu", toUserName=WuPingping_UserName)
itchat.logout()
"""
"""10分钟教你用Python实现微信自动回复"""
import itchat
import time
def login_func():
    print('Wechat Login ...')
def exit_func():
    print('Wechat Exit ...')

@itchat.msg_register(itchat.content.TEXT)
#@itchat.msg_register('Text')
def text_reply(msg):
    print(type(msg))
    print(msg)
    if not msg['FromUserName'] == myUserName:
        msg_get=u"[%s]收到好友@%s @%s 的消息:\n%s"\
                %(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(msg['CreateTime'])),
                  msg['User']['NickName'],msg['User']['RemarkName'],msg['Text'])
        msg_reply = u'[自动回复]您好,我现在有事不在,一会儿再和您联系吧...\n已经收到您的的消息:%s'%msg['Text']
        print(msg_get)
        print(msg_reply)
        itchat.send_msg(msg_get,'filehelper')
        return msg_reply
if __name__ == '__main__':
    itchat.auto_login(hotReload=True, loginCallback=login_func, exitCallback=exit_func)
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######
"""itchat_get_head_img_demo"""
"""
<class 'itchat.storage.templates.User'>
{'MemberList': <ContactList: []>, 'UserName': '@d2707ddeedea24777d64aefab81182d7f4ce0f1a394567cf72f9c566e9343ca8', 'City': '', 'DisplayName': '', 'PYQuanPin': '', 'RemarkPYInitial': '', 'Province': '', 'KeyWord': '', 'RemarkName': '', 'PYInitial': '', 'EncryChatRoomId': '', 'Alias': '', 'Signature': '', 'NickName': 'LittleHUANG', 'RemarkPYQuanPin': '', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=464400495&username=@d2707ddeedea24777d64aefab81182d7f4ce0f1a394567cf72f9c566e9343ca8&skey=@crypt_97d40fba_695da294fd080b61074cc3c844e6ac0a', 'UniFriend': 0, 'Sex': 1, 'AppAccountFlag': 0, 'VerifyFlag': 0, 'ChatRoomId': 0, 'HideInputBarFlag': 0, 'AttrStatus': 0, 'SnsFlag': 17, 'MemberCount': 0, 'OwnerUin': 0, 'ContactFlag': 0, 'Uin': 618150705, 'StarFriend': 0, 'Statues': 0, 'WebWxPluginSwitch': 0, 'HeadImgFlag': 1}
<class 'itchat.storage.templates.User'>
{'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@dcc21df2496fd6dfe85b6b745ea3d402b156cae30161aa82bf0583ad642c5909', 'NickName': 'Cherry', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=696958846&username=@dcc21df2496fd6dfe85b6b745ea3d402b156cae30161aa82bf0583ad642c5909&skey=@crypt_97d40fba_695da294fd080b61074cc3c844e6ac0a', 'ContactFlag': 2051, 'MemberCount': 0, 'RemarkName': '武萍萍', 'HideInputBarFlag': 0, 'Sex': 2, 'Signature': '🤔', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'CHERRY', 'PYQuanPin': 'Cherry', 'RemarkPYInitial': 'WPP', 'RemarkPYQuanPin': 'wupingping', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 4199, 'Province': '江西', 'City': '抚州', 'Alias': '', 'SnsFlag': 145, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}
<class 'itchat.storage.templates.User'>
{'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@f51e9c044fb1ed4206a512239451e1351143f36cd761de4ecd9fefc6f5011a40', 'NickName': '刘春华', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=638430943&username=@f51e9c044fb1ed4206a512239451e1351143f36cd761de4ecd9fefc6f5011a40&skey=@crypt_97d40fba_695da294fd080b61074cc3c844e6ac0a', 'ContactFlag': 1, 'MemberCount': 0, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'LCH', 'PYQuanPin': 'liuchunhua', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 4197, 'Province': '北京', 'City': '', 'Alias': '', 'SnsFlag': 1, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}
"""
"""
import itchat
itchat.auto_login(hotReload=True)

friends=itchat.get_friends()
#print(type(friends))
#print(friends)
for friend in friends:
    #print(type(friend))
    #print(friend)
    img=itchat.get_head_img(userName=friend['UserName'])
    path="itchat_get_head_imgHub\\"+friend['NickName']+".jpg"
    print("Downloading:%s's head img..."%friend['NickName'])
    with open(path,"wb") as f:
        f.write(img)
"""
"""itchat_getNote_msg[Text]_Dome"""
"""
"F:\Program Files (x86)\Python37\python.exe" F:/TianweiHUANG_BGI_Backups_20180504_附件/Python_Practise_20190604/PycharmProjects/untitled/itchat_Test_20190816.py
Start auto replying.
<class 'itchat.storage.messagequeue.Message'>
{'MsgId': '8656501658143517703', 'FromUserName': '@cbb9656ea374482f42db3b691942738ccfbc2e076bc2f5535b803c27abcc9c83', 'ToUserName': '@77d295ccd57ab854b17f9c21830cef993552291ff7f3f5ca09347944ca9c20df', 'MsgType': 10000, 'Content': '收到红包，请在手机上查看', 'Status': 3, 'ImgStatus': 1, 'CreateTime': 1566031611, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '', 'AppMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 8656501658143517703, 'OriContent': '', 'EncryFileName': '', 'User': <User: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@cbb9656ea374482f42db3b691942738ccfbc2e076bc2f5535b803c27abcc9c83', 'NickName': 'Cherry', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=696958846&username=@cbb9656ea374482f42db3b691942738ccfbc2e076bc2f5535b803c27abcc9c83&skey=@crypt_97d40fba_a774a391d5ebac1dad0b558daef0a34b', 'ContactFlag': 2051, 'MemberCount': 0, 'RemarkName': '武萍萍', 'HideInputBarFlag': 0, 'Sex': 2, 'Signature': '🤔', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'CHERRY', 'PYQuanPin': 'Cherry', 'RemarkPYInitial': 'WPP', 'RemarkPYQuanPin': 'wupingping', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 4199, 'Province': '江西', 'City': '抚州', 'Alias': '', 'SnsFlag': 145, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}>, 'Type': 'Note', 'Text': '收到红包，请在手机上查看'}
抢红包啦，武萍萍发红包了，快去抢呀...
"""
"""
import itchat
import tkinter
itchat.auto_login(hotReload=True)

def alarm(alarm_user):
    #tkinter.messagebox.showinfo(title='Hi', message='你好！')#提示信息对话窗
    print("抢红包啦，%s发红包了，快去抢呀..."%alarm_user)
@itchat.msg_register('Note',isGroupChat=False)
def getNote(msg):
    print(type(msg))
    print(msg)
    if "收到红包" in msg['Text']:
        alarm("武萍萍")

itchat.run()
"""