print("we are running codes in hello.py now!")

def get_name():
    print(__name__)

if __name__ == "__main__":
    print("we are running hello.py")
    get_name()
else:
    print("hello.py is being imported") 
    get_name()

