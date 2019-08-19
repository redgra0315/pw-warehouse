count = 0
age = 56
# guess_age = int(input("请输入年龄:"))
while count < 3:
    guess_age = int(input("请输入年龄:"))
    if guess_age == age:
        print("恭喜你，采正确了")
        break
    elif guess_age > age:
        print("兄弟你想多了，他没有那么大！")
    else:
        print("你猜小了")
    count += 1
    if count == 3:
        continue_firam = input("是否要继续玩")
        if continue_firam != 'n':
            count = 0
# else:
#     print("恭喜你")
# age = 56
# guess_age = int(input("请输入年龄:"))

# if guess_age == age:
#     print("恭喜你，采正确了")
# elif guess_age > age:
#     print("兄弟你想多了，他没有那么大！")
# else:
#     print("你猜小了")
