def _foo():
    print('test')

class  Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    #通过这个方法我们可以以学生对下绑定name和age两个属性 

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def study(self,conrse_name):
        print("%s正在学习%s." % (self.name,conrse_name))
    
    def watch_av(self):
        if self.age < 18:
            print("%s 再看熊出没" % self.name)
        else:
            print("%s 再看新闻" % self.name)

def main():
    sum = Student('罗浩',38)
    sum.study('Python')
    sum.watch_av()

if __name__ == "__main__":
    main()

