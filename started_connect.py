import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "127.0.0.1"

s.bind((ip, 27648))
s.listen(1)

clt, adr = s.accept()

print(f"已连接至{adr}")

a = None

while a != 'y':
    a = input("是否重置开机启动项?(y/n):")
    if a == 'y':
        clt.send(bytes("reset", 'utf-8'))
        msg = clt.recv(1024).decode()
        print(msg)
    elif a == 'n':
        clt.send(bytes("no", 'utf-8'))
        msg = clt.recv(1024).decode()
        print(msg)
    else:
        pass
