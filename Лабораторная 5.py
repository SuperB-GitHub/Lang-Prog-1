import csv
import os
import PySimpleGUI as sg
def Zadan1():
    direc=input('Введите путь папки: ')
    files = os.listdir(direc)
    return len(files)

def Zadan2():
    with open('123.csv',encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=',')
        stroka=[]
        for row in reader:
            for row1 in row:
                row1=row1.split(';')
                stroka.append(row1)
        stroka1=[]
        for x in range(1,len(stroka)):
            stry=stroka[x]
            stroka1.append(stry[1])
        stroka1.sort()
        strend=[]
        for i in range(len(stroka1)):
            for y in range(len(stroka)):
                if stroka1[i] in stroka[y]:
                    strend.append(stroka[y])
        return strend

def Zadan3():
    zadan2 = Zadan2()
    def Upd():
        strnach=[]
        for i in range(len(zadan2)):
            zdn2 = zadan2[i]
            zdn2[2] = int(zdn2[2]) + 1
            strnach.append(zdn2)
        return strnach
    
    layout = [  [sg.Text("Строка из 2 задания:")],
                [sg.Text(zadan2)], # type: ignore
                [sg.Button('Добавить 1 ко всем возрастам студентов')],
                [sg.Text("Результат")],
                [sg.Text(key='выход1')]]
    window = sg.Window('Задание 3', layout)  
    while True:
        event, values = window.read() # type: ignore
        if event=='Добавить 1 ко всем возрастам студентов':
            window['выход1'].update(Upd()) # type: ignore
        if event==None:
            break

def Zadan4():
    zadan2 = Zadan2()
    def Upd():
        strnach=[]
        for i in range(len(zadan2)):
            zdn2 = zadan2[i]
            zdn2[2] = int(zdn2[2]) + 1
            strnach.append(zdn2)
        return strnach
    
    def coxp():
        with open('1234.csv','w',encoding='utf-8',newline='') as f:
            writer = csv.writer(f,delimiter=';')
            writer.writerow(['No','ФИО','Возраст','Группа'])
            for i in range(len(upd)):
                writer.writerow(upd[i])


    
    layout = [  [sg.Text("Строка из 2 задания:")],
                [sg.Text(zadan2)], # type: ignore
                [sg.Button('Добавить 1 ко всем возрастам студентов'), sg.Button('Сохранить в документ')],
                [sg.Text("Результат")],
                [sg.Text(key='выход1')],
                [sg.Text(key='выход2')]]
    window = sg.Window('Задание 4', layout)  
    while True:
        event, values = window.read() # type: ignore
        if event=='Добавить 1 ко всем возрастам студентов':
            upd=Upd()
            window['выход1'].update(upd) # type: ignore
            window['выход2'].update('') # type: ignore
        if event=='Сохранить в документ':
            coxp()
            window['выход2'].update('Сохранено в документ') # type: ignore
        if event==None:
            break



u=True
while u==True:
    print('Вариант 1')
    Zadan=(int(input('Введите номер задания:')))
    if Zadan== 1:
        print(Zadan1())
    elif Zadan== 2:
        print(Zadan2())
    elif Zadan== 3:
        print(Zadan3())
    elif Zadan== 4:
        print(Zadan4())
    else:
        u=False