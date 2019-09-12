import time
import globalvar

def TCP_Socket_tool():
    while True:
        if globalvar.get_value("Connect")==True:
            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("send_Message"))
            print("Connect=True")
            globalvar.set_value("Connect", False)
        if globalvar.get_value("Send")==True:
            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("send_Message"))
            print("Send=True")
            globalvar.set_value("Send", False)
        if globalvar.get_value("Close")==True:
            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("send_Message"))
            print("Close=True")
            globalvar.set_value("Close", False)
        time.sleep(0.1)

