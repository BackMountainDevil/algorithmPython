# -*- encoding: UTF-8 -*-
'''
@File    :  hasDuplicate.py
@Time    :  2021/05/15 18:55:44
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  数组中有无重复值的优化方法
'''


def hasDuplicateValue(list):
    """
    参数
        list: 待检查重复的队列
    返回值
        True | False：有重复值就返回 True, 否则返回 False
    效率： O(n^2)
    """
    size = len(list)
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if list[i] == list[j]:
                return True
    return False


def hasDuplicateValue_On(list):
    """
    参数
        list: 待检查重复的队列
    返回值
        True | False：有重复值就返回 True, 否则返回 False
    效率： O(n)
    用集合 set 会更快一点
    """
    tag = {}
    for i in list:
        if (i not in tag):  # 判断元素是否已经被标记
            tag[i] = 1  # 标记新元素
        else:
            return True
    return False


unsort = [4, 2, 1, 7, 3, 4]

print("未排序数列： ", unsort)
print("是否存在重复值： ", hasDuplicateValue(unsort), hasDuplicateValue_On(unsort))
