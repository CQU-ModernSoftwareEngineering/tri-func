import tkinter as tk
import tkinter.messagebox
import re
from functions import *

root = tk.Tk()
root.minsize(342, 388)  # 窗口大小300*400
root.resizable(0, 0)
root.config(background='#226767')
root.title('Calculator')
pixelVirtual = tk.PhotoImage(width=1, height=1)

# 第一行
btn_sin = tkinter.Button(root,
                         text="sin",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='sin': buttonClick1(x)
                         )
btn_sin.place(x=9, y=87, width=75, height=50)
btn_cos = tkinter.Button(root,
                         text="cos",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='cos': buttonClick1(x)
                         )
btn_cos.place(x=92, y=87, width=75, height=50)
btn_arctan = tkinter.Button(root,
                            text="arctan",
                            font=('Arial', 12),
                            bg=('#E1E1E1'),
                            fg=('#000000'),
                            bd=0.5,
                            image=pixelVirtual,
                            width=75,
                            height=50,
                            compound="c",
                            command=lambda x='arctan': buttonClick1(x)
                            )
btn_arctan.place(x=175, y=87, width=75, height=50)
btn_arcsin = tkinter.Button(root,
                            text="arcsin",
                            font=('Arial', 12),
                            bg=('#E1E1E1'),
                            fg=('#000000'),
                            bd=0.5,
                            image=pixelVirtual,
                            width=75,
                            height=50,
                            compound="c",
                            command=lambda x='arcsine': buttonClick1(x)
                            )
btn_arcsin.place(x=258, y=87, width=75, height=50)

# 第二行
btn_7 = tkinter.Button(root,
                       text="7",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='7': buttonClick1(x)
                       )
btn_7.place(x=9, y=144, width=75, height=50)
btn_8 = tkinter.Button(root,
                       text="8",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='8': buttonClick1(x)
                       )
btn_8.place(x=92, y=144, width=75, height=50)
btn_9 = tkinter.Button(root,
                       text="9",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='9': buttonClick1(x)
                       )
btn_9.place(x=175, y=144, width=75, height=50)
btn_C = tkinter.Button(root,
                       text="C",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='C': buttonClick1(x)
                       )
btn_C.place(x=258, y=144, width=75, height=50)

# 第三行
btn_4 = tkinter.Button(root,
                       text="4",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='4': buttonClick1(x)
                       )
btn_4.place(x=9, y=201, width=75, height=50)
btn_5 = tkinter.Button(root,
                       text="5",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='5': buttonClick1(x)
                       )
btn_5.place(x=92, y=201, width=75, height=50)
btn_6 = tkinter.Button(root,
                       text="6",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='6': buttonClick1(x)
                       )
btn_6.place(x=175, y=201, width=75, height=50)
btn_rad = tkinter.Button(root,
                         text="R/°",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='rad': buttonClick1(x)
                         )
btn_rad.place(x=258, y=201, width=75, height=50)

# 第四行
btn_1 = tkinter.Button(root,
                       text="1",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='1': buttonClick1(x)
                       )
btn_1.place(x=9, y=258, width=75, height=50)
btn_2 = tkinter.Button(root,
                       text="2",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='2': buttonClick1(x)
                       )
btn_2.place(x=92, y=258, width=75, height=50)
btn_3 = tkinter.Button(root,
                       text="3",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='3': buttonClick1(x)
                       )
btn_3.place(x=175, y=258, width=75, height=50)
btn_del = tkinter.Button(root,
                         text="del",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='del': buttonClick1(x)
                         )
btn_del.place(x=258, y=258, width=75, height=50)

# 第五行
btn_sign = tkinter.Button(root,
                          text="+/-",
                          font=('Arial', 12),
                          bg=('#E1E1E1'),
                          fg=('#000000'),
                          bd=0.5,
                          image=pixelVirtual,
                          width=75,
                          height=50,
                          compound="c",
                          command=lambda x='sign': buttonClick1(x)
                          )
btn_sign.place(x=9, y=315, width=75, height=50)
btn_0 = tkinter.Button(root,
                       text="0",
                       font=('Arial', 12),
                       bg=('#E1E1E1'),
                       fg=('#000000'),
                       bd=0.5,
                       image=pixelVirtual,
                       width=75,
                       height=50,
                       compound="c",
                       command=lambda x='0': buttonClick1(x)
                       )
