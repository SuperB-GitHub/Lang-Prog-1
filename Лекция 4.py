from tkinter import *
from math import *

def tk():
    root=Tk()
    root.title('Лекция 4')
    A = Entry(root, width=20)
    B = Entry(root, width=20)
    btn_zad1 = Button(text="Сумма")
    btn_zad2 = Button(text="Разность")
    btn_zad3 = Button(text="Произведение")
    btn_zad4 = Button(text="Деление")
    btn_clear = Button(text="Clear")
    lbl0= Label(text='Введите 1 число')
    lbl01= Label(text='Введите 2 число')
    lbl = Label(bg='white', fg='black', width=40)
    lbl1 = Label(bg='white', fg='black', width=40)

    def zad1(event):
        lbl1['text'] = ''
        x1 = int(A.get())
        y1 = int(B.get())
        lbl['text'] = str(x1+y1)

    def zad2(event):
        lbl1['text'] = ''
        x1 = int(A.get())
        y1 = int(B.get())
        lbl['text'] = str(x1-y1)

    def zad3(event):
        lbl1['text'] = ''
        x1 = int(A.get())
        y1 = int(B.get())
        lbl['text'] = str(x1*y1)

    def zad4(event):
        lbl1['text'] = ''
        x1 = int(A.get())
        y1 = int(B.get())
        lbl['text'] = str(x1/y1)

    def clear(event):
        lbl['text'] = ''
        lbl1['text'] = ''

    
    btn_zad1.bind('<Button-1>', zad1)
    btn_zad2.bind('<Button-1>', zad2)
    btn_zad3.bind('<Button-1>', zad3)
    btn_zad4.bind('<Button-1>', zad4)
    btn_clear.bind('<Button-1>', clear)
    lbl0.pack()
    A.pack()
    lbl01.pack()
    B.pack()
    lbl.pack()
    lbl1.pack()
    btn_zad1.pack()
    btn_zad2.pack()
    btn_zad3.pack()
    btn_zad4.pack()
    btn_clear.pack()

    root.mainloop()

def simple():
    import PySimpleGUI as sg 
    layout = [  [sg.Text("Введите число 1")],
                [sg.Input(key='a')],
                [sg.Text("Введите число 2")],
                [sg.Input(key='b')],
                [sg.Text("Результат")],
                [sg.Button('Сумма'),sg.Button('Разница'),sg.Button('Произведение'),sg.Button('Деление')],
                [sg.Text(size=(5,1), key='выход1'), sg.Text(size=(10,1), key='выход2'),sg.Text(size=(9,1), key='выход3'),sg.Text(size=(5,1), key='выход4')]]
    window = sg.Window('Лекция 4', layout)  
    while True:
        event, values = window.read()
        if event=='Сумма':
            window['выход1'].update(int(values['a']) + int(values['b']))
        if event=='Разница':
            window['выход2'].update(int(values['a']) - int(values['b']))
        if event=='Произведение':
            window['выход3'].update(int(values['a']) * int(values['b']))
        if event=='Деление':
            window['выход4'].update(int(values['a']) / int(values['b']))
        if event==None:
            break
print(simple())
# есть еще wxpython и PyQt5

