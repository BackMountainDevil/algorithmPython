# -*- encoding: UTF-8 -*-
'''
@File    :  insert.py
@Time    :  2021/05/15 20:17:35
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  插入排序 - 可将注释去掉查看过程
'''


def sort_insert(list):
    """
    参数
        list: 待排序的队列
    返回值
        list：经过排序的队列，默认升序排列，降序排列将大于号改为小于号即可
    """
    for i in range(1, len(list)):
        pos = i
        tmp = list[i]

        while pos > 0 and list[pos - 1] > tmp:
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos] = tmp
        # print("选择排序中： ", list)
    return list


unsort = [4, 2, 7, 4, 3, 1]
print("未排序： ", unsort)
sort = sort_insert(unsort)
print("插入排序： ", sort)
