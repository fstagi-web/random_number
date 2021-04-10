import random
import time

num = random.randint(1,5)
num2 = random.randint(1,5)
game_num = (num,num2)

y_num1 = int(input("What is your first number?\n"))
y_num2 = int(input("What is your second number?\n"))
your_num = (y_num1,y_num2)
print(your_num)
time.sleep(1)
print("and the computers numbers are:\n")
time.sleep(1)
print(game_num)
