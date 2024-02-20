# Write a function called "printMany" that prints out integers 1, 2, 3, ..., 100.
def printMany():
    for i in range(1,101):
        print(i)
# printMany()

# Write a function called "printEvery3" that prints out integers 1, 4, 7, 10, ..., 88.
def printEvery3():
    for i in range(1, 89, 3):
        print(i)
# printEvery3()

# Write a function called "position" that returns a tuple of the first uppercase letter and its index location. If not found, returns -1.
def position(str: str):
    for ind, s in enumerate(str):
        if s == s.upper():
            print((s, ind))
            return (s, ind)
    print(-1)
    return -1
        
# position("abcd")  # returns -1
# position("AbcD")  # returns ('A', 0)
# position("abCD")  # returns ('C', 2)

# Write a function called "findSmallCount" that takes one list of integers and one integer as input, and returns an integer indicating how many elements in the list is smaller than the input integer.
def findSmallCount(lis: list[int], num: int):
    cout = 0
    for i in lis:
        if i < num:
            cout += 1
    print(cout)
    return cout

# findSmallCount([1, 2, 3], 2); # returns 1
# findSmallCount([1, 2, 3, 4, 5], 0); # returns 0

# Write a function called "findSmallerTotal" that takes one list of integers and one integer as input, and returns the sum of all elements in the list that are smaller than the input integer. 
def findSmallerTotal(lis: list[int], num: int):
    total = 0
    for i in lis:
        if i < num:
            total += i
    print(total)
    return total
findSmallerTotal([1, 2, 3], 3) # returns 3
findSmallerTotal([1, 2, 3], 1) # returns 0
findSmallerTotal([3, 2, 5, 8, 7], 999) # returns 25
findSmallerTotal([3, 2, 5, 8, 7], 0) # returns 0

#Write a function called "findAllSmall" that takes one list of integers and another integer as input, and returns an list of integers that contains all elements that are smaller than the input integer.
def findAllSmall(lis: list[int], num: int):
    arr = []
    for i in lis:
        if i < num:
            arr.append(i)
    print(arr)
    return arr
findAllSmall([1, 2, 3], 10); # returns [1, 2, 3]
findAllSmall([1, 2, 3], 2); # returns [1]
findAllSmall([1, 3, 5, 4, 2], 4); #  returns [1, 3, 2]

#Write a function called "summ" that takes one list of numbers, and return the sum of all elements in the input list.
def summ(lis: list[int]):
    total = 0
    for i in lis:
        total += i
    print(total)
    return total
summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]); # returns 55
summ([]); # return 0
summ([-10, -20, -30]); # return -60