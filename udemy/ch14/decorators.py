def new_decorator(original_func):
    def wrap_func():
        print("Here is some codes before the original function.")
        original_func()
        print("Here is some codes after the original function.")
    return wrap_func

@new_decorator ## 使用decorator(@higher order) 語法去執行new_decorator
def func_needs_decorator():
    print("I am a funtion that needs decorator.")

func_needs_decorator()

# Generator 
# yield

def cube(n):
    for x in range(n):
        yield x ** 3

for element in cube(10):
    print(element)

# yieldfrm

def teachet_id_generator(lst):
    for id in lst:
        yield id

def student_id_generator(lst):
    for id in lst:
        yield id

def get_all_users(slst, tlst):
    yield from teachet_id_generator(tlst)
    yield from student_id_generator(slst)

slst = [1, 5, 8, 10, 12]
tlst = [2, 5, 9, 10, 13]
get_all_users(slst, tlst)

for element in get_all_users(slst, tlst):
    print(element)