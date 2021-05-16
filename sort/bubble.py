# -*- encoding: UTF-8 -*-
'''
@File    :  bubble.py
@Time    :  2021/05/15 16:09:46
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  冒泡排序 - 可将注释去掉查看过程
'''


def sort_bubble(list, ascend=True):
    """
    参数
        list: 待冒泡排序的队列
        ascend： 是否升序排列，默认是（True），否（False）就降序排列
            升降序唯一差别在于是 大于号 还是 小于号
    返回值
        list：经过冒泡排序的队列；需要特别说明的是不需要返回值也是可以的，原队列还是会被修改
    """
    size = len(list)
    if ascend:
        for i in range(0, size - 1):
            for j in range(0, size - 1 - i):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                # print("升序排序中： ", i, j, list)
    else:
        for i in range(0, size - 1):
            for j in range(0, size - 1 - i):
                if list[j] < list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                # print("降序排序中： ", i, j, list)
    return list


unsort = [4, 2, 7, 4, 3, 1]
print("未排序： ", unsort)
sort = sort_bubble(unsort)
print("冒泡排序 - 升序： ", sort, "unsort: ", unsort)
sort = sort_bubble(sort, False)
print("冒泡排序 - 降序： ", sort)
