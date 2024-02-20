import os
import sys

print(os.getcwd())
# print(os.pardir)
# print(os.listdir(os.curdir))
# print(os.listdir(os.pardir))
print(os.path.join("utils", "hello.html"))

# TODO: other methods
filepath = "whatever/some/directory/path.jpg" #macos路徑
print(os.path.basename(filepath))
print(os.path.dirname(filepath))
print(os.path.splitext(filepath))
print(sys.platform)

# TODO: os.walk 深度搜索
# for folder, sub_folders, file in os.walk("udemy"):
#     print("-----------------------------------------")
#     print("Currently we are looking at folder " + folder)
#     print("The subfolders in current diretory are:")
#     for sub in sub_folders:
#         print(sub)
#     print("The file in the current directory are:")
#     for f in file:
#         print(f)

# TODO: os.walk 刪除指定文件
for root, dirs, files in os.walk("udemy"):
    print(root)
    for f in files:
        # 使用splitext切割副檔名
        filename, filetype = os.path.splitext(f)
        # 指定副檔名
        if filetype == ".pyc":
            print(os.path.join(root, f))
            # 組合路徑並下指令做事
            # os.remove(os.path.join(root, f))