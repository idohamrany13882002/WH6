#START
num: int = int(input("enter a number: "))
if num % 5 == 0 and num % 3 == 0:
    print ("fizz buzz")
else:
    if num % 5 == 0:
        print ("fizz")
    elif num % 3 == 0:
        print("buzz")

#END