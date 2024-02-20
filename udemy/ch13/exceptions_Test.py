# LBYL approach
def safe_divide_1(x, y):
    if y == 0:
        print("Divide by 0 attempt detected")
        return None
    else:
        return x / y

# EAFP (Easier to ask forgivenes than permission)
def safe_divide_2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Divide by 0 attempt detected")
        return None

# safe_divide_2(10, 0)

def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number here:"))
        except ValueError as ve:
            print(f"{ve} Please try again.")
        except:
            print("Invalid number. Please try again.")
        else:
            print(f"Good job! {result}")
            return result
# ask_for_int()
        
class NegativeNumberException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
        if (age < 0):
            print("This is not a valid age!!")
    
def enter_age(age):
        if age < 0:
            raise NegativeNumberException(age)
        
        if age % 2 == 0:
            print("Your age is an even number.")
        else:
            print("Your age is odd.")
        