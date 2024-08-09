import random


def into():
    while True:
        global i1, sum1, cuo1, lng, end, stat
        sum1 += 1
        if r1 > 0:
            i1 = int(input('输入{}到{}之间的数:'.format(lng, end)))
            if i1 <= lng or i1 >= end:
                print('不在范围内')
                cuo1 += 1
                continue
            if r1 == i1:
                return print('游戏结束！！！{}是本轮的随机数,总共执行了{}次循环,{}次输入超过规定范围'.format(i1, sum1, cuo1))
                break
            elif r1 > i1:
                print('写小了')
                lng = i1
            else:
                print('写大了')
                end = i1
            if end - lng == 2 and r1 == i1:
                return print('游戏结束！！！是{}到{}之间的数,{}是本轮的随机数,总共执行了{}次循环,{}次输入超过规定范围'.format(lng, end, i1, sum1, cuo1))
                break
        else:
            i1 = int(input('输入{}到{}之间的数:'.format(stat, lng)))
            if i1 >= lng or i1 <= stat:
                print('不在范围内')
                cuo1 += 1
                continue
            if r1 == i1:
                return print('游戏结束！！！{}是本轮的随机数,总共执行了{}次循环,{}次输入超过规定范围'.format(i1, sum1, cuo1))
                break
            elif r1 > i1:
                print('写小了')
                stat = i1
            else:
                print('写大了')
                lng = i1
            if lng - stat == 2 and r1 == i1:
                return print('游戏结束！！！是{}到{}之间的数,{}是本轮的随机数,总共执行了{}次循环,{}次输入超过规定范围'.format(stat, lng, i1, sum1, cuo1))
                break

# i1 = int(input('输入{}到{}之间的数:'.format(start, end)))

def randomGame():
    global r1
    r1 = random.randint(-100, 100)
    if r1 > 0:
        print('这次猜的是个正数')
        into()
    elif r1 == 0:
        print('这次猜的是零，不用继续了')
    else:
        print('这次猜的是个负数')
        into()


if __name__ == '__main__':
    print('···随机数猜猜猜···')
    stat = -100
    lng = 0
    end = 100
    sum1 = 0
    cuo1 = 0
    randomGame()


def myfunction():
    pass
