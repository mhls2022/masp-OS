import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

w = str(input("ip:"))
s.connect((w, 32437))

while True:
    a = input(">>>")
    s.sendto(a.encode(), (w, 32437))
    if a == 'dir':
        msg = s.recv(1024)
        print(msg.decode("utf-8"))
    else:
        msg = str(s.recv(1024).decode())
        if a == 'exit':
            s.close()
        if msg == 'w':
            wr = ''
            et = random.randint(100000, 999999)
            print(f'你的退出代码为:{et}')
            i = 1
            while True:
                w = input(f'{i}:')
                if str(w) == str(et):
                    break
                wr = str(wr) + str(w) + '\n'
                i = i + 1
            s.send(wr.encode())
        elif msg == 'st':
            msg = str(s.recv(1024).decode())
            print(msg)
            aw = input("请输入文件名:")
            s.send(aw.encode())
            nt = str(s.recv(1024).decode())
            if nt == 'st_nt':
                aw2 = str(input("1:添加进开机自启动。2:删除"))
                s.send(aw2.encode())
                ae = str(s.recv(1024).decode())
                print(ae)
        else:
            print(msg, '')
