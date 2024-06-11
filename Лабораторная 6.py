import csv
import os
import random
import PySimpleGUI as sg
import numpy as np
from prettytable import PrettyTable
def Menu1():
    layout = [  [sg.Text("Выберите лабораторную работу")],
                [sg.Button('Лаба 1'),sg.Button('Лаба 2'),sg.Button('Лаба 3')],
                [sg.Button('Лаба 4'),sg.Button('Лаба 5'),sg.Button('Лаба 6')],
                [sg.Button('Лаба 7'),sg.Button('Лаба 8'),sg.Button('Лаба 9')],
                [sg.Button('Лаба 10'),sg.Button('Лаба 11'),sg.Button('Лаба 12')],
                [sg.Button('Бонусная лаба 1'),sg.Button('Бонусная лаба 2')]]
    window = sg.Window('Выбор лаб. работы', layout,size=(400,200),element_justification="center")  
    while True:
            event, values = window.read() # type: ignore
            if event=='Лаба 1':
                window.close()
                Laba1()
            if event=='Лаба 2':
                window.close()
                Laba2()
            if event=='Лаба 3':
                window.close()
                Laba3()
            if event=='Лаба 4':
                window.close()
                Laba4()
            if event=='Лаба 5':
                window.close()
                Laba5()
            if event=='Лаба 6':
                sg.popup('''Это и есть 6 лаба, т.е. 
сбор всех лаб в графический редактор''', title='Лаб. работа №6')
            if event=='Лаба 7':
                window.close()
                Laba7()
            if event=='Лаба 8':
                window.close()
                Laba8()
            if event=='Лаба 9':
                window.close()
                Laba9()
            if event=='Лаба 10':
                window.close()
                Laba10()
            if event=='Лаба 11':
                window.close()
                Laba11()
            if event=='Лаба 12':
                window.close()
                Laba12()
            if event=='Бонусная лаба 1':
                window.close()
                Laba13()
            if event=='Бонусная лаба 2':
                window.close()
                Laba14()
            if event==None:
                break

def Laba1():
    layout = [  [sg.Text("Выберите задание ")],
                [sg.Button('Задание 1'),sg.Button('Задание 3')],
                [sg.Button('Задание 2'),sg.Button('Задание 4')],
                [sg.Button('Вернуться в меню')]]
    window = sg.Window('Лаб. работа №1', layout,size=(300,150),element_justification="center")
    while True:
            event, values = window.read() # type: ignore
            if event=='Задание 1':
                window.close()
                Laba1Zadan1()
            if event=='Задание 2':
                window.close()
                Laba1Zadan2()
            if event=='Задание 3':
                window.close()
                Laba1Zadan3()
            if event=='Задание 4':
                window.close()
                Laba1Zadan4()
            if event=='Вернуться в меню':
                window.close()
                Menu1()
            if event==None:
                break

def Laba2():
    layout = [  [sg.Text("Выберите задание ")],
                [sg.Button('Задание 1'),sg.Button('Задание 3')],
                [sg.Button('Задание 2'),sg.Button('Задание 4')],
                [sg.Button('Вернуться в меню')]]
    window = sg.Window('Лаб. работа №2', layout,size=(300,150),element_justification="center")
    while True:
            event, values = window.read() # type: ignore
            if event=='Задание 1':
                window.close()
                Laba2Zadan1()
            if event=='Задание 2':
                window.close()
                Laba2Zadan2()
            if event=='Задание 3':
                window.close()
                Laba2Zadan3()
            if event=='Задание 4':
                window.close()
                Laba2Zadan4()
            if event=='Вернуться в меню':
                window.close()
                Menu1()
            if event==None:
                break

def Laba3():
    layout = [  [sg.Text("Выберите задание ")],
                [sg.Button('Задание 1'),sg.Button('Задание 3')],
                [sg.Button('Задание 2'),sg.Button('Задание 4')],
                [sg.Button('Вернуться в меню')]]
    window = sg.Window('Лаб. работа №3', layout,size=(300,150),element_justification="center")
    while True:
            event, values = window.read() # type: ignore
            if event=='Задание 1':
                window.close()
                Laba3Zadan1()
            if event=='Задание 2':
                window.close()
                Laba3Zadan2()
            if event=='Задание 3':
                window.close()
                Laba3Zadan3()
            if event=='Задание 4':
                window.close()
                Laba3Zadan4()
            if event=='Вернуться в меню':
                window.close()
                Menu1()
            if event==None:
                break

def Laba4():
    layout = [  [sg.Text("Выберите задание ")],
                [sg.Button('Задание 1'),sg.Button('Задание 3')],
                [sg.Button('Задание 2'),sg.Button('Задание 4')],
                [sg.Button('Вернуться в меню')]]
    window = sg.Window('Лаб. работа №4', layout,size=(300,150),element_justification="center")
    while True:
            event, values = window.read() # type: ignore
            if event=='Задание 1':
                window.close()
                Laba4Zadan1()
            if event=='Задание 2':
                window.close()
                Laba4Zadan2()
            if event=='Задание 3':
                window.close()
                Laba4Zadan3()
            if event=='Задание 4':
                window.close()
                Laba4Zadan4()
            if event=='Вернуться в меню':
                window.close()
                Menu1()
            if event==None:
                break

def Laba5():
    layout = [  [sg.Text("Выберите задание ")],
                [sg.Button('Задание 1'),sg.Button('Задание 3')],
                [sg.Button('Задание 2'),sg.Button('Задание 4')],
                [sg.Button('Вернуться в меню')]]
    window = sg.Window('Лаб. работа №5', layout,size=(300,150),element_justification="center")
    while True:
            event, values = window.read() # type: ignore
            if event=='Задание 1':
                window.close()
                Laba5Zadan1()
            if event=='Задание 2':
                window.close()
                Laba5Zadan2()
            if event=='Задание 3':
                window.close()
                Laba5Zadan3()
            if event=='Задание 4':
                window.close()
                Laba5Zadan4()
            if event=='Вернуться в меню':
                window.close()
                Menu1()
            if event==None:
                break

