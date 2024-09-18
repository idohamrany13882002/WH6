# START
x: int = int(input("enter a number: "))
for i in range(1, x + 1, 2):
    print(f"{"*"*i:^{x}}")
# END
