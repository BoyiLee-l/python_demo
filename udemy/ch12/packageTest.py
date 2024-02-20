from myPackage import some_code, some_more_code
from myPackage.sub_package import hello
import sys

print("we are running codes in two.py.")

def get_name():
    print(f"packTest: {__name__}")

if __name__ == "__main__":
    some_code.some_hello()
    some_more_code.here_is_some_more()
    hello.get_name()
    get_name()



#查看python安裝路徑
# print(sys.path)
#查看__builtins__方法
# print(dir(__builtins__))
print(globals())