btn_0.place(x=92, y=315, width=75, height=50)
btn_dot = tkinter.Button(root,
                         text=".",
                         font=('Arial', 12),
                         bg=('#E1E1E1'),
                         fg=('#000000'),
                         bd=0.5,
                         image=pixelVirtual,
                         width=75,
                         height=50,
                         compound="c",
                         command=lambda x='.': buttonClick1(x)
                         )
btn_dot.place(x=175, y=315, width=75, height=50)
btn_equal = tkinter.Button(root,
                           text="=",
                           font=('Arial', 12),
                           bg=('#E1E1E1'),
                           fg=('#000000'),
                           bd=0.5,
                           image=pixelVirtual,
                           width=75,
                           height=50,
                           compound="c",
                           command=lambda x='=': buttonClick1(x)
                           )
btn_equal.place(x=258, y=315, width=75, height=50)

contentVar = tkinter.StringVar(root, '')
contentEntry = tkinter.Entry(
    root, textvariable=contentVar, state='readonly', font=("Arial", 12))
contentEntry.place(x=9, y=10, width=324, height=70)

rad_flag = True
sign_flag = True


def buttonClick1(btn):
    global rad_flag, sign_flag
    content = contentVar.get()
    if content.startswith('.'):  # 小数点前加0
        content = '0' + content
    if btn in '0123456789':
        content += btn
    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            tk.messagebox.showerror('错误', 'Input Error')
            return
        else:
            content += btn
    elif btn == 'del':
        content = ''
    elif btn == '=':
        try:
            strsin = r'sin\-?\d+(\.\d+)?'
            if 'sin' in content:
                m = re.search(strsin, content)

                if m is not None:
                    exchange = m.group()

                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(sin_t(float(value), rad_flag))
                        content = value
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(sin_t(float(value), rad_flag))
                        content = value
                    rad_flag = True
            strcos = r'cos\-?\d+(\.\d+)?'
            if 'cos' in content:
                m = re.search(strcos, content)
                if m is not None:
                    exchange = m.group()
                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(cos_t(float(value), rad_flag))
                        content = value
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(cos_t(float(value), rad_flag))
                        content = value
                    rad_flag = True
            strarcsine = r'arcsine\-?\d+(\.\d+)?'
            if 'arcsine' in content:
                m = re.search(strarcsine, content)
                if m is not None:
                    exchange = m.group()
                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(arcsine_t(float(value), flag=False))
                        content = value + "°"
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(arcsine_t(float(value), flag=False))
                        content = value + "°"
                rad_flag = True
            strarctan = r'arctan\-?\d+(\.\d+)?'
            if 'arctan' in content:
                m = re.search(strarctan, content)
                if m is not None:
                    exchange = m.group()

                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(arctan_t(float(value), flag=False))
                        content = value + "°"
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(arctan_t(float(value), flag=False))
                        content = value + "°"
                rad_flag = True

        except ZeroDivisionError:
            tk.messagebox.showerror('错误', 'VALUE ERROR')
            return
    elif btn in operators:
        if content.endswith(operators):
            tk.messagebox.showerror('错误', 'FORMAT ERROR')
            return
        content += btn
    elif btn == 'rad':
        if 'arc' not in content:
            if '°' in content:
                content = content.replace('°', '')
                rad_flag = not rad_flag
                # print("1{}".format(rad_flag))
            else:
                content += '°'
                rad_flag = not rad_flag


    elif btn == 'sin':
        content += 'sin'
    elif btn == 'cos':
        content += 'cos'
    elif btn == 'arcsine':
        content += 'arcsine'
    elif btn == 'arctan':
        content += 'arctan'
    elif btn == 'C':  # 如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
        content = content[0:-1]
    elif btn == 'sign':
        if '-' in content:
            content = content.replace('-', '')
            rad_flag = not sign_flag
        else:
            if "cos" in content:
                content = content[:3] + '-' + content[3:]
            if 'arctan' in content:
                content = content[:6] + '-' + content[6:]
            if 'arcsine' in content:
                content = content[:7] + '-' + content[7:]
            else:
                content = content[:3] + '-' + content[3:]
            sign_flag = not sign_flag

    contentVar.set(content)


operators = ('=', '.')
root.mainloop()