def Laba7():
    layout = [  [sg.Text("Выберите задание ")],
                [sg.Button('Задание 1')],
                [sg.Button('Задание 2')],
                [sg.Button('Задание 3')]]
    window = sg.Window('Лаб. работа №7', layout,size=(300,150),element_justification="center",)
    while True:
            event, values = window.read() # type: ignore
            if event=='Задание 1':
                window.close()
                Laba7Zadan1()
            if event=='Задание 2':
                window.close()
                Laba7Zadan2()
            if event=='Задание 3':
                window.close()
                Laba7Zadan3()
            if event==None:
                break

def Laba8():
    layout = [  [sg.Text("Выберите задание ")],
                [sg.Button('Задание 1')],
                [sg.Button('Задание 2')],
                [sg.Button('Задание 3')]]
    window = sg.Window('Лаб. работа №8', layout,size=(300,150),element_justification="center",)
    while True:
            event, values = window.read() # type: ignore
            if event=='Задание 1':
                window.close()
                Laba8Zadan1()
            if event=='Задание 2':
                window.close()
                Laba8Zadan2()
            if event=='Задание 3':
                window.close()
                Laba8Zadan3()
            if event==None:
                break

def Laba9():
    layout = [  [sg.Text("Выберите задание ")],
                [sg.Button('Задание 1'),sg.Button('Задание 3')],
                [sg.Button('Задание 2'),sg.Button('Задание 4')]]
    window = sg.Window('Лаб. работа №9', layout,size=(300,150),element_justification="center",)
    while True:
            event, values = window.read() # type: ignore
            if event=='Задание 1':
                window.close()
                Laba9Zadan1()
            if event=='Задание 2':
                window.close()
                Laba9Zadan2()
            if event=='Задание 3':
                window.close()
                Laba9Zadan3()
            if event=='Задание 4':
                window.close()
                Laba9Zadan4()
            if event==None:
                break

def Laba10():
    layout=[[sg.Text('Выберите задание')],
            [sg.Output(expand_x=True,expand_y=True, key='Вывод'),sg.Slider(key='Номер',orientation='h', range=(1,8))],
            [sg.Button('Выполнить')]]
    window = sg.Window('Лаб. работа 10', layout, element_justification='center', size=(500,250))
    while True:
        event, values = window.read() # type: ignore
        arr=np.array([[1,2,3,4,5,6,7,8],
                [8,7,6,5,4,3,2,1],
                [2,3,4,5,6,7,8,9],
                [9,8,7,6,5,4,3,2],
                [1,3,5,7,9,7,5,3],
                [3,1,5,3,2,6,5,7],
                [1,7,5,9,7,3,1,5],
                [2,6,3,5,1,7,3,2]])
        if event=='Выполнить' and values['Номер']==1:
            window['Вывод'].update('') # type: ignore
            print(arr, '\n', 'Функция возведения всех элементов матрицы в квадрат')
            print(np.square(arr))
        if event=='Выполнить' and values['Номер']==2:
            window['Вывод'].update('') # type: ignore
            print(arr,'\n', 'Функция сложения по строкам')
            b2 = np.array(arr.sum(axis=1))
            print(b2.reshape(8, 1))
        if event=='Выполнить' and values['Номер']==3:
            window['Вывод'].update('') # type: ignore
            print(arr,'\n', 'Функция возведения в квадрат всех элементов четных столбцов')
            b3=arr.copy()
            b3[:, 1::2] **= 2
            print(b3)
        if event=='Выполнить' and values['Номер']==4:
            window['Вывод'].update('') # type: ignore
            print(arr,'\n', 'Функция умножения по строкам')
            b4=[]
            for i in range(0,8):
                b4.append(np.prod(arr[i]))
            b4=np.array(b4)
            print(b4.reshape(8, 1))
        if event=='Выполнить' and values['Номер']==5:
            window['Вывод'].update('') # type: ignore
            print(arr,'\n', 'Функция замены всех четных элементов матрицы на 0')
            b5=arr.copy()
            b5=np.where(b5%2==0,b5==0,b5)
            print(b5)
        if event=='Выполнить' and values['Номер']==6:
            window['Вывод'].update('') # type: ignore
            print(arr,'\n', 'Функция удаления строки в матрице, чей номер равен введенному числу')
            b6=arr.copy()
            de=int(sg.PopupGetText('Введите номер строки:')) # type: ignore
            print('Номер введеной строки - ',de)
            b6=np.delete(b6,de-1,axis=0)
            print(b6)
        if event=='Выполнить' and values['Номер']==7:
            window['Вывод'].update('') # type: ignore
            print(arr,'\n', 'Функция, которая меняет первую и последнюю строку матрицы местами')
            b7=arr.copy()
            b7[0], b7[-1] = b7[-1], b7[0]
            print(b7)
        if event=='Выполнить' and values['Номер']==8:
            window['Вывод'].update('') # type: ignore
            print(arr,'\n', 'Функция, которая находит число по строке и столбцу')
            b8=arr.copy()
            strk=int(sg.PopupGetText('Введите номер строки:')) # type: ignore
            stlb=int(sg.PopupGetText('Введите номер столбца:')) # type: ignore
            print('Номер введеной строки - ',strk)
            print('Номер введеного столбца - ',stlb)
            num=b8[strk-1,stlb-1]
            print('Найденный элемент - ',num)
        if event== sg.WIN_CLOSED:
                break

def PromejOkno():
    layout = [  [sg.Text("Хотите продолжить?",key='1')],
                [sg.Button('Да, продолжить'),sg.Button('Вернуться в меню')],
                [sg.Button('Выйти из программы')]]
    window = sg.Window('Встал вопрос', layout,element_justification="center")
    while True:
        event, values = window.read() # type: ignore
        if event==sg.WIN_CLOSED or event=='Да, продолжить':
            window.close()
            return False
        if event=='Вернуться в меню':
            window.close()
            return 1
        if event=='Выйти из программы':
            window.close()
            return 2

