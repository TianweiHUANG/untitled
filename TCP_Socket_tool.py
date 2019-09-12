import time
import globalvar

def TCP_Socket_tool():
    while True:

        if globalvar.get_value("Connect")==True:
            globalvar.set_value("Connect",False)
            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("send_Message"))
            print("Connect=True")
        if globalvar.get_value("Send")==True:
            globalvar.set_value("Send",False)
            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("send_Message"))
            print("Send=True")
        if globalvar.get_value("Close")==True:
            globalvar.set_value("Close", False)
            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("send_Message"))
            print("Close=True")
        time.sleep(1)

