
#一个简单的猜数游戏
from random import randint
from collections import deque

history=deque([],5)
N=randint(0,100)

def guess(k):
    if k==N:
        print('right')
        return True
    if k<N:
        print('%s is less than N' % k)
    else:
        print('%s is more than N' % k)
    return False

while True:
    line=input('input a number:')
    if line.isdigit():#isdigit()方法检测字符串是否只由数字组成。
        k=int(line)
        history.append(k)
        if guess(k):
            break
    elif line=='history' or line == 'h?':
        print(list(history))


#需要一个历史数字，来显示已经尝试过的数字
#使用容量为n的队列来储存历史记录

from collections import deque

q=deque([],5)


'''
#pickle模块似乎有些异常

#pickle可以把python对象存储到文件中

import pickle
p=[23,53,54,32,56,33,22,66,33,22,66]
pickle.dump(p,open('history','w'))
his=pickle.load(open('history'))
print(his)
'''