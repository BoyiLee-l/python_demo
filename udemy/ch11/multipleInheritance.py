# 多重繼承範例
class C:
    def do_stuff(self):
        print("hello from class C")

class D:
    def do_another_stuff(self):
        print("hello from class D")
class B(C):
    def do_stuff(self):
        print("hello from class B")

class A(B,D):
    pass

a = A()
a.do_stuff()
a.do_another_stuff()
print(A.mro())