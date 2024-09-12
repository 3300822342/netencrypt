import shutil
import os


def move_file(source_path, dest_dir):
    """
    将文件从source_path移动到dest_dir，如果dest_dir不存在则创建它。
    """
    # 确保目标目录存在
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

        # 使用shutil.move来移动文件
    try:
        shutil.move(source_path, dest_dir)
        print("该文件的x1key值为:")
    except Exception as e:
        print(f"移动文件时发生错误: {e}")


def t1main():
    # 用户输入文件路径
    source_path = input("请输入文件路径:")
    # 定义目标目录路径
    dest_dir = "D:/x1long"

    # 检查用户输入的文件路径是否有效
    if not os.path.isfile(source_path):
        print("输入的文件路径不存在，请检查。")
        return

        # 移动文件
    move_file(source_path, dest_dir)

    # 在控制台输出文本
    print("bc4084505051278c114124f20d7bc16c")


if __name__ == "__main__":
    t1main()