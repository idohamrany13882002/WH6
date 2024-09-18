# START
x: int = int(input("enter a number: "))
for i in range(1, x + 1):
    # print (i)
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(x - 1, 1-1, -1):
    # print (i)
    for j in range(1, i + 1, ):
        print(j, end=" ")
    print()
# END
