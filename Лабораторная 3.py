from prettytable import PrettyTable
def Zadan1():
    spisok=input()
    spis=''
    spisok=spisok.replace('.',' ')
    spisok=spisok.replace(',',' ')
    spisok=spisok.split()
    for i in spisok:
        if len(i)>=5:
            spis=spis+' '+i
    return spis

def Zadan2():
    x=PrettyTable()
    my_string  =  'Ф;И;О;Возраст;Категория;Иванов;Иван;Иванович;23 года;Студент 3 курса;Петров;Семен;Игоревич;22 года;Студент 2 курса'
    p = my_string.split(';')
    x.field_names=[p[0]+p[1]+p[2],p[4],p[3]]
    x.add_row([p[5]+' '+p[6]+' '+p[7],p[9],p[8]])
    x.add_row([p[10]+' '+p[11]+' '+p[12],p[14],p[13]])
    x.align = "l"
    x.border = False
    return x

def Zadan3():
    my_string  =  'ФИО;Возраст;Категория;Иванов  Иван  Иванович;23 года;Студент  3  курса;Петров  Семен  Игоревич;22  года;Студент  2 курса;Иванов Семен Игоревич;22 года;Студент 2 курса;Акибов Ярослав Наумович;23  года;Студент  3  курса;Борков  Станислав  Максимович;21 год;Студент  1  курса;Петров  Семен  Семенович;21  год;Студент  1 курса;Романов  Станислав  Андреевич;23  года;Студент  3  курса;Петров Всеволод Борисович;21 год;Студент 2 курса'
    p = my_string.split(';')
    for i in range(len(p)):
        if 'Петров' in p[i]:
            # print(p[i],':', p[i+1],p[i+2])
            yield p[i]+': '+p[i+1]+ ' ' + p[i+2]
            

def Zadan4():
    spisok=input()
    print(len(spisok))
    spisok=spisok.replace('.',' ')
    spisok=spisok.replace(',',' ')
    spisok=spisok.split()
    return len(spisok)

u=True
while u==True:
    print('Вариант 1')
    Zadan=(int(input('Введите номер задания:')))
    if Zadan== 1:
        print(Zadan1())
    if Zadan== 2:
        print(Zadan2())
    if Zadan== 3:
        for el in Zadan3():
            print(el)
        # print(Zadan3())
    if Zadan== 4:
        print(Zadan4())
    if Zadan>=5 or Zadan<1:
        u=False

