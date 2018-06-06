# coding=utf-8

import socket  # socket模块
import commands  # 执行系统命令模块

HOST = '0.0.0.0'
PORT = 8005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
s.bind((HOST, PORT))  # 套接字绑定的IP与端口
s.listen(1)  # 开始TCP监听
while 1:
    conn, addr = s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
    print'Connected by', addr  # 输出客户端的IP地址
    while 1:
        data = conn.recv(3600 * 60)  
        print(data)
        conn.sendall(data)
    conn.close()  # 关闭连接
