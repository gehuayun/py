"""
实例017：字符串构成
题目 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析 利用 while 或 for 语句,条件为输入的字符不为 ‘\n’。
"""


def name_float():
    global i

    string = input("输入字符串：")
    alp = 0
    num = 0
    spa = 0
    oth = 0
    for i in range(len(string)):
        if string[i].isspace():
            spa += 1
        elif string[i].isdigit():
            num += 1
        elif string[i].isalpha():
            alp += 1
        else:
            oth += 1
    print('space: ', spa)
    print('digit: ', num)
    print('alpha: ', alp)
    print('other: ', oth)


# name_float()

"""
    实例019：完数
    题目 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
    程序分析 将每一对因子加进集合，在这个过程中已经自动去重。最后的结果要求不计算其本身。
"""


# ONE
def name_wan1():
    global i
    c_ = []
    for i in range(2, 1000):
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += j
            if c == i and j == (i - 1):
                c_.append(i)
    print(c_)


# TWO
def name_wan2():
    global i

    def factor(num):
        target = int(num)
        res = set()
        for i in range(1, num):
            if num % i == 0:
                res.add(i)
                res.add(num / i)
        return res

    for i in range(2, 1001):
        if i == sum(factor(i)) - i:
            print(i)


# name_wan1()
# name_wan2()

"""
实例024：斐波那契数列II
题目 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。
程序分析 就是斐波那契数列的后一项除以前一项。
"""


def name_he1():
    global a, b, s_, i
    a = 1
    b = 2
    s_ = 0
    for i in range(20):
        s_ += b / a
        a, b = b, (a + b)
    print(s_)


def name_he2():
    global i, a, b, s_
    i = 0
    a = 1
    b = 2
    s_ = 0
    while True:
        i += 1
        s_ += b / a
        a, b = b, (a + b)
        if i == 20:
            print(s_)
            break


# name_he1()
# name_he2()

"""
实例025：阶乘求和
题目 求1+2!+3!+…+20!的和。
程序分析 1+2!+3!+…+20!=1+2(1+3(1+4(…20(1))))
"""


def name_jc1():
    global i
    res = 1
    for i in range(20, 1, -1):
        res = i * res + 1
    print(res)


def name_jc2():
    global i, a, b
    a_ = 0
    for i in range(1, 21):
        a = 1
        b = 1
        while True:
            b *= a
            if a == i:
                break
            else:
                a += 1
        a_ += b
    print(a_)


# name_jc1()
# name_jc2()


"""
实例026：递归求阶乘
题目 利用递归方法求5!。
程序分析 递归调用即可。
"""


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


# print(factorial(5))


"""
实例027：递归输出
题目 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
程序分析 递归真是蠢方法。
"""


def rec(string):
    if len(string) != 1:
        rec(string[1:])
    print(string[0], end='')


# rec(input('string here:'))
