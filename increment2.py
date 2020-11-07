import tkinter as tk
import random
from tkinter import DISABLED
import datetime

list_formula = []
list_operator = ["+", "-"]


def Generate():
    while 1:
        m = random.randint(0, 100)
        n = random.randint(0, 100)
        x = random.choice(list_operator)
        s = str(m) + x + str(n)
        if eval(s) < 0:
            s = str(n) + x + str(m)
        if s not in list_formula:
            break
    list_formula.append(s)
    return s


def Check(s, y):
    if eval(s) == int(y):
        str4.set('回答正确')
        return 1
    else:
        str4.set('回答错误 ')
        return 0


def Update(s, y):
    i = Check(s, y)
    if i == 1:
        k = int(str2.get()) + 1
        str2.set(str(k))
    else:
        k = int(str3.get()) + 1
        str3.set(str(k))
    str1.set(Generate())
    str4.set('请答题')
    text1.delete("0.0", 'end')


def GetStartTime():
    now_time = datetime.datetime.now().strftime('%T')
    if str(text2.get("0.0", "end")).isspace():
        text2.insert('end', now_time)


def GetEndTime():
    now_time = datetime.datetime.now().strftime('%T')
    if str(text3.get("0.0", "end")).isspace():
        text3.insert('end', now_time)


def GetTotalTime():
    print(text3.get("0.0", "end"))
    print(len(text3.get("0.0", "end")))
    time1 = datetime.datetime.strptime(text3.get("0.0", "end")[:8], '%H:%M:%S')
    time2 = datetime.datetime.strptime(text2.get("0.0", "end")[:8], '%H:%M:%S')
    time = (time1 - time2).seconds
    if str(text4.get("0.0", "end")).isspace():
        text4.insert('end', str(time)+'秒')
    else:
        text4.delete("0.0", 'end')
        text4.insert('end', str(time)+'秒')


base = tk.Tk()
base.title("100以内加减法练习")
base.geometry('1000x600')
str4 = tk.StringVar()
str4.set("请开始答题")
text1 = tk.Text(base, width=10, height=2)
text1.place(x=600, y=200, anchor='nw')
text2 = tk.Text(base, width=15, height=1)
text2.place(x=860, y=200, anchor='nw')
text3 = tk.Text(base, width=15, height=1)
text3.place(x=860, y=230, anchor='nw')
text4 = tk.Text(base, width=15, height=1)
text4.place(x=860, y=260, anchor='nw')
str1 = tk.StringVar()
str2 = tk.StringVar()
str2.set('0')
str3 = tk.StringVar()
str3.set('0')

lab1 = tk.Label(base, text="答对", font=('Arial', 12))
lab1.place(x=250, y=302, anchor='nw')
lab2 = tk.Label(base, text="答错", font=('Arial', 12))
lab2.place(x=550, y=302, anchor='nw')
lab3 = tk.Label(base, text="=", font=('Arial', 12))
lab3.place(x=550, y=200, anchor='nw')
lab4 = tk.Label(base, text="题", font=('Arial', 12))
lab4.place(x=400, y=302, anchor='nw')
lab5 = tk.Label(base, text="题", font=('Arial', 12))
lab5.place(x=700, y=302, anchor='nw')
lab6 = tk.Label(base, text="100以内加减法练习", font=('Arial', 12))
lab6.place(x=450, y=50, anchor='nw')
lab7 = tk.Label(base, textvariable=str2, font=('Arial', 12))
lab7.place(x=325, y=300, anchor='nw')
lab8 = tk.Label(base, textvariable=str3, font=('Arial', 12))
lab8.place(x=625, y=300, anchor='nw')
lab9 = tk.Label(base, textvariable=str1, font=('Arial', 12))
lab9.place(x=300, y=200, anchor='nw')
lab10 = tk.Label(base, textvariable=str4, font=('Arial', 12))
lab10.place(x=450, y=400, anchor='nw')
lab11 = tk.Label(base, text='开始时间', font=('Arial', 12))
lab11.place(x=780, y=200, anchor='nw')
lab12 = tk.Label(base, text='结束时间', font=('Arial', 12))
lab12.place(x=780, y=230, anchor='nw')
lab13 = tk.Label(base, text='总时长', font=('Arial', 12))
lab13.place(x=780, y=260, anchor='nw')
button1 = tk.Button(base, text="开始", command=lambda: [str1.set(Generate()), GetStartTime()], font=('Arial', 12),
                    width=8, height=2).place(
    x=200,
    y=450,
    anchor='nw')
button2 = tk.Button(base, text="结束", command=lambda: [GetEndTime(), GetTotalTime()], font=('Arial', 12), width=8,
                    height=2).place(x=400,
                                    y=450,
                                    anchor='nw')
button3 = tk.Button(base, text="检查", command=lambda: Check(str1.get(), text1.get("0.0", "end")),
                    font=('Arial', 12), width=8, height=2).place(x=600, y=450, anchor='nw')
button4 = tk.Button(base, text="下一题", command=lambda: Update(str1.get(), text1.get("0.0", "end")), font=('Arial', 12),
                    width=8, height=2).place(x=800,
                                             y=450,
                                             anchor='nw')
# button6 = tk.Button(base, text="开始计时", command=lambda: GetStartTime(), font=('Arial', 7),
#                     width=8, height=1).place(x=800,
#                                              y=200,
#                                              anchor='nw')
# button6 = tk.Button(base, text="结束计时", command=lambda: GetEndTime(), font=('Arial', 7),
#                     width=8, height=1).place(x=800,
#                                              y=230,
#                                              anchor='nw')
base.mainloop()
