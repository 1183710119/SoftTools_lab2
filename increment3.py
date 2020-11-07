import datetime
import random
import tkinter as tk
from tkinter import ttk

import pygame

list_formula = []
list_operator = ["+", "-"]
list_wrong = []


def Generate():
    while 1:
        m = random.randint(0, 100)
        n = random.randint(0, 100)
        x = random.choice(list_operator)
        s = str(m) + "  " + x + "  " + str(n)
        if eval(s) < 0:
            s = str(n) + "  " + x + "  " + str(m)
        if s not in list_formula:
            break
    list_formula.append(s)
    return s


def Check(s, y):

    if eval(s) == int(y):
        str_tip.set('回答正确')
        return 1
    else:
        str_tip.set('回答错误 ')
        if s not in list_wrong:
            list_wrong.append(s)
            str_num_wrong.set(str(int(str_num_wrong.get())+1))
        return 0


def Update(s, y):
    i = Check(s, y)
    if i == 1:
        k = int(str_True.get()) + 1
        str_True.set(str(k))
        str_tip.set('上题正确。请回答本题...')
    else:
        k = int(str_False.get()) + 1
        str_False.set(str(k))
        str_tip.set('上题错误。请回答本题...')
    str_question.set(Generate())
    text_answer.delete("0.0", 'end')



def CheckWrongQuestion():
    base2 = tk.Tk()
    base2.title("错题集")
    base2.geometry('800x500')
    lab11 = tk.Listbox(base2)
    lab11.place(x=30, y=30, anchor='nw')
    for s in list_wrong:
        lab11.insert(1,s)
    base2.mainloop()


pygame.mixer.init()
t = pygame.mixer.music.load('play.wav')
i = 1

#############################
def start():
    str_True.set('0')
    str_False.set('0')
    str_num_wrong.set('0')
    list_wrong.clear()

    str_tip.set("请输入...")

    str_endtime.set('')
    str_lasttime.set('')

#########################
def PlaySound():
    global i
    if i == 1:
        str_music.set('开')
        pygame.mixer.music.play()
        i = 0
    else:
        str_music.set('关')
        pygame.mixer.music.stop()
        i = 1



def GetStartTime():
    now_time = datetime.datetime.now().strftime('%T')
    str_starttime.set(now_time)


def GetEndTime():
    now_time = datetime.datetime.now().strftime('%T')
    str_endtime.set(now_time)


def GetTotalTime():
    time1 = datetime.datetime.strptime(str_endtime.get(), '%H:%M:%S')
    time2 = datetime.datetime.strptime(str_starttime.get(), '%H:%M:%S')
    time = (time1 - time2).seconds
    str_lasttime.set(str(time))



base = tk.Tk()
base.title("100以内加减法练习")
base.geometry('850x600')
str_tip = tk.StringVar()
str_tip.set("点击”开始“开始练习...")
text_answer = tk.Text(base, width=10, height=3)
text_answer.place(x=400, y=215, anchor='nw')


str_question = tk.StringVar()
str_True = tk.StringVar()
str_True.set('0')
str_False = tk.StringVar()
str_False.set('0')

str_starttime = tk.StringVar()
str_starttime.set('')
str_endtime = tk.StringVar()
str_endtime.set('')
str_lasttime = tk.StringVar()
str_lasttime.set('')


lable_starttime = tk.Label(base,textvariable=str_starttime, width=15, height=1,bg='white')
lable_starttime.place(x=660, y=230, anchor='nw')
lable_endtime = tk.Label(base,textvariable=str_endtime, width=15, height=1,bg='white')
lable_endtime.place(x=660, y=260, anchor='nw')
lable_lasttime = tk.Label(base,textvariable=str_lasttime, width=15, height=1,bg='white')
lable_lasttime.place(x=660, y=290, anchor='nw')

# ##########################
# 音乐开关提示
str_music = tk.StringVar()
str_music.set('关')
lable_music = tk.Label(base, textvariable = str_music, font=('Arial', 12), bg='green',width=4).place(x=680,y=430,anchor='nw')
# 错题集题数
str_num_wrong = tk.StringVar()
str_num_wrong.set('0')
lable_num_wrong = tk.Label(base, textvariable = str_num_wrong, font=('Arial', 12),bg='green',width=4).place(x=680,y=480,anchor='nw')
# 正确题数
lable_true = tk.Label(base, textvariable = str_True, font=('Arial', 12), bg='green',width=4).place(x=660,y=170,anchor='nw')
lable_true = tk.Label(base, textvariable = str_False, font=('Arial', 12), bg='red',width=4).place(x=660,y=200,anchor='nw')

# ##########################


lab3 = ttk.Label(base, text="=", font=('Arial', 20))
lab3.place(x=355, y=215, anchor='nw')

lab6 = tk.Label(base, text="好好学习，天天向上", font=('Ubuntu', 50), bg='pink',width=27)
lab6.place(x=0, y=50, anchor='nw')

# 装饰
lable_decorate = tk.Label(base, text='',bg='pink',width=250).place(x=0, y=350, anchor='nw')

# 题目 标签
lab9 = tk.Label(base, textvariable=str_question, font=('Arial', 20), bg='yellow',width=12,height=2)
lab9.place(x=140, y=200, anchor='nw')
# 提示 标签
lab10 = tk.Label(base, textvariable=str_tip, font=('Arial', 12), bg='grey',width=25,height=5)
lab10.place(x=330, y=430, anchor='nw')
# 对错 标签
lable_true = tk.Label(base, text='正答题数', font=('Arial', 12)).place(x=580, y=170, anchor='nw')
lable_false = tk.Label(base, text='错答题数', font=('Arial', 12)).place(x=580, y=200, anchor='nw')
# 时间 标签
lab11 = ttk.Label(base, text='开始时间', font=('Arial', 12))
lab11.place(x=580, y=230, anchor='nw')
lab12 = ttk.Label(base, text='结束时间', font=('Arial', 12))
lab12.place(x=580, y=260, anchor='nw')
lab13 = ttk.Label(base, text='总时长', font=('Arial', 12))
lab13.place(x=580, y=290, anchor='nw')
# 按钮
button1 = tk.Button(base, text="开始", command=lambda: [str_question.set(Generate()), GetStartTime(),start()],width=9,height=3).place(
    x=100,y=400,anchor='nw')
button2 = tk.Button(base, text="结束", command=lambda:[GetEndTime(), GetTotalTime()],width=9,height=3).place(x=200,y=400, anchor='nw')
button3 = tk.Button(base, text="检查", command=lambda: Check(str_question.get(), text_answer.get("0.0", "end")), width=9,
                    height=3).place(x=100, y=500,anchor='nw')
button4 = tk.Button(base, text="下一题", command=lambda: Update(str_question.get(), text_answer.get("0.0", "end")),
                    width=9,height=3).place(x=200, y=500,anchor='nw')
button5 = ttk.Button(base, text="错题", command=lambda: CheckWrongQuestion()).place(x=580,y=480,anchor='nw')
button6 = ttk.Button(base, text="音乐", command=lambda: PlaySound()).place(x=580,y=430,anchor='nw')
base.mainloop()
