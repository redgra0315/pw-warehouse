# def add(x, y):
#     # print("call {}.{}+{}".format(add.__name__, x, y), file=file)
#     return x + y
#
#
# def add3(x, y, *args, z):
#     return x + y + z


def logger(fn):
    def _logger(*args, **kwargs):
        print("begin")
        x = fn(*args, **kwargs)
        print("end")
        return x

    return _logger  # 返回内层函数的引用


# print(logger(add3, x=20, y=43, z=65))
# print(logger(add)(20, 43))


# add(4, 5)

@logger   #  add1= logger(add1)
def add1(x, y):
    return x + y


print(add1(4, 5))
