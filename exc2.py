# START
import random

x: int = random.randint(1, 100)
# print (x)
tries: int = 1
y: int = int(input("guess the number: "))
while x != y:
    tries += 1
    if x > y:
        print("your number is to small")
    else:
        print("your number is too big")
    y: int = int(input("guess the number: "))
else:
    print(f"BINGO")
    print(f" you had {tries} tries")
# END
