import random

#todo: random.random()
# for n in range(10):
#     print(random.random())

#todo: random.randrange() a ~ b -1
for n in range(20):
    print(random.randrange(10, 20))

#todo: random.randint() a ~ b
for n in range(20):
    print(random.randint(10, 20))

#todo: random.seed() 固定取出隨機內容
a = random.Random()
a.seed(10)
for n in range(5):
    print(a.randint(10, 2000))

#todo: random.choice()可以放入Sequence
sentence = "Hi, this is just a sentence"
print(random.choice(sentence))

#todo: random.choices(Sequence, weights = 出現比例, k=數量)
fruits = ["apple", "banana", "cherry"]
result = random.choices(fruits, weights=[1, 1, 2], k=10)
# random.sample的k數量不可以大於陣列內的數量
result2 = random.sample(fruits, k=3)
print(result, result2)
# random.shuffle直接隨機改陣列內的內容
my_tuple = (3, 4, 2, 6, 0, 5, 1)
my_list = random.sample(my_tuple, k=len(my_tuple))
print(my_list)