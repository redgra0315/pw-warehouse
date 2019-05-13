class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, conre_name):
        print("%s正在学习中%s." % (self.name, conre_name))

    def watch_av(self):
        if self.age < 18:
            print("%s正在看动画片" % (self.name))
        else:
            print("%s正在看新闻" % (self.name))


def main():
    stu1 = Student('罗浩',43)
    stu1.study("Python程序涉及")
    stu1.watch_av()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_av()


if __name__ == "__main__":
    main()
