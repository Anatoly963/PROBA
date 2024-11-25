# ВСТРОЕННЫЕ ФУНКЦИИ

#int() - целое число
#float() - число с плавающей запятой
#bool() - логические значения
#str() - строки
#list() - список
#tuple() - кортеж
#dict() - словарь
#set() - множество

#bool() - логические значения. Отсутствие типа будет возвращать нам False. None — это отсутствие значения

list_1 = list('abcde')
print(list_1)               # ['a', 'b', 'c', 'd', 'e']  список

tuple_1 = tuple('abcde')
print (tuple_1)             # ('a', 'b', 'c', 'd', 'e')  кортеж

salary = (1800, 2300, 7500.5486, 1200.58742)    # Зарплаты сотрудников
print(len(salary))
print(round(sum(salary)/len(salary), 2), '- средняя зарплата в компании')    # средняя зарплата сотрудников с 2-мя знаками после запятой
print(round(max(salary), 2), '- максимальная зарплата в компании')    # максимальная зарплата сотрудников
print(round(min(salary), 2), '- минимальная зарплата в компании')    # минимальная зарплата сотрудников

names = ('Антон', 'Никита', 'Егор', 'Валя', 'Галя')
zipped = zip (names, salary)
#print (list(zipped))     #  [('Антон', 1800), ('Никита', 2300), ('Егор', 7500.5486), ('Валя', 1200.58742)] Объединение имен и зарплат
#print (dict(zipped)) # {'Антон': 1800, 'Никита': 2300, 'Егор': 7500.5486, 'Валя': 1200.58742}
zipped = dict(zipped)       # Надо определять словарь
#print(a)
print(zipped['Никита'], '- зарплата Никиты')     # другие определения перевести в комментарий
