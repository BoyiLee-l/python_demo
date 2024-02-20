import exceptions_Test

try:
    num = 30
    exceptions_Test.enter_age(num)
except exceptions_Test.NegativeNumberException as error:
    print(error)
except:
    print("something error")


# guard clauses
def divide(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("Not valid type given!")
    
    if b == 0:
        raise ZeroDivisionError("Second argument cannot be 0")
    
    print(a / b)
    return a/ b

try:
    # divide(10, "hello")
    # divide(10, 0)
    divide(10, 2)
except Exception as e:
    print(e)