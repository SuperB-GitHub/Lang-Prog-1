import numpy as np
def Zadan1():
    sym=0
    a=int(input('Введите кол-во строк: '))
    b=int(input('Введите кол-во столбцов: '))
    n=np.random.randint(0,100,size=(a,b))
    print(n,end='\n\n')
    print(n.tolist(),end='\n\n')
    for i in range(a):
        for o in range(b):
            num=n[i,o]
            sym=sym+num
    return sym

def Zadan2():
    spisok=[]
    stroka=input('Введите строку: ')
    print(stroka)
    for o in range(len(stroka)):
        spisok.append(stroka[o])
    spisok.pop(0)
    spisok.pop(0)
    print(spisok)
    spis=input('Введите еще 2 символа: ').split()
    for i in range(len(spis)):
        spisok.append(spis[i])
    return spisok

def Zadan3():
    my_len  =  [['БО-331101',['Акулова  Алена',  'Бабушкина Ксения']],['БОВ-421102',['Иванов Иван','Петров Петр']],['БО-331103',['Степанов Степан','Шо Линь']]]
    for a in range(len(my_len)):
        x=my_len[a]
        y=x[1]
        print(str(x[0]).center(30))
        for b in range(len(y)):
            print(str(y[b]).center(30))
        print('')
    return ''

def Zadan4():
    my_len  =  [['БО-331101',['Акулова  Алена',  'Абушкина Ксения']],['БОВ-421102',['Аванесков Аванес','Петров Афанасий']],['БО-331103',['Степанов Степан','Аша Линь']]]
    for a in range(len(my_len)):
        x=my_len[a]
        y=x[1]
        for b in range(len(y)):
            z=y[b]
            if 'А' in z[0]:
                print(z,'-',x[0])
    return ''


u=True
while u==True:
    print('Вариант 1')
    Zadan=(int(input('Введите номер задания:')))
    if Zadan== 1:
        print(Zadan1())
    if Zadan== 2:
        print(Zadan2())
    if Zadan== 3:
        print(Zadan3())
    if Zadan== 4:
        print(Zadan4())
    if Zadan>=5 or Zadan<1:
        u=False