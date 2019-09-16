# -*- coding:UTF-8 -*-

# 三种格式化拼接

name = input("name:")

age = input("age:")

job = input("job:")

salary = input("salary:")

info2 = '''
----  info of %s ----
Name: %s
Age: %s
Job: %s
Salary: %s
''' % (name, name, age, job, salary)

info3 = '''
----  info of {name} ----
Name: {name}
Age: {age}
Job:  {job}
Salary: {salary}
'''.format(name=name, age=age, job=job, salary=salary)


info = '''
----  info of {0} ----
Name: {0}
Age: {1}
Job:  {2}
Salary: {3}
'''.format(name, age, job, salary)
print(info)
