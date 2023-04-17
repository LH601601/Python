# 李昊. 3.13日作业
"""
1. 列表是一个有序容器, 里面数据可以重复, 列表使用方括号[], 里面的元素每个用逗号隔开
2. 列表有索引, 索引是从0开始的, 索引是整数递增
3. 正索引,最大的索引是 n-1; 从左向右依次从0开始递增
4. 负索引,第一个元素对应-n; 从右向左依次从-1开始递减
5. 列表命名不要与关键字冲突
6. 列表取值, 可以通过索引取值; 取值方法: 列表名字[索引]
7. 列表切片, 使用索引进行切片, 用法: 列表名[起始位置:终止位置:步长], 起始可以取到值, 终止取不到值, 左闭右开区间; 在步长为正数, 起始值必须小于终止值
8. 两个列表相加, 会有序的将两个列表合成一个, 一个列表乘一个数, 列表不会增加, 里面元素个数是原来的n倍
1. index(value, start, end): 获取元素在列表中首次出现的索引, value要查询索引的元素, start开始查找的索引位置, end结束的位置
2. count(): 查询元素出现的次数, 如果计算的元素不在列表中结果为0
3. sort(reverse=False): 排序, 默认为False升序排列, True降序排列
4.append(): 添加元素, 将元素添加到列表末尾
5.insert(index, 元素): 在列表的指定索引位置插入元素, 索引后边的元素对应的索引 + 1
6.extend(): 合并两个列表, 括号中放入列表, 所有元素有序添加进另一个列表
7.pop(): 默认删除最后一个元素, 可以通过元素索引进行删除
8.remove(): 直接移除元素, 当有多个元素重复时, 移除元素
9.reserve(): 列表倒置
10.clear(): 可以将列表清空, 变成空列表
11.copy(): 复制一个列表, 数据完全一样, 但是内存地址不一样, 不是同一个列表
12.关键字: del:删除列表

"""

# 2.累加
numbers = 0
for i in range(1, 101):
    numbers = numbers + i
    print(numbers)

# 3.累乘
numbers = 1
for i in range(1, 101):
    numbers = numbers * i
    print(numbers)

# 4.打印正三角形
for i in range(1, 6):
    print("*"*i)

# 5.流量计费 1. 每个月49套餐, 10G流量, 超出1G收费1/G元, 超出20G后开始收费2元/G, 超出50G后开始收费5元/G
set_meal = 49
flow = 10
n = int(input("请输入本月流量使用情况"))
if n <= flow:
    print("本月消费49元")
elif 20 >= n > flow:
    n -= flow
    n *= 1
    consume = n + set_meal
    print(consume)
elif 50 >= n > 20:
    n -= 20
    n *= 2
    consume2 = 59 + n
    print(consume2)
elif n > 50:
    n -= 50
    n *= 5
    consume3 = 119 + n
    print(consume3)




