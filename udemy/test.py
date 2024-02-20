def multiplication_table():
    for i in range(1, 10):
        for j in range(1, 10):
            result = i * j
            print(f"{i} * {j} = {result}\t", end="")
        print("\n")

# multiplication_table()

global_var = 10

def first_local_scope():
      local_var = 20     # 此為 local variable，
                         # 與 second_local_scope() 的 local_var，
                         # 雖然同名，但兩個是完全不相關的變數

      global_var = 30    # 此為 local variable，
                         # 與 global variable 的同名
      
      print("global_var: ", global_var, ", local_var: ", local_var)
print("global_var: ", global_var)  
first_local_scope()

a = b = c = 10
print("a = ", a, ", b = ", b, ", c = ", c)

# 先放入各種型別的變數
minteger = 10
mstring = "Hi, this is RS."
mfloat = 3.14159
incremental_list = range(10)
float_list = [8.787, -0.618, 3.14e+30]

mix_type_list = [minteger, mstring, 
  				mfloat, incremental_list, float_list, 
  				"I bought a keychron k6, nice~"]
print(mix_type_list)

print(mix_type_list[len(mix_type_list)-2][0])

x = [1,2,3,4]

squared_x = [item ** 2 for item in x if item > 3]
squard_dict = {item: item ** 2 for item in x if item > 3}
x_squard_set = {item ** 2 for item in x}

print(squared_x, squard_dict, x_squard_set)

a = 10
# 如何改變global 
def change(num):
     global a #a會指向global
     a = 25#改的是global
change(a)
print(a)

def myAddition(a, b):
     #加上 doctring
     """"This funtion does addition"""
     print(a + b)
# help(myAddition)


def newAddition(a, b):
     for i in range(a):
          for j in range(b):
               if i == 5 and j == 5:
                    return
               print(i, j)

newAddition(12,10)
