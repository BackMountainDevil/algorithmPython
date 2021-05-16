# -*- encoding: UTF-8 -*-
'''
@File    :  stack_lq.py
@Time    :  2021/05/16 09:15:22
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  栈 - FILO
'''
from queue import LifoQueue
from collections import deque

stack_lq = LifoQueue()  # 支持并发的栈

stack_lq.put(1)  # 入栈
stack_lq.put(3)
stack_lq.put(5)

print(stack_lq.get())  # 出栈
print(stack_lq.get())  # 出栈
print(stack_lq.get())  # 出栈
# print(stack_lq.get())  # 出栈，此时栈为空会发生阻塞

stack_dq = deque()  # 双端队列用作单线程栈
stack_dq.append(2)  # 入栈
stack_dq.append(4)
stack_dq.append(6)
print(stack_dq.pop())  # 出栈
print(stack_dq.pop())
print(stack_dq.pop())
# print(stack_dq.pop())   # 出栈，此时栈为空会引发异常错误
