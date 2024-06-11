import csv
import PySimpleGUI as sg

'Создать окно в котором будет выводиться файл csv'

layout=[[sg.Text('Создать окно в котором будет выводиться файл csv')],
        [sg.Output(expand_x=True,expand_y=True, key='Вывод')],
        [sg.Button('Выполнить')]]
window = sg.Window('Зачет', layout, element_justification='center', size=(500,250))
while True:
    event, values = window.read() # type: ignore
    with open('123.csv',encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=',')
        stroka=[]
        for row in reader:
            for row1 in row:
                row1=row1.split(';')
                stroka.append(row1)
    if event=='Выполнить':
        print(str(stroka))
    if event==sg.WIN_CLOSED:
        break