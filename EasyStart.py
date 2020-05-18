# ----Условия-----
# num = input("Введи число: ")
# if int(num) <= 32:
#     print("Low\n")
# elif 33 <= int(num) <= 66:
#     print("Middle")
# else:
#     print("High")


# -----Циклы-----
# i = 0
# while i < 5:
#     print("Your num is: ", i)
#     i += 1
#
# for j in 'hello world':
#     if(j == 'w'):
#         print("скипаю букву W")
#         continue           #break - выйдет из цикла
#     print(j * 2, end='')


# -----Списки (list)-----
# lis1 = []
# lis1 = [1, 2, 3, 5, 100, 'x', ['s', 't', 'r', 'o', 'k', 'a']]
# print(lis1)
#
# lis3 = [25, 24, 100, 100]
# lis2 = []
# lis2.append(27)            #добавить элемент в конец списка
# lis2.extend(lis3)          #расширение списка (добавили lis2 в lis3
# lis2.insert(3, 44)         #вставить по индексу
# lis2.remove(25)            #удаление по значению
# print(lis2.pop(0))         #удаляет по индексу и возвращает
# print(lis2.index(44))      #вернет индект элемента
# print(lis2.count(100))     #вернет кол-во элементов со значением 100
# lis2.sort()                #сортирует
# lis2.reverse()             #переворачивает список
# lis2.clear()               #очищает список
# print(lis2)                #вывести весь список


# -----Индексы и срезы-----
# l = [34, 'sd', 56, 34.34]
# print(l[0])                         #вывод по индексу
# print(l[0:4:2])                     #срез от/до [start,end,step]


# -----Кортежи(tuple)----- Короче говоря массив(фикс.длина)
# a = (43, 56, 23, 'd')           #кортеж
# b = [43, 56, 23, 'd']           #список - занимает больше память - не хорошо
#
# ab = tuple("Hello world")
# print(ab)


# -----Словари----- Ассоциативный массив, ключи, ссылки
# d1 = {'key1': 1, 'key2': 2}               #создание словаря
# print(d1['key2'])
#
# d2 = dict (fir='one', sec='second')       #второй способ создания
# print(d2['fir'])
#
# d3 = dict.fromkeys(['a', 'b'], 1)          #словарь из ключей, потом значения
# print(d3)
#
# d4 = {a : a ** 2 for a in range(7)}        #через цикл
# print(d4)


# -----Множества----- Нет повторяющихся элементов
# a1 = set("hello")
# print(type(a1))
# print(a1)
#
# a2 = {23, 24, 25}
# print(a2)
#
# a3 = frozenset("qwertty")               #set - можем изменять, frozenset - не можем
# print(a3)
# print(set(a3))
#
# a = {32, 45, 43, 12, 11}
# x = 45
# z = {67, 22, 90}
# print(len(a))                            #длина
# print(x in a)                            #есть ли x в a
# print(a.isdisjoint(z))                   #если нет общих элементов - true
# a.update(z)                              #объединение двух множеств
# print(a)
# a.intersection_update(z)                 #Объединение двух множеств
# a.difference_update(z)                   #Пересечение
# a.symmetric_difference_update()          #множество в одном из, но не в обоих
# a.add(32)
# a.remove(45)



# -----Функции----- def, lambda, return
# def myfunction(x, a, b):                    #объявление функции
#     return x + a + b
# print(myfunction(23, 12, 11))
#
#
# def funcvoidtype():
#     pass
#
#
# onestringfunc = lambda v, w: v - w          #функция в одну строку
# print(onestringfunc(2, 22))



#-----Исключения-----
# x =int(input())
# y =int(input())
#
# try:
#     res = x/y
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
#     res = 0
# print(res)


#-----работа с файлом-----
# f = open('input.txt', 'a')           # Открыть файл - название, способ открытия (запись, чтение итд)
# f.write("Hi, its me\n")
# f.close()


#-----Менеджеры With...as----- выполнение критических функций
# with open('input.txt', 'wt', encoding='utf-8') as inFile:
#     num = int(input())
#     line = str('1/ ' + str(num) + ' = ' + str(1/num))
#     print(line)
#     inFile.write(line)


#-----Молули. Import. form-----Ну типо библиотеки
# import math
# import time
# import os
# import random as r      #теперь random назвается r - просто переименовали
#
# #from название модуля import func - мы можем эксортировать конкретные функции с модуля
#
# print(math.e)
# print(math.pi)
# print(math.cos(0))
# print(time.time())
# print(os.getcwd())
# print(r.random())


#-----ООП-----Объекты и классы
#-----Наследование, Инкабсуляция, полиморфизм-----
#-----Конструкторы, переопределение методов-----
# class Person:
#     name = "Ivan"                  #поля
#     age = 10                       #поля
#     _slow = 1
#
#     def __init__(self, name, age):  #конструктор лего, это когда при создании мы сразу задаем параметры
#         self.name = name
#         self.age = age
#
# vlad = Person("vladislav", 13)                    #создал объект
# print(vlad.name)
# print(vlad.age)
#
# egor = Person("Егор4ик", 19)
# print(egor)
#
# class Student(Person):          #Студенты унаследовали все от человека (Student extends Rerson)
#     course = 1
#
#                                 #Если к методу или полю добавить в начало "_" - эо будет типо private
#                                 # Если к методу или полю добавить в начало "__" - эо будет типо protected