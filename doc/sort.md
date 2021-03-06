# 总结

| 排序方式 |    效率 |    代码链接 |
| :----:    | :----:    | :----:    |
| 冒泡排序 |    O(n^2) |    [../sort/bubble.py](../sort/bubble.py) |
| 选择排序 |    O(n^2) |    [../sort/select.py](../sort/select.py) |
| 插入排序 |    O(n^2) |    [../sort/insert.py](../sort/insert.py) |


# 冒泡排序

以 n 个元素的最糟糕情况考虑  
比较次数： (n-1) + (n-2) + ... + 1 = n(n-1)/2
交换次数：最差状况每次比较就交换一次位置 = n(n-1)/2  
最多总共 n(n-1) = n^2 - n 步

# 选择排序

选择排序和冒泡排序都需要双重循环，效率上都是O(n^2)，但是选择排序的交换次数在最糟糕的情况下（每轮最多一次）比同意糟糕的冒泡排序要少，因此通过步数比较的话，选择排序几乎比冒泡排序快一倍。

以 n 个元素的最糟糕情况考虑  
比较次数： (n-1) + (n-2) + ... + 1 = n(n-1)/2
交换次数：最差状况每轮比较就交换一次位置 = n-1
最多总共 n(n+1)/2 + 1 步

在最坏、平均、最好的情况下，都需要 n^2/2 步

# 插入排序

以 n 个元素的最糟糕情况考虑  
比较次数： (n-1) + (n-2) + ... + 1 = n(n-1)/2
平移次数：最差状况完全逆序每次比较就平移一次位置 = n(n-1)/2
移除次数：最差状况每轮比较就有一次 = n-1
插入次数：n-1
最多总共 n^2 + n - 2 步

在最坏、平均、最好的情况下，分别需要 n^2、n^2/2、n 步

# 重复值检测

[../sort/hasDuplicate.py](../sort/hasDuplicate.py)：算法优化的案例 
