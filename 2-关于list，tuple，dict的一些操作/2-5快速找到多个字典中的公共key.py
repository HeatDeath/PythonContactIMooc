from random import randint,sample

#sample随机取样
a=sample('abcdefg',3)
print(a)

b=sample('abcdefg',randint(3,6))
print(b)

s1={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
print(s1)

s2={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
print(s2)

s3={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
print(s3)

res=[]
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

print(res)

#方法二
print(list(s1.keys()&s2.keys()&s3.keys()))


#方法三
from functools import reduce

#print(list(map(dict.keys,[s1,s2,s3])))

print(list(reduce(lambda a,b:a&b,map(dict.keys,[s1,s2,s3]))))