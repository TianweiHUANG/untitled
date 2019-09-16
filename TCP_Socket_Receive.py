import time
import globalvar
import socket

def TCP_Socket_Receive():
    while True:
        #3.接收数据
        if globalvar.get_value("Receive_Enable")==True:
            try:
                globalvar.set_value("sys_log","Tcp socket is receiving...")

                tcp_socket=globalvar.get_value("tcp_socket")#get_tcp_socket
                recv_data=tcp_socket.recv(1024)
                globalvar.set_value("Receive_Message", recv_data.decode("utf-8"))

                print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                      globalvar.get_value("Send_Message"), globalvar.get_value("Receive_Message"), "Receive=True")
                globalvar.set_value("sys_log", "Tcp socket received...")

            #ConnectionAbortedError:[WinError 10053]您的主机中的软件中止了一个已建立的连接。
            #AttributeError:'str'object has no attribute'decode'
            #except ConnectionAbortedError:
            except :
                print("TCP_Socket_Receive is ConnectionAbortedError...")
            globalvar.set_value("Receive", False)

        time.sleep(0.1)#0.1s