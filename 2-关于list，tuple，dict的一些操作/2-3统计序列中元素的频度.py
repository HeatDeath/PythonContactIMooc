from random import randint

data=[randint(0,20) for x in range(30)]
print(data)

#dict.fromkeys()函数用于创建一个新字典，
#以序列seq中元素做字典的键，value为字典所有键对应的初始值。
#dict.fromkeys(seq[, value]))
#seq -- 字典键值列表。
#value -- 可选参数, 设置键序列（seq）的值。
#该方法返回列表。

c=dict.fromkeys(data,0)

#方法一
for x in data:
    c[x]+=1
print(c)
#筛选出出现次数大于等于2的k-v
print({k:v for k,v in c.items() if v>=2})



#方法二
from collections import Counter
c2=Counter(data)
print(c2)

print(c2.most_common(3))



import re
#打开article.txt，并读取
txt = open('2-3article.txt','r').read()
print(txt)
#将txt以非字符的内容进行分割，返回一个包含了article.txt中所有单词的list
print(re.split('\W+',txt))
c3=Counter(re.split('\W+',txt))
print(c3)
#选取出现次数前五的 单词 及其 出现次数
print(c3.most_common(5))
#将结果放在dict中
print({k:v for k,v in c3.most_common(5)})

print(c3.most_common())
c4={k:v for k,v in c3.most_common()}
print(c4)
print(c4['the'])