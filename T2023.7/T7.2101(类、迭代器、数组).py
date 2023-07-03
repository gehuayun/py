"""
递归
"""
print('1111111111111111 递归 11111111111111111111111')


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

"""
lambda函数
"""
print('22222222222222222 lambda函数 22222222222222222222')
x = lambda a, b, c: a + b + c
print(x(6, 7, 2))

"""
class创建对象
"""

print('33333333333333 class创建对象 3333333333333333333')


class MyClass:
    x = 7


p1 = MyClass()
print(p1.x)

"""
        _init_函数
            内置的 __init__() 函数。
            所有类都有一个名为 __init__() 的函数，它始终在启动类时执行。
            使用 __init__() 函数将值赋给对象属性，或者在创建对象时需要执行的其他操作
"""

print('44444444444444444 _init_函数 444444444444444444')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Bill", 63)  # 赋值

print(p1.name)  # 调用 name
print(p1.age)  # 调用 age

"""
创建对象方法
"""
print('55555555555555555555555创建对象方法5555555555555')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Bill", 63)
p1.myfunc()

"""
self参数
"""
print('6666666666666666   self参数  66666666666666666')


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Bill", 63)  # 对象赋值
p1.myfunc()
print(p1.age)
# p1.age = 66       # 修改对象属性
# del p1.age        # 删除对象属性
# print(p1.age)
"""
从元组返回迭代器
            __iter__() 和 __next__() 方法
"""
print('7777777777777777从元组返回迭代器77777777777777777777')
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

"""
从字符返回迭代器
"""
print('888888888888888从字符返回迭代器888888888888888888888888')
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

"""
创建迭代器
            __iter__() 和 __next__() 方法
            正如您在 Python 类/对象 一章中学到的，所有类都有名为 __init__() 的函数，它允许您在创建对象时进行一些初始化。
            __iter__() 方法的作用相似，您可以执行操作（初始化等），但必须始终返回迭代器对象本身。
            __next__() 方法也允许您执行操作，并且必须返回序列中的下一个项目
"""
print('9999999999999999创建迭代器9999999999999999999999')


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

"""
停止迭代器
        __iter__() 和 __next__() 方法
    如果你有足够的 next() 语句，或者在 for 循环中使用，则上面的例子将永远进行下去。
    为了防止迭代永远进行，我们可以使用 StopIteration 语句。
    在 __next__() 方法中，如果迭代完成指定的次数，我们可以添加一个终止条件来引发错误
"""

print('101010101停止迭代器1011010101001')


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

"""
        使用 super() 函数
        Python 还有一个 super() 函数，它会使子类从其父继承所有方法和属性：
"""

print('11111111111使用 super() 函数111111111111111111111')


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Elon", "Musk", 2019)
x.welcome()
