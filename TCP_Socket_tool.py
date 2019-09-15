import time
import globalvar
import socket
"""
>>> import socket
>>> tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> tcp_socket.connect(("192.168.1.101", 1234))
>>> tcp_socket.close()
>>> tcp_socket.connect(("192.168.1.101", 1234))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tcp_socket.connect(("192.168.1.101", 1234))
OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。
>>> #Close之后必须重新创建socket，否则无法重新connect。
"""
"""
>>> import socket
>>> tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> tcp_socket.connect(("192.168.1.101", 1234))
>>> tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
>>> #connect之后不能再次创建socket，否则将自动Close。
"""
def TCP_Socket_tool():
    #tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Close之后必须重新创建socket，否则无法重新connect。
    while True:
        #tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect之后不能再次创建socket，否则将自动Close。

        #1.创建套接字socket,连接服务器
        if globalvar.get_value("Connect")==True:
            globalvar.set_value("sys_log", "Tcp socket is connecting...")

            #解决方式：connect之前tcp_socket.close()。
            globalvar.set_value("Receive_Enable", False)  # Reset_Receive_Enable
            try:
                tcp_socket.close()
            #UnboundLocalError:local variable'tcp_socket'referenced before assignment
            except UnboundLocalError:
                print("TCP_Socket_close is UnboundLocalError...")

            tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            globalvar.set_value("tcp_socket",tcp_socket)#set_tcp_socket
            dest_ip=globalvar.get_value("Server_IP")
            dest_port=int(globalvar.get_value("Server_PORT"))
            dest_addr=(dest_ip,dest_port)
            #在connect之后等待Receive_Message期间，重复connect时报错啦；
            #ConnectionRefusedError:[WinError 10061]由于目标计算机积极拒绝，无法连接；
            tcp_socket.connect(dest_addr)

            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("Send_Message"),globalvar.get_value("Receive_Message"),"Connect=True")
            globalvar.set_value("sys_log", "Tcp socket connected...")
            globalvar.set_value("Connect", False)
            globalvar.set_value("Receive_Enable",True)#Set_Receive_Enable
        #2.发送数据
        if globalvar.get_value("Send")==True:
            globalvar.set_value("sys_log", "Tcp socket is sending...")

            send_data=globalvar.get_value("send_Message")
            tcp_socket.send(send_data.encode("utf-8"))

            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("Send_Message"),globalvar.get_value("Receive_Message"),"Send=True")
            globalvar.set_value("sys_log", "Tcp socket sended...")
            globalvar.set_value("Send", False)
        #3.接收数据
        """
        if globalvar.get_value("Receive")==True:
            globalvar.set_value("sys_log", "Tcp socket is receiving...")
            
            recv_data = tcp_socket.recv(1024)
            globalvar.set_value("Receive_Message", recv_data.decode("utf-8"))

            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("Send_Message"),globalvar.get_value("Receive_Message"),"Receive=True")
            globalvar.set_value("sys_log", "Tcp socket received...")
            globalvar.set_value("Receive", False)
        """
        #4.关闭套接字socket
        if globalvar.get_value("Close")==True:
            globalvar.set_value("Receive_Enable", False)#Reset_Receive_Enable
            globalvar.set_value("sys_log", "Tcp socket is closing...")

            tcp_socket.close()

            print(globalvar.get_value("Server_IP"), globalvar.get_value("Server_PORT"),
                  globalvar.get_value("Send_Message"),globalvar.get_value("Receive_Message"),"Close=True")
            globalvar.set_value("sys_log", "Tcp socket closed...")
            globalvar.set_value("Close", False)

        time.sleep(0.1)#0.1s