import random
import os

main_program_cd = None
app_name = None

class Hie:
    @staticmethod
    def set_app_name(name):
        global app_name
        app_name = name

    @staticmethod
    def get_name(name):
        return f"name:{name}"

    def new_dir(*args):
        len_args = len(args)
        if len_args != 2:
            raise TypeError("参数数量错误")
        if isinstance(args[0], str) is not True:
            raise TypeError("参数类型错误")
        if "name:" not in args[1]:
            raise ValueError("数据错误")
        os.makedirs(f"{args[0]}")
        return f"dir:{args[0]}"

    @staticmethod
    def next_dir(dir_def, name):
        if "dir:" not in dir_def:
            raise ValueError("数据错误")
        # print(dir_def)
        dir_name = dir_def.split(":")[1]
        os.makedirs(f"{dir_name}/{name}")
        return f"dir_next:{dir_name}:{name}"

    @staticmethod
    def new_file(file_name, dir_def, name, main_program=False):
        global main_program_cd
        if "name:" not in name:
            raise ValueError("数据错误")
        if "dir_next:" in dir_def:
            dir_name = dir_def.split(":")[1]
            dir_name2 = dir_def.split(":")[2]
            if main_program:
                main_program_cd = f"{dir_name}/{dir_name2}/{file_name}"
            rd = random.randint(10, 99)
            rd = rd * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
            return f"file_{rd}:{file_name}:{dir_name}/{dir_name2}"
        else:
            dir_name = dir_def.split(":")[1]
            if main_program:
                main_program_cd = f"{dir_name}/{file_name}"
            rd = random.randint(10, 99)
            rd = rd * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
            return f"file_{rd}:{file_name}:{dir_name}"

    @staticmethod
    def write_file(file_write, file_def, name):
        if "name:" not in name:
            raise ValueError("数据错误")
        file_name = file_def.split(":")[1]
        dir_name = file_def.split(":")[2]
        yz = file_def.split(":")[0].split("_")[1]
        yz = int(yz)
        yz = yz / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10
        if str(yz)[-2:] == ".0":
            yz = int(str(yz)[:-2])
        if isinstance(yz, int) is not True:
            os.rmdir(dir_name)
            raise TypeError("验证错误")
        with open(f"{dir_name}/{file_name}", "w", encoding="utf-8") as f:
            f.write(file_write)
            # print(file_write)

    @staticmethod
    def end_install():
        with open("system/apps.txt", "a", encoding="utf-8") as f:
            f.write(f"{app_name}:{main_program_cd}\n")
            print(f"'{app_name}'安装成功")

