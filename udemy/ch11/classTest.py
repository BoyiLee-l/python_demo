# oop example：繼承 private
class Robot:
    """Robot class is for creating robots"""
    ingredient = "metal"
    def __init__(self, name):
        self.name = name
        self.__age = 20
        

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours.")

    @staticmethod
    def greet():
        print("A robot says hi...")


my_robot_1 = Robot("duncan")
my_robot_1.sleep(10)
my_robot_1.__class__.greet()

class newRobot(Robot):
    def __init__(self, name, color):
       super().__init__(name)
       self.color = color
    
    def get_color(self):
        print(f"{self.name} is a {self.color} color.")
new_robot = newRobot("ken", "white")
new_robot.get_color()
new_robot.sleep(15)

# @staticmethod and @classmethod Example
class Circle:
    pi = 3.14159
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return self.__class__.pi * (self.radius ** 2)
    
    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total
    
    @classmethod
    def total_area2(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total
c1 = Circle(15)
print(c1.__class__.total_area())
print(c1.__class__.total_area2())

# @property example
class Employee:
    def __init__(self):
        self.income = 0

    def earn_money(self, money):
        self.income += money
    
    @property
    def tax_amount(self):
        return self.income * 0.05

    @tax_amount.setter
    def tax_amount(self, tax):
        self.income = tax * 20

duncan = Employee()
duncan.earn_money(300)
print(duncan.tax_amount)
# duncan.tax_amount = 200
print(duncan.income)