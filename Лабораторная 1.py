def Zadan1():
    a=int(input('Введите a:'))
    b=int(input('Введите b:'))
    c=int(input('Введите c:'))
    k=int(input('Введите k:'))
    if a==0 or b==0 or c==0 or k==0:
        return print('Ошибка деления на ноль')
    return abs((a**2/b**2+c**2*a**2)/(a+b+c*(k-a/b**3))+c+(k/b-k/a)*c)

def Zadan2():
    ac=input()
    c=[]
    d=2
    for i in ac:
        c.append(i)
    di=c[1::2]
    dil=len(di)
    for ih in range(dil):
        print(d,di[ih])
        d=d+2
     

def Zadan3():
    c=input().split(' ')
    d=0
    for i in range(len(c)):
        di=int(c[i])
        if int(di)>10:
           d=d+di 
    return d

def Zadan4():
    c=input().split(' ')
    d=[]
    for i in range(len(c)):
        d.append(int(c[i]))
    return max(d)


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
    