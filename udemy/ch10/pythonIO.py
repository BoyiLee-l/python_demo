# with open("myFile.txt", mode= "a") as my_file:
#     my_file.write("\nLearing python is so fun.")

# 終極密碼
import random
# 1 - 100
secret = random.randint(1, 100)
min_value = 1
max_value = 100
print(secret)

while True:
    guess = input(f"Make your guess between {min_value} and {max_value}: ")
    if int(guess) < min_value or int(guess) > max_value:
        print("Your guess is not within the range!")
        continue
    if int(guess) == secret:
        print(f"The secert is {secret}")
        break
    elif int(guess) < secret:
        min_value = int(guess)
    else:
        max_value = int(guess)