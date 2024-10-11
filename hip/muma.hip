with open('./start.txt', 'a', encoding='utf-8') as f:
    f.write("123.hip\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 32437))


s.listen(10)

while True:
    clt, adr = s.accept()

    while True:
        ep = ''
        msg = clt.recv(1024)
        msg = msg.decode()
        if msg == 'dir':
            b = ''
            for _filename in os.listdir('./hip'):
                b = str(b) + str(_filename) + '\n'
            clt.send(bytes(b, "utf-8"))
        elif msg == 'exit':
            s.close()
            break
        elif '__read ' in msg:
            with open(f'.\\hip\\{msg[7:]}', 'r', encoding='utf-8') as f:
                ex = ""
                for line in f:
                    ex = str(ex) + str(line) + '\n'
                ep = ex
        elif '__write' in msg:
            clt.send(bytes('w', "utf-8"))
            wr = clt.recv(1024)
            with open(f'.\\hip\\{msg[7:].strip()}', 'w', encoding='utf-8') as f:
                f.write(wr.decode())
        elif msg == 'help':
            ep = "exit:退出\ndir:打印文件列表\n__read [Filename]:打印文件内容\n__write [Filename]:写入文件内容\nset:多功能指令"
        elif msg == 'set start':
            clt.send(bytes('st', "utf-8"))
            s_ = ''
            for _filename in os.listdir('./hip'):
                s_ = str(s_) + str(_filename) + '\n'
            clt.send(bytes(s_, "utf-8"))
            aw = str(clt.recv(1024).decode())
            clt.send(bytes('st_nt', "utf-8"))
            aw2 = str(clt.recv(1024).decode())
            if str(aw2) == '1':
                with open('./start.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{aw}\n")
                    ep = "添加成功"
            elif str(aw2) == '2':
                ep = "暂不支持"
        else:
            if msg.strip() in os.listdir('.\\hip'):
                if ".hip" in msg:
                    with open(f'.\\hip\\{msg}', 'r', encoding='utf-8') as f:
                        ex = ""
                        for line in f:
                            ex = str(ex) + str(line) + '\n'
                        exec(ex)
                else:
                    ep = f"'{msg}'不是内部命令或.hip程序"
            elif msg.strip() == '':
                clt.send(bytes(ep, "utf-8"))

            else:
                ep = f"'{msg}'不是内部命令或.hip程序"
        clt.send(bytes(ep, "utf-8"))