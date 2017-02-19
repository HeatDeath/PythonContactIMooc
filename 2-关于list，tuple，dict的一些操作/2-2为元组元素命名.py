
#为元组中的每个元素命名，提高程序的可读性

#方法一：定义类似于其他语言的枚举类型
student=('Jim',16,'male','jim333@gmial.com')

NAME,AGE,SEX,EMAIL=range(4)

print(student[NAME])

#方法二，使用collections.namedtuple
from collections import namedtuple

Student=namedtuple('StudentMessage',['name','age','sex','email'])

s=Student('Jack',18,'male','Jack999@gamil.com')

print(s)
print(s.name)
print(s.age)
print(s.sex)
print(s.email)

print(isinstance(s,tuple))