# Title: String
# Author: Vincent
# Time: 2020/10/13

# 创建字符串
s = 'abcd'

# 查找字符串中的字符
print('a' in s)
print('x' not in s)

# 根据下标访问字符串中的值
print(s[1:3])
print(s[0])

# 字符串拼接
s1 = 'aaaa'
s2 = 'bbbb'
print(s1+s2)

# 常用的字符串操作
# 求取最值
print(max(s))
print(min(s))

# 分割字符串
s_list = s.split('c')

# 将list中的字符拼接为字符串
print(''.join(s_list))

# 忽略头部空格
s3 = '   aaa'
print(s3.lstrip())

# 忽略末尾空格
s4 = 'aaa   '
print(s4.rstrip())

# 忽略头尾空格
s5 = '   aaa   '
print(s5.strip())

# 转变字符大小写
s6 = 'aaa'
s7 = 'AAA'
print(s6.upper())
print(s7.lower())
