import subprocess

try:
    # 替换下面的路径为你的exe文件的路径
    exe_path = ".\\main.exe"
    # 运行exe文件
    subprocess.run(exe_path)
except FileNotFoundError as e:
    print("main.exe文件未找到")
except Exception as e:
    print(f"未知错误{e}")