# Write a function called "mySort" that takes an list of integers as input, and returns the sorted version of the input list. You are not allowed to use the built-in sorted() function.
def findMin(lis):
    if lis:
        min_element = lis[0]
    else:
        return "undefined"
    for i in lis:
        if i < min_element:
            min_element = i
    return min_element

def mySort(myList):
    result_list = []
    while len(myList) > 0:
        min_ele = findMin(myList)
        result_list.append(min_ele)
        myList.remove(min_ele)
    print(result_list)
    return result_list
    
mySort([17, 0, -3, 2, 1, 0.5]); # returns [-3, 0, 0.5, 1, 2, 17]

# Write a function called "isPrime" that takes an integer as input, and returns a boolean value that indicates if the input number is prime.
def isPrime(n: int):
    if n == 1:
        print(False)
        return False
    started = 2
    while started < n:
        if n % started == 0:
            print(False)
            return False
        started += 1
    print(True)
    return True
# isPrime(1); # returns false
# isPrime(5); # returns true
# isPrime(91); # returns false
# isPrime(1000000); # returns false

# Write a function called "palindrome" that checks if the input string is a palindrome. (Search on google if you don't know what a palindrome is.)
def palindrome(s: str):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            print(False)
            return False
        left += 1
        right -= 1
    print(True)
    return True

# palindrome("bearaeb"); # true
# palindrome("Whatever revetahW"); # true
# palindrome("Aloha, how are you today?"); # 

# Write a function called "pyramid" that takes an integer as input, and prints a pyramid in the following pattern:
def pyramid(num: int):
    speace = num - 1 #空白
    star = 1 #星星
    for i in range(num):
        print(speace * " " + star * "*")
        star += 2
        speace -= 1


# pyramid(1);
# *
# pyramid(2);
#  *
# ***
# pyramid(4);
#    *
#   ***
#  *****
# *******
# 最底層為(2*n - 1)

# Write a function called "inversePyramid" that draws pyramid upside down.
def inversePyramid(num: int):
    speace = 0 #空白
    star = (num * 2) - 1 #星星
    for i in range(num):
        print(speace * " " + star * "*")
        star -= 2
        speace += 1
inversePyramid(4);
# *******
#  *****
#   ***
#    *

# Given a list of ints, return True if the list contains a 3 next to a 3.
def has_33(lst):
    for i in lst:
        if i == 3 and lst [i + 1] == 3:
          return True
    
    return False

print(has_33([1, 5, 7, 3, 3])) # True
print(has_33([])) # False
print(has_33([4, 3, 2, 1, 0])) # False

# Write a function that check if a list contains a subsequence of 007
def spyGame(lst):
    string = "007"
    pointer_for_lst = 0
    pointer_for_str = 0
    
    while pointer_for_lst < len(lst):
        if lst[pointer_for_lst] == int(string[pointer_for_str]):
            pointer_for_str += 1
            if pointer_for_str == len(string):
                return True 
        pointer_for_lst += 1
    return False

print(spyGame([1, 2, 4, 0, 3, 0, 7])) # True
print(spyGame([1, 2, 5, 0, 3, 1, 7])) # False