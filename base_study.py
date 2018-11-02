# 单行注释，在’#‘后面需要加一个空格，避免黄线警告
"""
多行注释
"""
print("hello python")

"""
算数运算符
// 取整
%  取余
字符串可以使用运算符来使用 例如：”test“ *2 =  ”testtest"
"""

# 变量的使用  变量=值
"""
变量名只有第一次出现的时候才是定义变量
数据类型
str/列表/元组/字典
int/bool/float/complex
bool 非0即true
数字型变量跟字符串型变量 可以通过"+" 跟 "*" 进行算术计算
name = "etest"
print(name)

格式化输出
%s 输出字符串
%d 输出整数
%f 输出浮点型
%% 输出%

变量的命名
规则：flippey_name 
"""
name = "fippey"
print("my name is %s " % name)
price = 9.00
weight = 5
money = price*weight
print("单价 %.2f 重量 %.2f 总价 %.2f" % (price, weight, money))

# 函数
"""
input 函数实现键盘内容的输入
int("x") 字符串x转为int类型
float("y") 字符串y转为float类型

password = input("请输入密码")
print(password)

num: int = int(input("请输入数量"))
price: float = float(input("请输入单价"))
print(num*price)

"""

# 判断语句 if
age = 100
if age > 99:
    print("大于99")
else:
    print("小于99")





