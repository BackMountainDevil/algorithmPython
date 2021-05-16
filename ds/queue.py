# -*- encoding: UTF-8 -*-
'''
@File    :  queue.py
@Time    :  2021/05/16 09:27:42
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  队列 - FIFO
'''
from queue import Queue
from collections import deque

q = Queue()
q.put(1)  # 入队列
q.put(3)
q.put(5)
print(q.get())  # 出队列
print(q.get())
print(q.get())
# print(q.get())  # 出队列，此时队列为空会发生阻塞

dq = deque()  # 入队列
dq.append(2)
dq.append(4)
dq.append(6)
print(dq.popleft())  # 出队列
print(dq.popleft())
print(dq.popleft())
# print(dq.popleft())  # 出队列，此时栈为空会引发异常错误
