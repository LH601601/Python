# 定义变量
"""
变量: 在程序运行过程中发生变化的量
    命名规则: 只能用字母, 数字, 下划线, 不能数字开头
    表面理解: 给这个常量起个名字, 或贴上一个标签
    变量实质: 就是在程序运行过程中, 定义的变量会被开辟一块存储空间, 将数据放进去, 可以变量名调用里面的数据使用
    当变量数据值一样的时候, 他们的id地址是相同的.
"""
# = : 赋值符号, 将666赋值给num
# 等号右边叫做值
num = 666
# * : 乘以
num = num * 2
print(num)
name = "李冰冰"
print(name)
mark = 9.96
print(mark, type(mark))
# id(): 带括号的叫函数, 查看变量的内存地址
print(id(num))  # 2164972185008
nm = "李冰冰"
print(id(nm), id(name))
# 选中内容, shift + tab键 往左边移动, tab往右边移动
