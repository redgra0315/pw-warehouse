#import getpass

# username = input('you username:')
# password = getpass.getpass('your passwd:')

# if username == 'test' and password == '123123':
#     print("欢迎登陆！")
# else:
#     print("输入有误！")

age = 56
guess_age = int(input("请输入年龄:"))

if guess_age == age:
    print("恭喜你，猜正确了")
elif guess_age > age:
    print("兄弟你想多了，他没有那么大！")
else:
    print("你猜小了")
