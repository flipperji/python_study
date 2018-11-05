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

# 高级特性
"""
切片操作符 取list或者tuple部分元素 取L中索引为0,1,2的三个元素
    L=['A','B','C','D','E']  -> L[0：3]=['A','B','C']
    
迭代 for....in
"""

# Http

"""
https://www.jianshu.com/search?q=96%87&page=1&type=note
 url组成
    scheme: 访问协议 http/https/ftp等
    host: 域名 www.baidu.com
    prot：端口号 浏览器默认使用80端口
    path: 查找路径 search
    query-string: 查询字符串 q=96%87&page=1&type=note
    anchor: 锚点 前端页面用来进行定位
浏览器会对url进行编码，除了英文字母，数字和部分符号外，其他全部使用%+十六进制码值进行编码

请求头常见参数
    User_Agent：标记请求来源(浏览器的种类/版本，手机型号等)
    Referer：表示当前这个请求是从哪个url过来的
    Cookie：服务器用cookie来标示两个请求是否来自同一个人
"""

# ProxyHandler处理器(代理设置) demo01.py
"""
http://httpbin.org 方便查看http请求的一些参数
ip代理步骤
    1.调用request.ProxyHandler创建ProxyHandler
    2.调用request.build_opener创建opener
    3.调用opener.open 发送请求
    
    handler = request.ProxyHandler({"http": "115.46.66.241:8123"})
    opener = request.build_opener(handler)
    res = opener.open(url)
print(res.read())
常见的代理 
    西刺代理 www.xicidaili.com
    快代理 www.kuaidaili.com
    代理云 www.dailiyun.com
"""

# Cookie
# requests库
"""
    直接导入requests库   import requests

"""

