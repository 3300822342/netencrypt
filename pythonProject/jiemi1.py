import shutil
import os


def move_file_if_key_matches(target_key, source_file, dest_dir):
    """
    如果输入的key匹配，则将文件从source_file移动到dest_dir。
    """
    # 检查输入的key是否匹配
    if target_key == "9b6be13e655b3a00f6b1318122c0f3f9":
        # 确保目标目录存在
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

            # 尝试移动文件
        try:
            shutil.move(source_file, dest_dir)
            print("解密完成。")
        except Exception as e:
            print(f"解密时发生错误: {e}")
    else:
        print("输入的x1key不匹配，操作未执行。")


def jmmain():
    # 硬编码的源文件路径和目标目录路径
    source_file = "D:/x1long/index.html"
    dest_dir = "D:/x1mms/x1mms/templates"

    # 从用户那里获取key
    target_key = input("请输入x1key值：")

    # 调用函数
    move_file_if_key_matches(target_key, source_file, dest_dir)




if __name__ == "__main__":
    jmmain()