# print(1 + 1)
# print(33 + 66 * 6 + 55 - 6 ** 4 + 100000 / 50)
# print(100 // 3)  # 取商
# print(10 % 3)  # 取余数
# print(14 << 1)  # 二进制为1110，向左移动一位为11100，十进制为28
# print(18 >> 3)  # 二进制为10100，向右移动三位为10，十进制为2
# print(15 & 10)  # 按位与，二进制为1111&1010，选取相同部分为1010
# print(17 | 10)  # 按位或，二进制为10001|1010，合并不相同部分为11011
# print(14 ^ 11)  # 按位异或，二进制为1110^1011,选取区不相同部分为1,为101
# print(~14)  # 按位取反，-（x+1）的值
# a = 11
# a *= 2
# print(a)
# def test_Cn(n):  # 计算任意大于0的自然数的和
#     cn = 0
#     cn = int((n + 1) * n / 2)
#     print(cn)
def random1():
    import random
    a = random.randint(-100, 100)
    if a > 0:
        print(a)
        print("hello world")
    elif a == 0:
        print("hello world")
        print("hello world")
        print("hello world")
    else:
        print(a)
        print("No test")
    return a


b = 0
while True:
    random1()
    global a
    if a >= 0:
        b += 1
        random1()
    else:
        break
    if b > 5:
        break
