

'''
import numpy as np
import matplotlib.pyplot as plt # 首先载入matplotlib的绘图模块pyplot，并且重命名为plt

x = np.linspace(0, 10, 1000)

y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))   #2 创建绘图对象

plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()

plt.show()

print(11111111111111111)


for idx, color in enumerate("rgbyck"):
    plt.subplot(320+idx+1, facecolor=color)
plt.show()


print(222222222222222)


plt.subplot(221) # 第一行的左图
plt.subplot(222) # 第一行的右图
plt.subplot(212) # 第二整行
plt.show()



print(3333333333333333)


plt.figure(1)  # 创建图表1
plt.figure(2)  # 创建图表2
ax1 = plt.subplot(211)  # 在图表2中创建子图1
ax2 = plt.subplot(212)  # 在图表2中创建子图2

x = np.linspace(0, 3, 100)
for i in range(5):
    plt.figure(1)  # 选择图表1
    plt.plot(x, np.exp(i * x / 3))
    plt.sca(ax1)  # 选择图表2的子图1，将当前轴实例设置为ax
    plt.plot(x, np.sin(i * x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i * x))
plt.show()


print(44444444444444444)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 20, 1)
y1 = x * x
y2 = np.log(x)

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(x, y1, label="$y1 = x * x$", color="r")
ax1.legend(loc=0)
# 设置对应坐标轴的名称
ax1.set_ylabel("y1")
ax1.set_xlabel("Compare y1 and y2")

# 设置x轴刻度的数量
ax = plt.gca()
ax.locator_params("x", nbins=20)

# 添加坐标轴,并在新添加的坐标轴中画y2 = log(x)图像
ax2 = plt.twinx()
ax2.set_ylabel("y2")
ax2.plot(x, y2, label="$y2 = log(x)$")
ax2.legend(loc=0)

plt.show()

print(55555555555555)



#画三维图
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
fig=figure()
ax=Axes3D(fig)
x=np.arange(-4,4,0.1)
y=np.arange(-4,4,0.1)
x,y=np.meshgrid(x,y)
R=np.sqrt(x**2+y**2)
z=np.sin(R)
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap='hot')
show()


print(6666666666666)


#更多简单的图形
x = [1,2,3,4]
y = [5,4,3,2]

plt.figure()
plt.subplot(2,3,1)
plt.plot(x, y)

plt.subplot(232)
plt.bar(x, y)

plt.subplot(233)
plt.barh(x, y)

plt.subplot(234)
plt.bar(x, y)
y1 = [7,8,5,3]
plt.bar(x, y1, bottom=y, color = 'r')

plt.subplot(235)
plt.boxplot(x)

plt.subplot(236)
plt.scatter(x,y)

plt.show()




print(7777777777777)

'''
from __future__ import division

'''
使用pandas画图
pandas中画图的主要类型包括：
累和图
柱状图
散点图
饼图
矩阵散点图
'''

from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
np.random.seed(12345)
from pandas import Series, DataFrame
import pandas as pd
# %matplotlib inline

s = pd.Series([2, np.nan, 5, -1, 0])
print(s)

print(s.cumsum())

#画累和图
ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
ts=ts.cumsum()
ts.plot()
plt.show()
df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=list('ABCD'))

# cumulative意为累计、累积，这个函数可以返回一个累计值，经常会遇到月累计、年累计这种指标，会用这个函数
df=df.cumsum()
df.plot()
plt.show()

'''
#画柱状图
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot(kind='bar') #分开并列线束
df2.plot(kind='bar', stacked=True) #四个在同一个里面显示 百分比的形式
df2.plot(kind='barh', stacked=True)#纵向显示
plt.show()
df4=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000)-1},columns=list('abc'))
df4.plot(kind='hist', alpha=0.5)
df4.plot(kind='hist', stacked=True, bins=20)
df4['a'].plot(kind='hist', orientation='horizontal',cumulative=True) #cumulative是按顺序排序
plt.show()
#Area Plot
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot(kind='area')
df.plot(kind='area',stacked=False)
plt.show()
'''