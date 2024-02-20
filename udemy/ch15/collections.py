from collections import Counter
from collections import defaultdict
from collections import namedtuple
from math import sqrt

letters = "aaaaaaaaaaaaaccdddkkkelwmmasdwdw"
c = Counter(letters)
print(c.most_common())

#TODO: defaultdict

# factory function
Harry = defaultdict(lambda: "Wrong key!!")
Harry["name"] = "Harry Potter"
Harry["age"] = 15
print(Harry["name"], Harry["age"], Harry["school"])

#TODO: Named Tuple

Point = namedtuple("Point", ["x", "y"])
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)  

line_length = sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)
print(line_length)

# Namedtuple creates a class
Worker = namedtuple("worker", ["job", "salary", "workplace"])

duncan = Worker("Engineer", 70000, "Taiwan")
print(type(duncan))
print(duncan.job, duncan.salary, duncan.workplace)