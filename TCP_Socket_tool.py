import time
import globalvar
import socket

def TCP_Socket_tool():
    while True:
        #1.创建套接字socket
        #tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #2.创建套接字socket,连接服务器
        if globalvar.get_value("Connect")==True:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            dest_ip=globalvar.get_value("Server_IP")
            dest_port=int(globalvar.get_value("Server_PORT"))
            dest_addr=(dest_ip,dest_port)
            tcp_socket.connect(dest_addr)

            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("Send_Message"),globalvar.get_value("Receive_Message"),"Connect=True")
            globalvar.set_value("Connect", False)

        #3.接收/发送数据
        if globalvar.get_value("Send")==True:
            send_data=globalvar.get_value("send_Message")
            tcp_socket.send(send_data.encode("utf-8"))

            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("Send_Message"),globalvar.get_value("Receive_Message"),"Send=True")
            globalvar.set_value("Send", False)
        if globalvar.get_value("Receive")==True:
            recv_data = tcp_socket.recv(1024)
            globalvar.set_value("Receive_Message", recv_data.decode("utf-8"))

            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("Send_Message"),globalvar.get_value("Receive_Message"),"Receive=True")
            globalvar.set_value("Receive", False)

        #4.关闭套接字socket
        if globalvar.get_value("Close")==True:
            tcp_socket.close()

            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("Send_Message"),globalvar.get_value("Receive_Message"),"Close=True")
            globalvar.set_value("Close", False)

        time.sleep(0.1)