def Laba1Zadan1():
    layout = [  [sg.Text("Впишите значения:")],
                [sg.Text('a:'),sg.Input(key='a')],
                [sg.Text('b:'),sg.Input(key='b')],
                [sg.Text('c:'),sg.Input(key='c')],
                [sg.Text('k:'),sg.Input(key='k')],
                [sg.Text('Результат действия: (a**2/b**2+c**2*a**2)/(a+b+c*(k-a/b**3))+c+(k/b-k/a)*c')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 1', layout)
    while True:
        event, values = window.read() # type: ignore
        if event=='Ответ: ':
            try:
                window['Otvet'].update(abs((int(values['a'])**2/int(values['b'])**2+int(values['c'])**2*int(values['a'])**2)/(int(values['a'])+int(values['b'])+int(values['c'])*(int(values['k'])-int(values['a'])/int(values['b'])**3))+int(values['c'])+(int(values['k'])/int(values['b'])-int(values['k'])/int(values['a']))*int(values['c']))) # type: ignore
            except ZeroDivisionError:
                window['Otvet'].update('Ошибка деления на ноль') # type: ignore
            except ValueError:
                window['Otvet'].update('Вводите целые числа') # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba1Zadan2():
    layout = [  [sg.Text("Впишите список, содержащий строки и числа:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод четных символов:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 2', layout)
    while True:
        event, values = window.read() # type: ignore
        ac=str(values['a'])
        c=[]
        m=[]
        for i in ac:
            c.append(i)
        di=c[1::2]
        dil=len(di)
        for ih in range(dil):
            m.append(di[ih])
        if event=='Ответ: ':
            window['Otvet'].update(m) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba1Zadan3():
    layout = [  [sg.Text("Впишите целые числа через пробел:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод сложения чисел больше 10:'),
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]]
    window = sg.Window('Задание 3', layout)
    while True:
        event, values = window.read() # type: ignore
        c=str(values['a']).split(' ')
        d=0
        for i in range(len(c)):
            di=int(c[i])
            if int(di)>10:
                d=d+di 
        if event=='Ответ: ':
            window['Otvet'].update(d) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba1Zadan4():
    layout = [  [sg.Text("Впишите целые числа через пробел:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод максимального числа:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 4', layout)
    while True:
        event, values = window.read() # type: ignore
        c=str(values['a']).split(' ')
        d=[]
        for i in range(len(c)):
            d.append(int(c[i]))
        if event=='Ответ: ':
            window['Otvet'].update(max(d)) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba2Zadan1():
    layout = [  [sg.Text("Впишите целые числа:")],
                [sg.Text("my_number"),sg.Text("user_number")],
                [sg.Input(key='a',size=(10)),sg.Input(key='b',size=(10))],
                [sg.Text('Проверка на my > user:'),sg.Text(key="Otvet3")],
                [sg.Button('Ответ: '),sg.Text(key="Otvet"),sg.Text(">"),sg.Text(key="Otvet1"),sg.Text(key="TR/FL")]]
    window = sg.Window('Задание 1', layout,size=(370,150))
    while True:
        event, values = window.read() # type: ignore
        my_number=int(values['a'])
        user_number=int(values['b'])
        if event=='Ответ: ':
            if my_number <= user_number:
                window['Otvet3'].update('Введите еще раз число user') # type: ignore
                window['TR/FL'].update('(Неправильно!)') # type: ignore
            else:
                window['Otvet3'].update('') # type: ignore
                window['TR/FL'].update('(Правильно!)') # type: ignore
            window['Otvet'].update(my_number) # type: ignore
            window['Otvet1'].update(user_number) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba2Zadan2():
    layout = [  [sg.Text("Впишите строки через пробел:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод строк от 5 до 10 элем.:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 2', layout)
    while True:
        event, values = window.read() # type: ignore
        spisok=str(values['a']).split(' ')
        spis=[]
        for i in spisok:
            if len(i)>=5 and len(i)<10:
                spis.append(i)
        if event=='Ответ: ':
            window['Otvet'].update(spis) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba2Zadan3():
    layout = [  [sg.Text("Впишите целое число знаков для вывода:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод русских заглавных букв:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 3', layout)
    while True:
        event, values = window.read() # type: ignore
        alfavit =''.join([chr(i) for i in range(ord('а'), ord('а')+32)])
        rand_string = ''.join(random.choice(alfavit.upper()) for i in range(int(values['a'])))
        if event=='Ответ: ':
            window['Otvet'].update(rand_string) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba2Zadan4():
    layout = [  [sg.Text("Впишите строку:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод всех цифр:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 4', layout)
    while True:
        event, values = window.read() # type: ignore
        stroka=str(values['a'])
        stroka1 =''
        for i in stroka:
            if i.isdigit():
                stroka1+=i
        if event=='Ответ: ':
            window['Otvet'].update(stroka1) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba3Zadan1():
    layout = [  [sg.Text("Впишите строку, состоящую из слов, пробелов и знаков препинания:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод слова  больше  5  символов, разделитель слов в строке — пробел.:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 1', layout)
    while True:
        event, values = window.read() # type: ignore
        spisok=str(values['a'])
        spis=''
        spisok=spisok.replace('.',' ')
        spisok=spisok.replace(',',' ')
        spisok=spisok.split()
        for i in spisok:
            if len(i)>=5:
                spis=spis+' '+i
        if event=='Ответ: ':
            window['Otvet'].update(spis) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba3Zadan2():
    layout = [  [sg.Text("Cтроковая переменная, содержащая информацию о студентах:")],
                [sg.Text('Ф;И;О;Возраст;Категория;Иванов;Иван;Иванович;23 года;Студент 3 курса;Петров;Семен;Игоревич;22 года;Студент 2 курса')],
                [sg.Text('Вывод в виде таблицы:'),sg.Button('Таблица')],
                [sg.Text(key="Otvet")]]
    window = sg.Window('Задание 2', layout)
    while True:
        event, values = window.read() # type: ignore
        x=PrettyTable()
        my_string  =  'Ф;И;О;Возраст;Категория;Иванов;Иван;Иванович;23 года;Студент 3 курса;Петров;Семен;Игоревич;22 года;Студент 2 курса'
        p = my_string.split(';')
        x.field_names=[p[0]+p[1]+p[2]+'        ','           '+p[4],'              '+p[3]]
        x.add_row([p[5]+' '+p[6]+' '+p[7],p[9],p[8]])
        x.add_row([p[10]+' '+p[11]+' '+p[12],p[14],p[13]])
        x.align = "l"
        x.border = False
        if event=='Таблица':
            window['Otvet'].update(x) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba3Zadan3():
    layout = [  [sg.Text("Cтроковая переменная, содержащая информацию о студентах:")],
                [sg.Text('ФИО;Возраст;Категория;')],
                [sg.Text('Иванов  Иван  Иванович;23 года;Студент  3  курса;Петров  Семен  Игоревич;22  года;Студент  2 курса;')],
                [sg.Text('Иванов Семен Игоревич;22 года;Студент 2 курса;Акибов Ярослав Наумович;23  года;Студент  3  курса;')],
                [sg.Text('Борков  Станислав  Максимович;21 год;Студент  1  курса;Петров  Семен  Семенович;21  год;Студент  1 курса;')],
                [sg.Text('Романов  Станислав  Андреевич;23  года;Студент  3  курса;Петров Всеволод Борисович;21 год;Студент 2 курса')],
                [sg.Text('Вывод информации о Петровых:'),sg.Button('Ответ')],
                [sg.Text(key="Otvet")]]
    window = sg.Window('Задание 3', layout)
    while True:
        event, values = window.read() # type: ignore
        my_string  =  'ФИО;Возраст;Категория;Иванов  Иван  Иванович;23 года;Студент  3  курса;Петров  Семен  Игоревич;22  года;Студент  2 курса;Иванов Семен Игоревич;22 года;Студент 2 курса;Акибов Ярослав Наумович;23  года;Студент  3  курса;Борков  Станислав  Максимович;21 год;Студент  1  курса;Петров  Семен  Семенович;21  год;Студент  1 курса;Романов  Станислав  Андреевич;23  года;Студент  3  курса;Петров Всеволод Борисович;21 год;Студент 2 курса'
        p = my_string.split(';')
        otv=[]
        for i in range(len(p)):
            if 'Петров' in p[i]:
                otv.append(p[i]+':'+' '+p[i+1]+' '+p[i+2])
        if event=='Ответ':
            window['Otvet'].update(otv) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba3Zadan4():
    layout = [  [sg.Text("Впишите строку, содержащую знаки препинания:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод кол-ва элементов и кол-во слов:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 4', layout)
    while True:
        event, values = window.read() # type: ignore
        spisok=str(values['a'])
        d=len(spisok)
        spisok=spisok.replace('.',' ')
        spisok=spisok.replace(',',' ')
        spisok=spisok.split()
        if event=='Ответ: ':
            window['Otvet'].update(str(d)+' '+'и'+' '+str(len(spisok))) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba4Zadan1():
    layout = [  [sg.Text("Впишите целые числа кол-во строк и столбцов:")],
                [sg.Input(key='a',size=15 ),sg.Input(key='b',size=15)],
                [sg.Text('Вывод матрицы:'),sg.Button('Ответ')],
                [sg.Text(key="Otvet")],
                [sg.Text('Вывод матрицы в строке:')],
                [sg.Text(key="Otvet2")],
                [sg.Text('Вывод суммы:'),sg.Text(key="Otvet1")]]
    window = sg.Window('Задание 1', layout)
    while True:
        event, values = window.read() # type: ignore
        sym=0
        a=int(values['a'])
        b=int(values['b'])
        n=np.random.randint(0,100,size=(a,b))
        for i in range(a):
            for o in range(b):
                num=n[i,o]
                sym=sym+num
        if event=='Ответ':
            window['Otvet'].update(n) # type: ignore
            window['Otvet2'].update(n.tolist()) # type: ignore
            window['Otvet1'].update(sym) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba4Zadan2():
    layout = [  [sg.Text("Впишите список:")],
                [sg.Input(key='a')],
                [sg.Text('Впишите значения через пробел:')],
                [sg.Input(key='b')],
                [sg.Text('Вывод строк:'),sg.Button('Ответ')],
                [sg.Text(key='Otvet')]]
    window = sg.Window('Задание 2', layout)
    while True:
        event, values = window.read() # type: ignore
        spisok=[]
        stroka=str(values['a'])
        for o in range(len(stroka)):
            spisok.append(stroka[o])
        spisok.pop(0)
        spisok.pop(0)
        spis=str(values['b']).split()
        for i in range(len(spis)):
            spisok.append(spis[i])
        if event=='Ответ':
            window['Otvet'].update(spisok) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba4Zadan3():
    layout = [  [sg.Text("Дан список в виде:")],
                [sg.Text("my_len  =  [['БО-331101',['Акулова  Алена',  'Абушкина Ксения']],['БОВ-421102',['Аванесков Аванес','Петров Афанасий']],['БО-331103',['Степанов Степан','Аша Линь']]]")],
                [sg.Text('Вывод Группы и ФИО в определенном виде:'),sg.Button('Вывод')],
                [sg.Text(key="Otvet")],
                [sg.Text(key="Otvet1")]]
    window = sg.Window('Задание 3', layout)
    while True:
        event, values = window.read() # type: ignore
        my_len  =  [['БО-331101',['Акулова  Алена',  'Бабушкина Ксения']],['БОВ-421102',['Иванов Иван','Петров Петр']],['БО-331103',['Степанов Степан','Шо Линь']]]
        if event=='Вывод':
            for a in range(len(my_len)):
                x=my_len[a]
                y=x[1]
                p=[]
                window['Otvet'].update(str(x[0]).center(30)) # type: ignore
                for b in range(len(y)):
                    p.append(str(y[b]).center(30))
                window['Otvet1'].update(p) # type: ignore

            
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba4Zadan4():
    layout = [  [sg.Text("Дан список в виде:")],
                [sg.Text("my_len  =  [['БО-331101',['Акулова  Алена',  'Абушкина Ксения']],['БОВ-421102',['Аванесков Аванес','Петров Афанасий']],['БО-331103',['Степанов Степан','Аша Линь']]]")],
                [sg.Text('Вывод всех студентов с фамилией на А:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 4', layout)
    while True:
        event, values = window.read() # type: ignore
        my_len  =  [['БО-331101',['Акулова  Алена',  'Абушкина Ксения']],['БОВ-421102',['Аванесков Аванес','Петров Афанасий']],['БО-331103',['Степанов Степан','Аша Линь']]]
        zp=[]
        for a in range(len(my_len)):
            x=my_len[a]
            y=x[1]
            for b in range(len(y)):
                z=y[b]
                if 'А' in z[0]:
                    zp.append(z+'-'+x[0])
        if event=='Ответ: ':
            window['Otvet'].update(zp) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba5Zadan1():
    layout = [  [sg.Text("Впишите путь папки:")],
                [sg.Input(key='a')],
                [sg.Text('Вывод количества файлов:')],
                [sg.Button('Ответ: '),sg.Text(key="Otvet")]]
    window = sg.Window('Задание 1', layout)
    while True:
        event, values = window.read() # type: ignore
        direc=str(values['a'])
        files = os.listdir(direc)
        if event=='Ответ: ':
            window['Otvet'].update(len(files)) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba5Zadan2():
    layout = [  [sg.Text("В файле csv записана строка:")],
                [sg.Text("[[1, Иванов Иван Иванович, 23, БО-11111],[2, Сидоров Семён Семенович, 23, БО-111111],")],
                [sg.Text('[3, Яшков Илья Петрович, 24, БО-222222], [4, Абушк Георг Иванович, 22, БО-333333]]')],
                [sg.Text('Вывод отсортированного списка по фамилиям:')],
                [sg.Button('Вывод')],
                [sg.Text(key="Otvet")],
                [sg.Text(key="Otvet1")]]
    
    window = sg.Window('Задание 2', layout)
    while True:
        event, values = window.read() # type: ignore
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
        if event=='Вывод':
            window['Otvet'].update(strend[0:2]) # type: ignore
            window['Otvet1'].update(strend[2:4]) # type: ignore
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba5Zadan3():
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
    zadan2 = strend
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
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba5Zadan4():
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
        zadan2 = strend
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
                Proomj=PromejOkno()
                if Proomj==1:
                    window.close()
                    Menu1()
                    return False
                if Proomj==2:
                    window.close()
                    return False
                if event==None:
                    break

def Laba7Zadan1():
    layout=[[sg.Text('(0:Первый обьект,1:Второй обьект, 2:Третий обьект, 3:Четвертый обьект)')],
            [sg.Button('Вывод кол-ва ключей'),sg.Input(key='ZDN1',expand_x=True)]]
    window = sg.Window('Задание 1', layout)  
    while True:
        event, values = window.read() # type: ignore
        dic={0:'Первый обьект',1:'Второй обьект', 2:'Третий обьект', 3:'Четвертый обьект'}
        if event=='Вывод кол-ва ключей':
            window['ZDN1'].update(len(list(dic))) #type: ignore
        if event==None or event== sg.WIN_CLOSED:
            break   

def Laba7Zadan2():
    layout = [  [sg.Text("В файле csv записана строка:")],
                [sg.Text("[[1, Иванов Иван Иванович, 23, БО-11111],[2, Сидоров Семён Семенович, 23, БО-111111],")],
                [sg.Text('[3, Яшков Илья Петрович, 24, БО-222222], [4, Абушк Георг Иванович, 22, БО-333333]]')],
                [sg.Text('Вывод отсортированного словаря по фамилиям:')],
                [sg.Output(size=(0,8),expand_x=True),sg.Button('Вывод')]]
    
    window = sg.Window('Задание 2', layout)
    while True:
        event, values = window.read() # type: ignore
        with open('123.csv',encoding='utf-8') as f:
            reader = csv.reader(f,delimiter=',')
            stroka={}
            for row in reader:
                for row1 in row:
                    row1=row1.split(';')
                    stroka[row1[0]]=row1[1:]
            stroka1=[]
            for x in range(1,len(stroka)):
                stry=stroka[str(x)]
                stroka1.append(stry[0])
            stroka1.sort()
            strend={'No':['ФИО','Возраст','Группа']}
            for i in range(len(stroka1)):
                for y in range(1,len(stroka)):
                    if stroka1[i] in stroka[str(y)]:
                        strend[str(y)]=stroka[str(y)]
        if event=='Вывод':
            print(strend)
        Proomj=PromejOkno()
        if Proomj==1:
            window.close()
            Menu1()
            return False
        if Proomj==2:
            window.close()
            return False
        if event==None:
            break

def Laba7Zadan3():
    zadan2 =  {'4': ['Абушк Георг Иванович', '22', 'БО-333333'], 
               '1': ['Иванов Иван Иванович', '23', 'БО-111111 '], 
               '2': ['Сидоров Семен Семенович', '23', 'БО-111111 '], 
               '3': ['Яшков Илья Петрович', '24', 'БО-222222']}
    def Upd():
        strnach=[]
        keys=[]
        for i in zadan2.keys():
            keys.append(i)
        for i in range(len(zadan2)):
            zdn2 = zadan2[str(keys[i])]
            zdn2[1] = int(zdn2[1]) + 1 # type: ignore
            strnach.append(zdn2)
        return strnach
    
    def coxp():
        with open('1234.csv','w',encoding='utf-8',newline='') as f:
            writer = csv.writer(f,delimiter=';')
            writer.writerow(['ФИО','Возраст','Группа'])
            for i in range(len(upd)):
                writer.writerow(upd[i])


    
    layout = [  [sg.Text("Словарь из 2 задания:")],
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

def Laba8Zadan1():
    layout = [  [sg.Text("Cписок студентов:")],
                [sg.Text("[['1', 'Иванов Иван Иванович', '23', 'БО-111111 '], ['2', 'Сидоров Семен Семенович', '23', 'БО-111111 '],")],
                [sg.Text("['3', 'Яшков Илья Петрович', '24', 'БО-222222'], ['4', 'Абушк Георг Иванович', '22', 'БО-333333']]")],
                [sg.Button('Перевод в словарь')],
                [sg.Output(size=(100,3),key='Output')]]
    window = sg.Window('Задание 1', layout)
    while True:
        event, values = window.read() # type: ignore
        lisst=[['1', 'Иванов Иван Иванович', '23', 'БО-111111 '], ['2', 'Сидоров Семен Семенович', '23', 'БО-111111 '], ['3', 'Яшков Илья Петрович', '24', 'БО-222222'], ['4', 'Абушк Георг Иванович', '22', 'БО-333333']]
        slovar={}
        for i in lisst:
            slovar[i[0]]=i[1:]
        if event=='Перевод в словарь':
            print(slovar)
            Proomj=PromejOkno()
            if Proomj==1:
                window.close()
                Menu1()
                return False
            if Proomj==2:
                window.close()
                return False
            if event==None:
                break
        if event==None:
            break

def Laba8Zadan2():
    layout=[[sg.Text('Выберите задание:')],
            [sg.Slider(expand_x=True, key='Номер',orientation='h'),sg.Button('Выполнить')]]
    window = sg.Window('Задание 2', layout)  
    while True:
        slovar={'1': ['Иванов Иван Иванович', '23', 'БО-111111 '], 
                '2': ['Сидоров Семен Семенович', '23', 'БО-111111 '], 
                '3': ['Яшков Илья Петрович', '24', 'БО-222222'], 
                '4': ['Абушк Георг Иванович', '22', 'БО-333333']}
        event, values = window.read() # type: ignore
        if values['Номер']==1 and event=='Выполнить':
                window.close()
                layout=[[sg.Text('Увеличить  возраст  конкретного  студента  на  1.  Поиск  по  «ФИО»')],
                        [sg.Text('Введите ФИО: '),sg.Input(k='FIO'),sg.Button('Выполнить')],
                        [sg.Output(expand_x=True, size=(0,8)),sg.Button('Вернуться в выбор задания')]]
                window = sg.Window('Задание 1', layout)  
                while True:
                    event, values = window.read() # type: ignore
                    if event=='Выполнить':
                        FIO=values['FIO']
                        print('Изначальный словарь:','\n',slovar)
                        for i in range(1,len(slovar)+1):
                            g=slovar[str(i)]
                            if FIO == g[0]:
                                g[1] = str(int(g[1])+1)
                                print('Получилось: ',i,g)
                                print('Измененный словарь:','\n',slovar)
                                break
                        else: print('Нет такого ФИО')
                        Proomj=PromejOkno()
                        if Proomj==1:
                            window.close()
                            Menu1()
                            return False
                        if Proomj==2:
                            window.close()
                            return False
                        if event==None:
                            break
                    if event=='Вернуться в выбор задания':
                        window.close()
                        Laba8Zadan2()
                    if event==None:
                        break

        if values['Номер']==2 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Изменить «ФИО» студента. Поиск по «ФИО» ')],
                    [sg.Text('Введите ФИО: '),sg.Input(k='FIO1')],
                    [sg.Text('Введите новое ФИО: '),sg.Input(k='FIO2'),sg.Button('Выполнить')],
                    [sg.Output(expand_x=True, size=(0,8)),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 2', layout)  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    FIO=values['FIO1']
                    FIO2=values['FIO2']
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if FIO == g[0]:
                            g[0]=FIO2
                            print('Получилось: ',i,g)
                            print('Измененный словарь:','\n',slovar)
                            break
                    else: print('Нет такого ФИО')
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break

        if values['Номер']==3 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Увеличить  возраст  конкретного  студента  на  1.  Поиск  по  «№»')],
                    [sg.Text('Введите №: '),sg.Input(k='nom'),sg.Button('Выполнить')],
                    [sg.Output(expand_x=True, size=(0,8)),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 3', layout)  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    nom=values['nom']
                    if str(nom) in slovar:
                        g=slovar[str(nom)]
                        g[1]=str(int(g[1])+1)
                        print('Получилось: ',nom,g)
                        print('Измененный словарь:','\n',slovar)
                    else: print('Нет такого номера')
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break

        if values['Номер']==4 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Изменить  группу  студента.  Поиск  по    «ФИО»')],
                    [sg.Text('Введите ФИО: '),sg.Input(k='ФИО')],
                    [sg.Text('Введите группу: '),sg.Input(k='group'),sg.Button('Выполнить')],
                    [sg.Output(expand_x=True, size=(0,8)),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 4', layout)  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    FIO=values['ФИО']
                    group=values['group']
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if FIO == g[0]:
                            g[2]=group 
                            print('Получилось: ',i,g)
                            print('Измененный словарь:','\n',slovar)
                            break
                    else: print('Нет такого ФИО')
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break

        if values['Номер']==5 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Удалить  запись  о  студенте.  Поиск  по  «№» ')],
                    [sg.Text('Введите №: '),sg.Input(k='nom'),sg.Button('Выполнить')],
                    [sg.Output(expand_x=True, size=(0,8)),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 5', layout)  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    nom=values['nom']
                    if str(nom) in slovar:
                        del slovar[str(nom)]
                        print('Измененный словарь:','\n',slovar)
                    else: print('Нет такого номера')
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break

        if values['Номер']==6 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Если возраст студента больше 22 уменьшить его на 1')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 6', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if int(g[1]) >= 22:
                            g[1]= str(int(g[1])-1)
                            # print(i,g)
                    print('Измененный словарь:','\n',slovar)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break

        if values['Номер']==7 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Если возраст студента равен 23, удалить его из списка.')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 7', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if g[1] == '23':
                            del slovar[str(i)]
                            # print(i,g)
                    print('Измененный словарь:','\n',slovar)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break
            
        if values['Номер']==8 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('У всех студентов с фамилией «Иванов» увеличить возраст на 1.')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 8', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if 'Иванов' in g[0]:
                            g[1]=str(int(g[1])+1)
                            # print(i,g)
                    print('Измененный словарь:','\n',slovar)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break
            
        if values['Номер']==9 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('У студентов с фамилией «Иванов» изменить фамилию на «Сидоров»')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 9', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        g1=g[0]
                        g1=g1.split()
                        if 'Иванов' in g1[0]:
                            g1[0]='Сидоров'
                            g1=' '.join(g1)
                            g[0]=g1
                            # print(i,g)
                    print('Измененный словарь:','\n',slovar)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break
            
        if values['Номер']==10 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Поменять «ФИО» и «Группа» местами.')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 10', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        fio=g[0]
                        g[0]=g[2]
                        g[2]=fio
                        # print(i,g)
                    print('Измененный словарь:','\n',slovar)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan2()
                if event==None:
                    break

def Laba8Zadan3():
    layout=[[sg.Text('Выберите задание:')],
            [sg.Slider(expand_x=True, key='Номер',orientation='h'),sg.Button('Выполнить')]]
    window = sg.Window('Задание 3', layout)  
    while True:
        slovar={'1': ['Иванов Иван Иванович', '23', 'БО-111111'], 
                '2': ['Сидоров Семен Семенович', '23', 'БО-111111'], 
                '3': ['Яшкова Илья Петрович', '24', 'БО-2222222'], 
                '4': ['Абушк Георг Иванович', '22', 'БО-333333'],
                '5': ['Кедрова Роза Ивановна', '25', 'БО-111111'],
                '6': ['Жигалов Роман Эдуардович', '25', 'БО-1111111']}
        event, values = window.read() # type: ignore
        if values['Номер']==1 and event=='Выполнить':
                window.close()
                layout=[[sg.Text('Вывод списка студентов (а также информацию о них) группы БО-111111')],
                        [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                        [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
                window = sg.Window('Задание 1', layout,size=(550,150))  
                while True:
                    event, values = window.read() # type: ignore
                    if event=='Выполнить':
                        print('Изначальный словарь:','\n',slovar)
                        print('Список по требованиям:')
                        for i in range(1,len(slovar)+1):
                            g=slovar[str(i)]
                            if g[2] == 'БО-111111':
                                print(i,g)
                        Proomj=PromejOkno()
                        if Proomj==1:
                            window.close()
                            Menu1()
                            return False
                        if Proomj==2:
                            window.close()
                            return False
                        if event==None:
                            break
                    if event=='Вернуться в выбор задания':
                        window.close()
                        Laba8Zadan3()
                    if event==None:
                        break

        if values['Номер']==2 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод списка студентов (а также информацию о них) с номерами 1-10')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 2', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if i in range(1,11):
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break

        if values['Номер']==3 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод списка студентов (а также информацию о них) в возрасте 22 лет')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 3', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if g[1] == '22':
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break

        if values['Номер']==4 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод список студентов (а также информацию о них) с фамилией Иванов')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 4', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        g1=g[0]
                        g1=g1.split()
                        if 'Иванов' in g1[0]:
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break
            
        if values['Номер']==5 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод списка  студентов  (а  также  информацию  о  них),  чьи  фамилии заканчиваются на «а»')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 5', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        g1=g[0]
                        g1=g1.split()
                        g2=g1[0]
                        if g2[-1]=='а':
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break

        if values['Номер']==6 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод списка студентов (а также информацию о них), чей возраст –  четное число')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 6', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if int(g[1])%2==0:
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break

        if values['Номер']==7 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод списка  студентов  (а  также  информацию  о  них),  если  в  возрасте студента встречается число 5')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 7', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if '5' in g[1]:
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break
            
        if values['Номер']==8 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод списка студентов (а также информацию о них), если их номера группы длиннее 7 символов')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 8', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        gg=g[2]
                        if gg[-7::].isdigit():
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break
            
        if values['Номер']==9 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод списка студентов (а также информацию о них), если их «№» четное число')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 9', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        if i%2==0:
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break
            
        if values['Номер']==10 and event=='Выполнить':
            window.close()
            layout=[[sg.Text('Вывод списка студентов (а также информацию о них), если их номер группы заканчивается на «1»')],
                    [sg.Text('', expand_x=True),sg.Button('Выполнить'), sg.Text('', expand_x=True)],
                    [sg.Output(expand_x=True, size=(0,8),),sg.Button('Вернуться в выбор задания')]]
            window = sg.Window('Задание 9', layout,size=(550,150))  
            while True:
                event, values = window.read() # type: ignore
                if event=='Выполнить':
                    print('Изначальный словарь:','\n',slovar)
                    print('Список по требованиям:')
                    for i in range(1,len(slovar)+1):
                        g=slovar[str(i)]
                        gg=g[2]
                        if gg[-1::]=='1':
                            print(i,g)
                    Proomj=PromejOkno()
                    if Proomj==1:
                        window.close()
                        Menu1()
                        return False
                    if Proomj==2:
                        window.close()
                        return False
                    if event==None:
                        break
                if event=='Вернуться в выбор задания':
                    window.close()
                    Laba8Zadan3()
                if event==None:
                    break

def Laba9Zadan1():
    slovar={'1': ['Иванов Иван Иванович', '23', 'БО-111111'], 
            '2': ['Сидоров Семен Семенович', '23', 'БО-111111'], 
            '3': ['Яшкова Илья Петрович', '24', 'БО-2222222'], 
            '4': ['Абушк Георг Иванович', '22', 'БО-333333'],
            '5': ['Кедрова Роза Ивановна', '25', 'БО-111111'],
            '6': ['Жигалов Роман Эдуардович', '25', 'БО-1111111']}
    layout=[[sg.Text('Добавить студента в словарь')],
            [sg.Text('Введите номер студента:  '), sg.Input(expand_x=True, key='Nom')],
            [sg.Text('Введите ФИО студента:    '), sg.Input(expand_x=True, key='FIO')],
            [sg.Text('Введите Возраст студента:'), sg.Input(expand_x=True, key='Vozr')],
            [sg.Text('Введите Группу студента: '), sg.Input(expand_x=True, key='Group')],
            [sg.Output(expand_x=True,size=(0,8), key='Out'),sg.Button('Выполнить')]]
    window = sg.Window('Задание 1', layout)
    while True:
        event, values = window.read() # type: ignore
        if values['Nom'] in list(slovar) and event=='Выполнить':
            window['Nom'].update('Такой номер уже есть') # type: ignore

        if values['Nom'] not in list(slovar) and event=='Выполнить':
            window['Out'].update(False)
            slovar[values['Nom']]=[values['FIO'],values['Vozr'],values['Group']]
            print(slovar)
            
        if event== sg.WIN_CLOSED:
            break

def Laba9Zadan2():
    slovar={'1': ['Иванов Иван Иванович', '23', 'БО-111111'], 
            '2': ['Сидоров Семен Семенович', '23', 'БО-111111'], 
            '3': ['Яшкова Илья Петрович', '24', 'БО-2222222'], 
            '4': ['Абушк Георг Иванович', '22', 'БО-333333'],
            '5': ['Кедрова Роза Ивановна', '25', 'БО-111111'],
            '6': ['Жигалов Роман Эдуардович', '25', 'БО-1111111']}
    layout=[[sg.Text('Изменить данные о студенте в словаре')],
            [sg.Text('Введите номер студента:  '), sg.Input(expand_x=True, key='Nom')],
            [sg.Text('Введите ФИО студента:    '), sg.Input(expand_x=True, key='FIO')],
            [sg.Text('Введите Возраст студента:'), sg.Input(expand_x=True, key='Vozr')],
            [sg.Text('Введите Группу студента: '), sg.Input(expand_x=True, key='Group')],
            [sg.Output(expand_x=True,size=(0,8), key='Out'),sg.Button('Выполнить')]]
    window = sg.Window('Задание 2', layout)
    while True:
        event, values = window.read() # type: ignore
        if values['Nom'] not in list(slovar) and event=='Выполнить':
            window['Nom'].update('Такого номера нет') # type: ignore

        if values['Nom'] in list(slovar) and event=='Выполнить':
            window['Out'].update('')  # type: ignore
            slovar[values['Nom']]=[values['FIO'],values['Vozr'],values['Group']]
            print(slovar)
            
        if event== sg.WIN_CLOSED:
            break

def Laba9Zadan3():
    slovar={'1': ['Иванов Иван Иванович', '23', 'БО-111111'], 
            '2': ['Сидоров Семен Семенович', '23', 'БО-111111'], 
            '3': ['Яшкова Илья Петрович', '24', 'БО-2222222'], 
            '4': ['Абушк Георг Иванович', '22', 'БО-333333'],
            '5': ['Кедрова Роза Ивановна', '25', 'БО-111111'],
            '6': ['Жигалов Роман Эдуардович', '25', 'БО-1111111']}
    layout=[[sg.Text('Удаление данных о студенте в словаре')],
            [sg.Text('Введите номер студента:  '), sg.Input(expand_x=True, key='Nom')],
            [sg.Output(expand_x=True,size=(0,10), key='Out'),sg.Button('Выполнить')]]
    window = sg.Window('Задание 3', layout)
    while True:
        event, values = window.read() # type: ignore
        if values['Nom'] not in list(slovar) and event=='Выполнить':
            window['Nom'].update('Такого номера нет') # type: ignore

        if values['Nom'] in list(slovar) and event=='Выполнить':
            window['Out'].update('') #type: ignore
            del slovar[values['Nom']]
            print(slovar)
            
        if event== sg.WIN_CLOSED:
            break

def Laba9Zadan4():
    slovar={'1': ['Иванов Иван Иванович', '23', 'БО-111111'], 
            '2': ['Сидоров Семен Семенович', '23', 'БО-111111'], 
            '3': ['Яшкова Илья Петрович', '24', 'БО-2222222'], 
            '4': ['Абушк Георг Иванович', '22', 'БО-333333'],
            '5': ['Кедрова Роза Ивановна', '25', 'БО-111111'],
            '6': ['Жигалов Роман Эдуардович', '25', 'БО-1111111']}
    layout=[[sg.Text('Вывод данных о студенте')],
            [sg.Text('Введите номер студента:  '), sg.Input(expand_x=True, key='Nom')],
            [sg.Output(expand_x=True,size=(0,10), key='Out'),sg.Button('Выполнить')]]
    window = sg.Window('Задание 4', layout)
    while True:
        event, values = window.read() # type: ignore
        if values['Nom'] not in list(slovar) and event=='Выполнить':
            window['Nom'].update('Такого номера нет') # type: ignore
            window['Out'].update('') #type: ignore

        if values['Nom'] in list(slovar) and event=='Выполнить':
            window['Out'].update('') #type: ignore
            print(slovar[values['Nom']])
            
        if event== sg.WIN_CLOSED:
            break
Menu1()