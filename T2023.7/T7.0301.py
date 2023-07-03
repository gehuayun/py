# 导入tkinter库
import tkinter

window = tkinter.Tk()
# 设置窗口title
window.title('my window')
# 设置窗口大小
window.geometry('600x600')
# 显示主窗口
window.mainloop()
'''
l0 = tkinter.Label(window,
                   text='This is Label!',  # 标签的文字
                   bg='pink',  # 背景颜色
                   font=('Arial', 6),  # 字体和字体大小
                   width=15, height=2  # 标签长宽
                   )
# 固定窗口位置
l0.pack()

window.mainloop()

'''
# pack布局
l1 = tkinter.Label(window,text='This is Label!',bg='pink',width=15, height=2)
l1.pack(side='bottom')
### place布局
l2 = tkinter.Label(window, text='This is Label2!', justify=tkinter.RIGHT, width=50)
l2.place(x=40, y=50,   # 设置x，y坐标
         width=100, height=30  # 设置长宽
         )

window.mainloop()

