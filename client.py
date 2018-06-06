#  coding=utf-8

import socket
import time

HOST = '0.0.0.0'
PORT = 8005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
s.connect((HOST, PORT))  # 要连接的IP与端口
while 1:
    s.sendall('python socket is listening')  # 把命令发送给对端
    s.sendall('数据已更新') 
    data = s.recv(3600 * 60)
    print data  # 输出数据
    time.sleep(10)
s.close()  # 关闭连接
