# Write a function called "stars" which prints out layers of stars in the following pattern:
def stars(num: int):
    for i in range(1, num + 1):
        print("*" * i)
# stars(1);
# stars(4);

# Write a function called "stars2" which prints out layers of stars in the following pattern:
def stars2(num: int):
    for i in range(1, num + 1):
        print("*" * i)

    for i in range(num - 1, 0, -1):
        print("*" * i)

    print("\n")

stars2(1);
stars2(2);
stars2(3);
stars2(4);

# Write a function called "table" which takes an input n, and prints out n x 1 to n x 9
def table(n:int):
    for i in range(1, 10, 1):
        print(f"{n} x {i} = {n * i}")
# table(3);
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 9 = 27

# Write a function called "table9to9" that prints out the multiplication table:
def table9to9():
    for i in range(1, 10, 1):
        for j in range(1, 10, 1):
            print(f"{i} x {j} = {i * j}")
# table9to9();
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 1 x 9 = 9
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 9 x 9 = 81

# Write a function called "swap" that takes a string as input, and returns a new string with lowercase changed to uppercase, uppercase changed to lowercase.
def swap(s:str):
    result = ""
    for i in s:
        if i == i.upper():
            result += i.lower()
        else:
            result += i.upper()
    print(result)

swap("Aloha"); # returns "aLOHA"
swap("Love you."); # returns "lOVE YOU."

# Write a function called "findMin" which takes an list as input, and returns the minimum element in the input list.
def findMin(lis: [int]):
    if lis:
        min_element = lis[0]
    else:
        print("undefined")
        return "undefined"
    
    for i in lis:
        if i < min_element:
            min_element = i
    print(min_element)
    return min_element

findMin([1, 2, 5, 6, 99, 4, 5]); # returns 1
findMin([]); # returns undefined
findMin([1, 6, 0, 33, 44, 88, -10]); # returns -10