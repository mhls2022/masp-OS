from os import rmdir, listdir, getcwd, path
import socket
from chinese_python import *
from functools import wraps


# 定义一个装饰器来拦截 os.rmdir 的调用
def intercept_rmdir(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        go = False
        with open("./system/root.txt", 'r', encoding='utf-8') as f:
            if f.read().strip() == "1":
                go = True
        # 在调用前添加自定义逻辑
        # print(f"Intercepted call to rmdir with arguments: {args}, {kwargs}")
        if go:
            rmdir(*args, **kwargs)
        else:
            print("你没有权限")
        # 调用原始的 os.rmdir 函数
        # result = func(*args, **kwargs)

        # 在调用后添加自定义逻辑
        # print(f"rmdir returned: {result}")
        # return result

    return wrapper


# 使用装饰器来包装 os.rmdir 函数
@intercept_rmdir
def rm(path):
    rmdir(path)


exit_ = False
next_run = False


try:
    with open("system/version.txt", 'r', encoding='utf-8') as f:
        for line in f:
            if "v:" in line:
                v = line.strip().strip("v:")
            if "b:" in line:
                b = line.strip().strip("b:")
    print(f'Masp OS欢迎您\n版本:{v}\n补丁号:{b}')

    with open('system/start.txt', 'r', encoding='utf-8') as f:
        print('--开机自启动开始--')
        m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            socket.setdefaulttimeout(1)

            ip_ = '127.0.0.1'

            m.connect((ip_, 27648))

            while True:
                msg = m.recv(1024).decode()
                print(msg)
                if msg == 'reset':
                    with open("system/start.txt", 'w', encoding='utf-8') as f:
                        f.write("")
                    m.send(bytes("yes", 'utf-8'))
                else:
                    msg = str(m.recv(1024).decode())
                    if msg == 'no':
                        m.send(bytes("yes", 'utf-8'))
        except Exception as e:
            socket.setdefaulttimeout(60)
            print(e)
            pass
        for i in f:
            # print(f'>>>{i.strip()}')
            if ".hip" in i:
                with open(f'.\\hip\\{i.strip()}', 'r', encoding='utf-8') as f:
                    ex = ""
                    for line in f:
                        ex = str(ex) + str(line) + '\n'
                    exec(ex)
            else:
                print(f"'{i}'不是.hip程序")
        print('--开机自启动结束--')
    while True:
        a = input(">>>")
        if a == 'dir':
            for _filename in listdir('./hip'):
                print(_filename)
        elif a == 'exit':
            exit()
        elif '__read ' in a:
            with open(f'.\\hip\\{a[7:]}', 'r', encoding='utf-8') as f:
                ex = ""
                for line in f:
                    ex = str(ex) + str(line) + '\n'
                print(ex)
        elif '__write' in a:
            et = random.randint(100000, 999999)
            print(f'你的退出代码为:{et}')
            wr = ""
            i = 1
            while True:
                w = input(f'{i}:')
                if str(w) == str(et):
                    break
                wr = str(wr) + str(w) + '\n'
                i = i + 1
            with open(f'.\\hip\\{a[7:].strip()}', 'w', encoding='utf-8') as f:
                f.write(wr)
        elif a == 'help':
            print("exit:退出\ndir:打印文件列表\n__read [Filename]:打印文件内容\n__write [Filename]:写入文件内容\nset:多功能指令")
        elif a == 'set start':
            for _filename in listdir('./hip'):
                print(_filename)
            aw = input("请输入文件名:")
            aw2 = str(input("1:添加进开机自启动。2:删除"))
            if str(aw2) == '1':
                with open('system/start.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{aw}\n")
                    print("添加成功")
            elif str(aw2) == '2':
                print("暂不支持")
        elif a == 'net connect':
            # print(f"连接码/退出码:{ct}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.bind((socket.gethostname(), 32437))

            # port number can be anything between 0-65535(we usually specify non-previleged ports which are > 1023)

            s.listen(1)

            while True:
                clt, adr = s.accept()

                print(f"已连接至{adr}")
                while True:
                    ep = ''
                    msg = clt.recv(1024)
                    msg = msg.decode()
                    if msg == 'dir':
                        b = ''
                        for _filename in listdir('./hip'):
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
                        for _filename in listdir('./hip'):
                            s_ = str(s_) + str(_filename) + '\n'
                        clt.send(bytes(s_, "utf-8"))
                        aw = str(clt.recv(1024).decode())
                        clt.send(bytes('st_nt', "utf-8"))
                        aw2 = str(clt.recv(1024).decode())
                        if str(aw2) == '1':
                            with open('system/start.txt', 'a', encoding='utf-8') as f:
                                f.write(f"{aw}\n")
                                ep = "添加成功"
                        elif str(aw2) == '2':
                            ep = "暂不支持"
                    else:
                        if msg.strip() in listdir('.\\hip'):
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
        elif "rm" in a:
            with open("./system/root.txt", 'r', encoding='utf-8') as f:
                if f.read().strip() == "1":
                    relative_path = a.strip().replace("rm ", "")
                    current_directory = getcwd()  # 获取当前工作目录
                    full_path = path.join(current_directory, relative_path)
                    if path.exists(full_path):
                        print("正在删除")
                        rmdir(full_path)
                        print("删除成功")
                    else:
                        print("目录不存在")
                else:
                    print(f"'{a}'不是内部命令或.hip程序")
        elif a == "python":
            awp = None
            print("Python 3.12.2 (tags/v3.12.2:69, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32")
            print('Type "help", "copyright", "credits" or "license" for more information.')
            while awp != "quit()" or awp != "exit()":
                try:
                    awp = input(">")
                    exec(awp)
                except Exception as e:
                    print(e)
        else:
            if a.strip() in listdir('.\\hip'):
                if ".hip" in a:
                    with open(f'.\\hip\\{a}', 'r', encoding='utf-8') as f:
                        ex = ""
                        for line in f:
                            ex = str(ex) + str(line) + '\n'
                        exec(ex)
                else:
                    if ".hie" in a:
                        if a.strip() in listdir('.\\hip'):
                            with open(f'.\\hip\\{a}', 'r', encoding='utf-8') as f:
                                ex = ""
                                for line in f:
                                    ex = str(ex) + str(line) + '\n'
                                exec(ex)
            elif a.strip() == "":
                pass
            else:
                with open("system/apps.txt", 'r', encoding='utf-8') as f:
                    # print(1)
                    for line in f:
                        if a.strip() in line.strip():
                            dir_name = line.strip().split(":")[0]
                            # print(a.strip())
                            if a.strip() == dir_name.strip():
                                dir_cd = line.strip().split(":")[1]
                                # print(dir_cd)
                                with open(f'{dir_cd}', 'r', encoding='utf-8') as f:
                                    ex = ""
                                    for line in f:
                                        ex = str(ex) + str(line) + '\n'
                                    exec(ex)
                                    exit_ = True
                                    break
                            else:
                                print(f"'{a}'不是内部命令或.hip程序")
                        else:
                            pass
                    if exit_ is False:
                        print(f"'{a}'不是内部命令或.hip程序")
except Exception as e:
    print(e)
    input()
