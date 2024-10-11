from chinese_python.implant import *

run_v = """
导入 os
导入 socket


尝试：
    使用 打开（“version.txt“, ‘r‘, encoding=‘utf-8‘） 命名 f：
        迭代循环 line 在 f：
            如果 “v：“ 在 line：
                v = line.strip（）.strip（“v：“）
            如果 “b：“ 在 line：
                b = line.strip（）.strip（“b：“）
    打印（f‘Masp OS欢迎您/n版本：{v}/n补丁号：{b}’）

    使用 打开（‘start.txt‘, ‘r‘, encoding=‘utf-8‘） 命名 f：
        打印（‘--开机自启动开始--‘）
        迭代循环 i 在 f：
            # 打印（f‘>>>{i.strip（）}‘）
            如果 “.hip“ 在 i：
                使用 打开（f‘.//hip//{i.strip（）}‘, ‘r‘, encoding=‘utf-8‘） 命名 f：
                    ex = ““
                    迭代循环 line 在 f：
                        ex = 字符串（ex） + 字符串（line） + ‘/n’
                    exec（ex）
            否则：
                打印（f“‘{i}‘不@&1.hip程序“）
        打印（‘--开机自启动结束--‘）
    while True：
        a = 输入（“>>>“）
        如果 a == ‘dir‘：
            迭代循环 _filename 在 os.listdir（‘.//hip‘）：
                打印（_filename）
        反之可能  a == ‘exit‘：
            exit（）
        反之可能 ‘__read ‘ 在 a：
            使用 打开（f‘.//hip//{a[7：]}‘, ‘r‘, encoding=‘utf-8‘） 命名 f：
                ex = ““
                迭代循环 line 在 f：
                    ex = 字符串（ex） + 字符串（line） + ‘/n’
                打印（ex）
        反之可能 ‘__write‘ 在 a：
            et = random.randint（100000, 999999）
            打印（f‘你的退出代码为：{et}‘）
            wr = ““
            i = 1
            while True：
                w = 输入（f‘{i}：‘）
                如果 str（w） == str（et）：
                    break
                wr = 字符串（wr） + 字符串（w） + ‘/n’
                i = i + 1
            使用 打开（f‘.//hip//{a[7：].strip（）}‘, ‘w‘, encoding=‘utf-8‘） 命名 f：
                f.write（wr）
        反之可能 a == ‘help‘：
            打印（“exit：退出/ndir：打印文件列表/n__read [Filename]：打印文件内容/n__write [Filename]：写入文件内容/nset：多功能指令“）
        反之可能 a == ‘set start‘：
            迭代循环 _filename 在 os.listdir（‘.//hip‘）：
                打印（_filename）
            aw = 输入（“请输入文件名：“）
            aw2 = str（输入（“1：添加进开机自启动。2：删除“））
            如果 str（aw2） == ‘1‘：
                使用 打开（‘.//start.txt‘, ‘a‘, encoding=‘utf-8‘） 命名 f：
                    f.write（f“{aw}/n“）
                    打印（“添加成功“）
            反之可能 str（aw2） == ‘2‘：
                打印（“暂不支持“）
        反之可能 a == ‘net connect‘：
            ct = random.randint（100000, 999999）
            # 打印（f“连接码/退出码：{ct}“）
            s = socket.socket（socket.AF_INET, socket.SOCK_STREAM）

            s.bind（（socket.gethostname（）, 32437））

            # port number can be anything between 0-65535（we usually specify non-previleged ports which are > 1023）

            s.listen（1）

            while True：
                clt, adr = s.accept（）

                打印（f“已连接至{adr}“）
                while True：
                    ep = ‘‘
                    msg = clt.recv（1024）
                    msg = msg.decode（）
                    如果 msg == ‘dir‘：
                        b = ‘‘
                        迭代循环 _filename 在 os.listdir（‘.//hip‘）：
                            b = 字符串（b） + 字符串（_filename） + ’/n‘
                        clt.send（bytes（b, “utf-8“））
                    反之可能 msg == ‘exit‘：
                        s.close（）
                        break
                    反之可能 ‘__read ‘ 在 msg：
                        使用 打开（f‘.//hip//{msg[7：]}‘, ‘r‘, encoding=‘utf-8‘） 命名 f：
                            ex = ““
                            迭代循环 line 在 f：
                                ex = 字符串（ex） + 字符串（line） + ‘/n’
                            ep = ex
                    反之可能 ‘__write‘ 在 msg：
                        clt.send（bytes（‘w‘, “utf-8“））
                        wr = clt.recv（1024）
                        使用 打开（f‘.//hip//{msg[7：].strip（）}‘, ‘w‘, encoding=‘utf-8‘） 命名 f：
                            f.write（wr.decode（））
                    反之可能 msg == ‘help‘：
                        ep = “exit：退出/ndir：打印文件列表/n__read [Filename]：打印文件内容/n__write [Filename]：写入文件内容/nset：多功能指令“
                    反之可能 msg == ‘set start‘：
                        clt.send（bytes（‘st‘, “utf-8“））
                        s_ = ‘‘
                        迭代循环 _filename 在 os.listdir（‘.//hip‘）：
                            s_ = 字符串（s_） + 字符串（_filename） + ‘/n’
                        clt.send（bytes（s_, “utf-8“））
                        aw = str（clt.recv（1024）.decode（））
                        clt.send（bytes（‘st_nt‘, “utf-8“））
                        aw2 = str（clt.recv（1024）.decode（））
                        如果 str（aw2） == ‘1‘：
                            使用 打开（‘.//start.txt‘, ‘a‘, encoding=‘utf-8‘） 命名 f：
                                f.write（f“{aw}/n“）
                                ep = “添加成功“
                        反之可能 str（aw2） == ‘2‘：
                            ep = “暂不支持“
                    否则：
                        如果 msg.strip（） 在 os.listdir（‘.//hip‘）：
                            如果 “.hip“ 在 msg：
                                使用 打开（f‘.//hip//{msg}‘, ‘r‘, encoding=‘utf-8‘） 命名 f：
                                    ex = ““
                                    迭代循环 line 在 f：
                                        ex = 字符串（ex） + 字符串（line） + ‘/n’
                                    exec（ex）
                            否则：
                                ep = f“‘{msg}‘不@&1内部命令或.hip程序“
                        反之可能 msg.strip（） == ‘‘：
                            pass
                        否则：
                            ep = f“‘{msg}’不@&1内部命令或.hip程序“
                    clt.send（bytes（ep, “utf-8“））
        否则：
            如果 a.strip（） 在 os.listdir（‘.//hip‘）：
                如果 “.hip“ 在 a：
                    使用 打开（f‘.//hip//{a}‘, ‘r‘, encoding=‘utf-8‘） 命名 f：
                        ex = ““
                        迭代循环 line 在 f：
                            ex = str（ex） + str（line） + ‘/n‘
                        exec（ex）
                否则：
                    打印（f“‘{a}‘不@&1内部命令或.hip程序“）
            反之可能 a.strip（） == ‘‘：
                pass
            否则：
                打印（f“‘{a}‘不@&1内部命令或.hip程序“）
错误 Exception 命名 e：
    打印（e）
    输入（）"""

run(run_v)
