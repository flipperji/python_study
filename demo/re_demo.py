import re


#text = "hello"
# match 匹配某个字符串
#re_text = re.match('hel', text)
# .匹配任意字符，但是不能匹配换行符'\n'
# \d 匹配任意数字开头 (0,9)
#text = "1hell1"
# '\D'匹配任意非数字
# '\s'匹配空白字符（\n,\t,\r,空格）
# '\w'匹配 a-z和'A-Z',0-9和下划线  '\W'与之相反

# []组合方式 满足中括号中的字符都可以匹配字符
#text = "0522-34355446dasff"
# 匹配多个字符
"""
    *   匹配0个或者任意多个字符
    text = "05235-2344324"
    re.match('\d*', text).group() = 05235
    +   匹配一个或多个字符
    text = "05235-2344324"
    re.match('\d+', text).group() = 05235
    ?   匹配0个或者一个
    text = "05235-2344324"
    re.match('\d?', text).group() = 0
    {m} 匹配m个字符
    {m,n}   匹配m-n个字符
"""
text = "ab31cd"
re_text = re.match('\w{4}', text)
print(re_text.group())
# ----------------------------------正则小案例--------------------------------------------
# 1.1 验证手机号 1开头 第二位可以是34587 ，后面9位随意
phone = "145553553123131"
re_phone = re.match('1[34587]\d{9}', phone)
print(re_phone.group())
# 1.2 验证邮箱
email = "rretae@gmail.com"
# ‘+’表示匹配多个字符
re_email = re.match('\w+@[a-z0-9]+\.[a-z]+', email)
print(re_email.group())
# 1.3 验证url 规则：前面是http或https或ftp，然后加冒号，加斜杠，后面任意非空白字符
url = "http://www.baidu.com"
re_url = re.match('(http|https|ftp)://[^\s]+',url)
print(re_url.group())

"""
^(脱字号)  在[]表示取反，其他表示开始位置
$   表示以...结尾
|   匹配多个字符
"""

tt = '1241412'
re_tt = re.match('\d', tt)
print(re_tt.group())