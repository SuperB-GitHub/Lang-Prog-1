import random
def Zadan1():
    my_number=int(input('Введите число:'))
    user_number=int(input('Введите число:'))
    while my_number < user_number:
        user_number=int(input('Введите еще раз число:'))

def Zadan2():
    spisok=input().split()
    spis=[]
    for i in spisok:
        if len(i)>=5 and len(i)<10:
            spis.append(i)
    print(spis)
            

def Zadan3():
    alfavit =''.join([chr(i) for i in range(ord('а'), ord('а')+32)])
    rand_string = ''.join(random.choice(alfavit.upper()) for i in range(5))
    return rand_string

def Zadan4():
    stroka=input()
    stroka1 =''
    for i in stroka:
        if i.isdigit():
            stroka1+=i
    return stroka1


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
