
#-------------list----------------
#-----------筛去list中的负数------------
data=[1,5,-3,6,0,-2,-6,-9,11,27]

res=[]

#------------基本方法---------------
def count(data,res):
    for x in data:
        if x>=0:
            res.append(x)
    print(res)

#--------------filter函数-----------------
from random import randint

data=[randint(-10,10) for x in range(10)]
print(data)

print(list(filter(lambda x:x>=0,data)))


#---------------列表解析-------------------

print([x for x in data if x >= 0])

'''
#####没搞懂timeit的用法 ...
from timeit import timeit as timeit

timeit('list(filter(lambda x:x>=0,data))')
#print(timeit([x for x in data if x >= 0]))
#print(timeit(count(data,res)))

'''
#-----经测试，列表解析运行速度最优-----------




#----------------dict---------------------
#-------筛选出value大于90的key-value组合
StudentData={x:randint(60,100) for x in range(10)}
print(StudentData)

#-------字典解析-----------
print({k:v for k,v in StudentData.items() if v>90 })


#-----------------set-------------------

#------筛选出set中小于0 的数---------
print(data)
s=set(data)
print(s)
print({x for x in s if x>=0})