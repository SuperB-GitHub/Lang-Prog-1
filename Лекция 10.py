# class Person():
#     name = ""
#     money = 0
#     def out (self):	# self - ссылка на экземпляр класса
#         print(self.name,'has',self.money,'dollars.')
#     def changemoney (self,newmoney):
#         self.money = newmoney

# obj1 = Person()
# obj2 = Person()
# obj1.name = 'Bob'
# obj2.name = 'Masha'
# obj1.out()
# obj2.out()
# obj1.changemoney(150)
# obj1.out()

# class Critter():			          # создание класса
#     """Виртуальный питомец"""      # строка документирования
#     # создание метода
#     def talk(self):		
#         print("Привет.  Я животное – экземпляр класса Critter.")
#     def vvv(self):
#         print("Привет.  Я класс Critter.")

# # основная часть
# # создание объекта и вызов метода
# crit = Critter()
# crit.talk()
# crit.vvv()

# input("\nНажмите Enter, чтобы выйти.")

# class Critter():
#     """Виртуальный питомец""" 
#     def __inyit__(self):	# метод-конструктор
#         print("Появилось на свет новое животное!")
#     def __init__(self):	# метод-конструктор
#         print("Появилось на свет новое животное!")

#     def talk(self):
#         print("\n Привет.  Я животное – экземпляр класса Critter.")

# crit1 = Critter()
# crit2 = Critter()

# crit1.talk()
# crit2.talk()

class Critter():
    """Виртуальный питомец""" 
    def __init__(self, name):
        print("Появилось на свет новое животное!")
        self.name = name
    def __str__(self):		      # возвращает строку, которая
        rep = "Объект класса Critter\n"     # содержит значение
        rep += "имя: " + self.name + "\n"   # атрибута name 
        return rep
    def talk(self):
        print("Привет.  Меня зовут", self.name, "\n")

crit1 = Critter("Бобик")
crit1.talk()

crit2 = Critter("Мурзик")
crit2.talk()

print("Вывод объекта crit1 на экран:")
print(crit1)

print("Доступ к атрибуту crit1.name:")
print(crit1.name)

input ("\nНажмите Enter, чтобы выйти")