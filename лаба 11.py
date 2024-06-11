import sqlite3
conn = sqlite3.connect('Laba11.db')
cursor = conn.cursor()
def zadan1():
    cursor.execute('CREATE TABLE IF NOT EXISTS Кафедры (id INTEGER, Название TEXT, КолвоПреподавателей NUMERIC, id_Дисциплины REFERENCES Дисциплины(id))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Дисциплины (id INTEGER PRIMARY KEY, Название TEXT, КолвоЛекций NUMERIC, КолвоПрактик NUMERIC, Курсовая TEXT, ФормаКонтроля TEXT)')
    conn.commit()
    conn.close()

def zadan2():
    def add(table):
        if table==1:
            num=int(input('Сколько значений в таблицу вводим?: '))
            fin=''
            for i in range(num):
                idi=int(input('Введите id: '))
                nazv=input('Введите название кафедры: ')
                kol_vo=int(input('Введите кол-во преподавателей: '))
                idd1=int(input('Введите номер id дисциплины: '))
                idd=cursor.execute(f'SELECT id FROM Дисциплины WHERE id={idd1} ')
                fin+=f'({idi}, "{nazv}", {kol_vo}, {idd}),'
            fin=fin[:-1]
            print(fin)
            cursor.execute(f"INSERT INTO Кафедры (id, Название, КолвоПреподавателей, id_Дисциплины) VALUES {fin}")
        
        if table==2:
            num=int(input('Сколько значений?: '))
            fin=''
            for i in range(num):
                fio=input('Введите ФИО: ')
                nazv=input('Введите название кафедры: ')
                dol=input('Введите должность преподавателя: ')
                fin+=f'("{fio}", "{nazv}", "{dol}"),'
            fin=fin[:-1]
            print(fin)
            cursor.execute(f"INSERT INTO Дисциплины (id, Название, КолвоЛекций, КолвоПрактик, Курсовая, ФормаКонтроля) VALUES {fin}")
    
    def dell():
        num=int(input('Какую запись вы хотите удалить?: '))
        cursor.execute(f'DELETE FROM Задание234 WHERE _rowid_ ={num} ')

    def upd():
        try:
            num=int(input('Какую запись вы хотите изменить?: '))
            fio=input('Введите ФИО: ')
            nazv=input('Введите название кафедры: ')
            dol=input('Введите должность преподавателя: ')
            cursor.execute(f'UPDATE Задание234 SET fio="{fio}",НазвКаф="{nazv}",ДолжПреп="{dol}" WHERE _rowid_={num}')
        except sqlite3.OperationalError:
            print('Нет такого номера')

    table=int(input('''Введите номер таблицы:
[1] - Кафедры
[2] - Дисциплины
Номер: '''))
    add(table)
            
    conn.commit()
    conn.close()

# def zadan3():

zadan2()