import tkinter as tk
import random
from tkinter import DISABLED


list_operator = ["+", "-"]


def Generate():
    m = random.randint(0, 100)
    n = random.randint(0, 100)
    x = random.choice(list_operator)
    s = str(m) + x + str(n)
    if eval(s) < 0:
        s = str(n) + x + str(m)
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



base = tk.Tk()
base.title("100以内加减法练习")
base.geometry('1000x600')
str4 = tk.StringVar()
str4.set("请开始答题")
text1 = tk.Text(base, width=10, height=2)
text1.place(x=600, y=200, anchor='nw')
str1 = tk.StringVar()
str2 = tk.StringVar()
str2.set('0')
str3 = tk.StringVar()
str3.set('0')


lab3 = tk.Label(base, text="=", font=('Arial', 12))
lab3.place(x=550, y=200, anchor='nw')
lab6 = tk.Label(base, text="100以内加减法练习", font=('Arial', 12))
lab6.place(x=450, y=50, anchor='nw')
lab9 = tk.Label(base, textvariable=str1, font=('Arial', 12))
lab9.place(x=300, y=200, anchor='nw')
lab9 = tk.Label(base, textvariable=str4, font=('Arial', 12))
lab9.place(x=450, y=300, anchor='nw')
button1 = tk.Button(base, text="开始", command=lambda: str1.set(Generate()), font=('Arial', 12), width=8, height=2).place(
    x=200,
    y=450,
    anchor='nw')
button2 = tk.Button(base, text="结束", command=lambda: base.quit(), font=('Arial', 12), width=8, height=2).place(x=400,
                                                                                                               y=450,
                                                                                                               anchor='nw')
button3 = tk.Button(base, text="检查", command=lambda: Check(str1.get(), text1.get("0.0", "end")),
                    font=('Arial', 12), width=8, height=2).place(x=600, y=450, anchor='nw')
button4 = tk.Button(base, text="下一题", command=lambda: Update(str1.get(), text1.get("0.0", "end")), font=('Arial', 12),
                    width=8, height=2).place(x=800,
                                             y=450,
                                             anchor='nw')
base.mainloop()
