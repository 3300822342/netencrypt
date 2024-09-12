import os
import shutil
import t1
import jiemi1


def run_script(script_name):
    """
    运行指定的Python脚本。
    """
    import subprocess
    subprocess.run(['python', script_name])


def main():
    print("按1加密文件or按2解密x1key值")
    choice = input("请输入你的选择（1/2）：")

    if choice == '1':
        print("正在执行加密操作...")
        run_script('t1.py')  # t1.py是加密文件的脚本
        t1.t1main()
    elif choice == '2':
        print("正在执行解密操作...")
        run_script('jiemi1.py')  # jiemi1.py是解密x1key值的脚本
        jiemi1.jmmain()
    else:
        print("无效的选择，请输入1或2。")


if __name__ == "__main__":
    main()