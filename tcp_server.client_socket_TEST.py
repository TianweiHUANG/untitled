#########################-tcp_server_socket_TEST.py-#########################
import socket
 
 
def main():
  # 1.创建套接字
  tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # 2.绑定端口
  # addr = ("", 2000)
  addr = ("192.168.43.245", 2000)
  tcp_server_socket.bind(addr)
 
  # 3.监听链接
  tcp_server_socket.listen(128)
 
  # 4.接收别人的连接
  # client_socket用来为这个客户端服务
  client_socket, client_addr = tcp_server_socket.accept()
  print("客户端已连接...")
  
  # 5.接收对方发送的数据
  recv_data = client_socket.recv(1024) 
  print("接收到的数据：%s" % recv_data.decode("utf-8"))
  
  # 6.给对方发送数据
  client_socket.send("hello vivo".encode("utf-8")) 
 
  # 7.关闭套接字 
  client_socket.close()
  tcp_server_socket.close()
 
 
if __name__ == "__main__":
  main()
"""
#########################-tcp_client_socket_TEST.py-#########################
import socket
 
 
def main():
  # 1.创建套接字socket
  tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
  # 2.连接服务器
  dest_ip = input("请输入服务器ip：")
  dest_port = int(input("请输入服务器port："))
  dest_addr = (dest_ip, dest_port)
  tcp_socket.connect(dest_addr)
 
  # 3. 接收/发送数据
  send_data = input("请输入要发送的数据：")
  tcp_socket.send(send_data.encode("utf-8")) 
  
  # 接收服务器发送的数据
  recv_data = tcp_socket.recv(1024)
  print(recv_data.decode("utf-8")) 
 
  # 4. 关闭套接字socket
  tcp_socket.close()
 
if __name__ == "__main__":
 
  main()
"""
