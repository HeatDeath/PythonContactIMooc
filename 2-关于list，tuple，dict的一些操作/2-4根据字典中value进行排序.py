from random import randint

d={x:randint(60,100) for x in 'xyzabcdret'}
print(d)

#sorted()只能对key进行排序

#tuple的比较是先比较第一个元素

print(d.keys())
print(d.values())

#zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple。
print(list(zip(d.values(),d.keys())))
print(sorted(zip(d.values(),d.keys())))


print(d.items())
#以key值作为比较对象
print(sorted(d.items(),key=lambda x:x[1]))
