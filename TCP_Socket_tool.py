import time
import globalvar
import socket

def TCP_Socket_tool():
    while True:
        if globalvar.get_value("TCP_select")=="As TCP Client":
            #1.创建套接字socket,连接服务器
            if globalvar.get_value("Connect")==True:
                myWindow = globalvar.get_value("myWindow")
                myWindow.printf_sys_log_Func("Tcp socket is connecting...")

                globalvar.set_value("Receive_Enable", False)
                try:
                    tcp_socket.shutdown(socket.SHUT_RDWR)
                    tcp_socket.close()
                except:
                    print("TCP_Socket_Connect As TCP Client is Error...")

                tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                globalvar.set_value("tcp_socket",tcp_socket)
                dest_ip=globalvar.get_value("Server_IP")
                dest_port=int(globalvar.get_value("Server_PORT"))
                dest_addr=(dest_ip,dest_port)
                tcp_socket.connect(dest_addr)

                myWindow.printf_sys_log_Func("Tcp socket connected...")
                globalvar.set_value("Connect", False)
                globalvar.set_value("Receive_Enable",True)
            #2.发送数据
            if globalvar.get_value("Send")==True:
                myWindow = globalvar.get_value("myWindow")
                myWindow.printf_sys_log_Func("Tcp socket is sending...")

                send_data=globalvar.get_value("send_Message")
                tcp_socket.send(send_data.encode("utf-8"))

                myWindow.printf_sys_log_Func("Tcp socket sended...")
                globalvar.set_value("Send", False)
            #4.关闭套接字socket
            if globalvar.get_value("Close")==True:
                globalvar.set_value("Receive_Enable", False)
                myWindow = globalvar.get_value("myWindow")
                myWindow.printf_sys_log_Func("Tcp socket is closing...")

                try:
                   tcp_socket.shutdown(socket.SHUT_RDWR)
                   tcp_socket.close()
                except OSError:
                   print("TCP_Socket_close As TCP Client is Error...")

                myWindow.printf_sys_log_Func("Tcp socket closed...")
                globalvar.set_value("Close", False)
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
        elif globalvar.get_value("TCP_select")=="As TCP Server":

            if globalvar.get_value("Connect") == True:
                myWindow = globalvar.get_value("myWindow")
                myWindow.printf_sys_log_Func("Tcp socket is connecting...")
                globalvar.set_value("Receive_Enable", False)
                try:
                    tcp_socket.shutdown(socket.SHUT_RDWR)
                    tcp_socket.close()
                except:
                    print("TCP_Socket_Connect As TCP Server is Error...")

                tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp_server_socket.bind(("",int(globalvar.get_value("Server_PORT"))))
                tcp_server_socket.listen(128)
                client_socket,client_addr = tcp_server_socket.accept()
                globalvar.set_value("client_socket",client_socket)
                globalvar.set_value("client_addr", client_addr)

                myWindow.printf_sys_log_Func(str(client_socket))
                myWindow.printf_sys_log_Func(str(client_addr))
                myWindow.printf_sys_log_Func("Tcp socket connected...")
                globalvar.set_value("Connect", False)
                globalvar.set_value("Receive_Enable", True)

            if globalvar.get_value("Send") == True:
                myWindow = globalvar.get_value("myWindow")
                myWindow.printf_sys_log_Func("Tcp socket is sending...")

                send_data = globalvar.get_value("send_Message")
                client_socket.send(send_data.encode("utf-8"))

                myWindow.printf_sys_log_Func(str(client_socket))
                myWindow.printf_sys_log_Func(str(client_addr))
                myWindow.printf_sys_log_Func("Tcp socket sended...")
                globalvar.set_value("Send", False)

            if globalvar.get_value("Close") == True:
                globalvar.set_value("Receive_Enable", False)
                myWindow = globalvar.get_value("myWindow")
                myWindow.printf_sys_log_Func("Tcp socket is closing...")

                try:
                    client_socket.shutdown(socket.SHUT_RDWR)
                    tcp_server_socket.shutdown(socket.SHUT_RDWR)
                    client_socket.close()
                    tcp_server_socket.close()
                except OSError:
                    print("TCP_Socket_close As TCP Server is Error...")

                myWindow.printf_sys_log_Func(str(client_socket))
                myWindow.printf_sys_log_Func(str(client_addr))
                myWindow.printf_sys_log_Func("Tcp socket closed...")
                globalvar.set_value("Close", False)

        time.sleep(0.1)