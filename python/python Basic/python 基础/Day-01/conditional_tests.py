

count = 0
lst = []
while 5 > count:
    # for i in range(1):
    vale_1 = input("Please enter the  1  value:")
    vale_2 = input("Please enter the  2  value:")

    if vale_1.lower() == vale_2:
        lst.append(vale_1)
    elif (vale_1 > vale_2) or (vale_1 <vale_2):
        print("它是老大")
    else:
        print("他最小")
    count += 1
    print(lst)


