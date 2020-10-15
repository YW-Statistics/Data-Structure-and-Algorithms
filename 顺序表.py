# Title：Sequence Table
# Time: 2020/10/9
# author: Vincent

size = 8
nums = 0
x = [0 for _ in range(8)]

for i in range(size):
    print(x[i])
    
# 尾端加入
x[nums] = 1
nums += 1

# 非保序添加
a = 0
x[nums] = x[a]
x[a] = 2

# 保序添加
a = 0
for j in range(nums, a-1, -1):
    x[j] = x[j-1]
x[a] = 3