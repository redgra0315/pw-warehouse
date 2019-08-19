age = 56
for i in range(5):
    guess_age = int(input("请输入年龄:"))
    if guess_age == age:
        print("恭喜你，采正确了")
        break
    elif guess_age > age:
        print("兄弟你想多了，他没有那么大！")
    else:
        print("你猜小了")
else:
    print("恭喜你,完成")
