vsego = int(input("введите всего монет: "))
orel = 0
reshka = 0
for i in range(vsego):
    x = int(input())
    if(x == 0):
        orel += 1
    else:
        reshka+=1
    if(orel > reshka):
        print(reshka)
else:
    print(orel)
