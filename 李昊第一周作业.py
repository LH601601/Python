# 基本数据类型
# 1.int整型
# 2.布尔型bool(Ture(1) False(O))
# 3.字符串str
# 4.浮点型float

# 2.写出标识符的命名规则
"""
命名规则：只能使用字母，数字，下划线，切记不能用数字开头，数字开头会报错
       1.区分大小写，Mysql 不区分大小写， Linux 不区分大小写，ls 和 Ls不一样
       2.用小写字母给变量，对象，函数等命名，类开头需要大写
       3.见名知意，看见名字就要知道内容数据大概情况，例如 name
       4.不要混淆，例如字母o和数字0，字母l和数字1
       5.不要跟系统的关键字冲突，例如： if for while in and
命名写法： 多个单词命名时，可以用下划线连接： 例如 one_two_three,
驼峰命名法： 多个单词命，第一个单词小写，后面单词首字母的大写
     例如：getYouName, fullInLove, 定义类时： FirstPerson
"""
# 3.定义一个学生的信息变量：姓名，性别，年龄，学号，班级，专业，家庭地址，
name = "李昊"
gender = "男"
age = 18
number = 202151050226
stu_class = "智能二班"
major = "人工智能"
home = "河南省南阳市唐河县郭滩镇二郎庙"
print("学生姓名：%s, 性别：%s, 年龄：%s, 学号：%s, 班级：%s, 专业：%s, 家庭地址：%s " % (name, gender, age, number, stu_class, major, home))

# 将上述改为键盘输入每一项信息，然后打印格式化输出
name = input("姓名：")
gender = input("性别：")
age = input("年龄：")
number = input("学号：")
stu_class = input("班级：")
major = input("专业：")
home = input("住址：")

print("姓名：%s" % name,"性别：%s" % gender, "年龄：%s" % age, "学号：%s" % number, "班级：%s" % stu_class,"专业：%s" % major,"地址：%s" % home)
