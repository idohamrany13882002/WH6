# START
counter: int = 1
num: int = int(input("enter a number: "))
while num % 7 == 0:
    if num % 11 == 0:
        break
    counter += 1
    num: int = int(input("enter a number: "))
else:
    print(f" you entered {counter - 1} number divisible by 7")
# END
