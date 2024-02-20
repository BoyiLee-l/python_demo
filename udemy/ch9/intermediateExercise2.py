# Write a function called "factorPrime" that takes an integer as input, and returns the prime factorization of the input.

def factorPrime(num: int):
    divisor = 2
    answer = str(num) + " = "
    while divisor <= num:
        if num % divisor == 0:
            num /= divisor
            answer += str(divisor) + " x "
        else:
            divisor += 1
    return answer[:len(answer) - 3]
print(factorPrime(120)) # returns "2 x 2 x 2 x 3 x 5"

# Write a function called "intersection" that takes 2 lists, and returns an list of elements that are in the intersection of 2 list.
def intersection(lst1, lst2):
    result = []
    for i in lst1:
        for j in lst2:
            if i == j:
                result.append(i)
    result2 = list(set(lst1).intersection(set(lst2)))
    print(result, result2)
intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]); # returns [3, 4]

# Write a function called "flatten" that flattens an list.
result = []
def flatten(lst):
    for i in lst:
        if type(i) == type([]):
            flatten(i)
        else:
            result.append(i)
    return result

print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
# returns [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]