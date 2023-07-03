"""
实例061：杨辉三角
题目 打印出杨辉三角形前十行。
"""


def generate(numRows):
    r = [[1]]
    for i in range(1, numRows):
        r.append(list(map(lambda x, y: x + y, [0] + r[-1], r[-1] + [0])))
    return r[:numRows]


# a = generate(10)
# for i in a:
#     print(i)

"""
实例076：做函数
题目 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+…+1/n,当输入n为奇数时，调用函数1/1+1/3+…+1/n
"""


def peven(n):
    i = 0
    s = 0.0
    for i in range(2, n + 1, 2):
        s += 1.0 / i
    return s


def podd(n):
    s = 0.0
    for i in range(1, n + 1, 2):
        s += 1.0 / i
    return s


def dcall(fp, n):
    s = fp(n)
    return s


if __name__ == '__main__':
    n = int(input('input a number: '))
    if n % 2 == 0:
        sum = dcall(peven, n)
    else:
        sum = dcall(podd, n)
    print(sum)

s1 = int(input('输入数字为整数：'))
s_ = 0
if s1 % 2 == 0:
    for i in range(0, s1, 2):
        s_ += 1 / (i + 2)
else:
    for i in range(0, s1, 2):
        s_ += 1 / (i + 1)

print(s_)


def name_s():
    global s1, s_, i
    s1 = int(input('输入数字为整数：'))
    s_ = 0
    for i in range(0, s1, 2):
        if s1 % 2 == 0:
            s_ += 1 / (i + 2)
        else:
            s_ += 1 / (i + 1)
    print(s_)


name_s()

