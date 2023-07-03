"""
题目 输出 9*9 乘法口诀表。
程序分析 分行与列考虑，共9行9列，i控制行，j控制列。
"""
print('*****************乘法**********************')
for i in range(1, 10, 1):
    for j in range(1, i + 1):
        print('%d*%d=%2d ' % (i, j, i * j), end='')
    print()

for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print('%d*%d=%2d ' % (i, j, i * j), end='')
    print()
"""
除法
"""
print('*******************除法********************')
for i in range(1, 10, 1):
    for j in range(1, i + 1):
        print('%d/%d=%2d ' % (i * j, i, j), end='')
    print()

for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print('%d/%d=%2d ' % (i * j, i, j), end='')
    print()
"""
加法
"""
print('****************加法***********************')
for i in range(1, 10, 1):
    for j in range(1, i + 1):
        print('%d+%d=%2d ' % (i, j, i+j), end='')
    print()

for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print('%d+%d=%2d ' % (i, j, i+j), end='')
    print()
"""
减法
"""
print('***********************减法***********************')
for i in range(1, 10, 1):
    for j in range(1, i + 1):
        print('%d-%d=%2d ' % (i, j, i-j), end='')
    print()

for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print('%d-%d=%2d ' % (i, j, i-j), end='')
    print()

