# START
sum_temp: int = 0
for _ in range(5):
    temp: int = int(input(" enter temperature: "))
    while not -50 <= temp <= 45:
        print(" invalid temp")
        temp: int = int(input(" enter temperature: "))
    else:
        print("temp registered")
    sum_temp += temp
print(sum_temp / 5)
# END