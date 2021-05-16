# -*- encoding: UTF-8 -*-
'''
@File    :  select.py
@Time    :  2021/05/15 16:47:43
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  选择排序 - 可将注释去掉查看过程
'''


def sort_select(list):
    """
    参数
        list: 待排序的队列
    返回值
        list：经过选择排序的队列，默认升序排列，降序排列将小于号改为大于号即可
    """
    size = len(list)
    for i in range(0, size - 1):
        minindex = i
        for j in range(i + 1, size):
            if list[j] < list[minindex]:
                minindex = j
        if not minindex == i:
            list[i], list[minindex] = list[minindex], list[i]
            # print("选择排序中： ", list)
    return list


unsort = [4, 2, 7, 4, 3, 1]
unsort.sort()
print("未排序： ", unsort)
sort = sort_select(unsort)
print("选择排序： ", sort)
