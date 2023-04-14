x = int(input())  #1 задуманное число
y = int(input())  #2 задуманное число
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)