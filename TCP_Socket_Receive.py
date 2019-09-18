import time
import globalvar
import socket

def TCP_Socket_Receive():
    while True:
        if globalvar.get_value("TCP_select")=="As TCP Client":
            #3.接收数据
            if globalvar.get_value("Receive_Enable") == True:
                try:
                    myWindow = globalvar.get_value("myWindow")
                    myWindow.printf_sys_log_Func("Tcp socket is receiving...")

                    tcp_socket = globalvar.get_value("tcp_socket")
                    recv_data = tcp_socket.recv(1024)
                    globalvar.set_value("Receive_Message", recv_data.decode("utf-8"))

                    myWindow.printf_sys_log_Func("Tcp socket received...")

                except:
                    print("TCP_Socket_Receive As TCP Client is Error...")
                globalvar.set_value("Receive", False)
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
        elif globalvar.get_value("TCP_select") == "As TCP Server":
            if globalvar.get_value("Receive_Enable") == True:
                try:
                    myWindow = globalvar.get_value("myWindow")
                    myWindow.printf_sys_log_Func("Tcp socket is receiving...")

                    client_socket = globalvar.get_value("client_socket")
                    client_addr = globalvar.get_value("client_addr")
                    recv_data = client_socket.recv(1024)
                    globalvar.set_value("Receive_Message", recv_data.decode("utf-8"))

                    myWindow.printf_sys_log_Func(str(client_socket))
                    myWindow.printf_sys_log_Func(str(client_addr))
                    myWindow.printf_sys_log_Func("Tcp socket received...")
                except:
                    print("TCP_Socket_Receive As TCP Server is Error...")
                globalvar.set_value("Receive", False)

        time.sleep(0.1)