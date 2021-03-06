# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
#

for name in names:
    print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
# 

for name in names:
    x = len(name)
    print("{} - {} букв".format(name, x))


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика


is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
#

for name in names:

    if is_male[name]:
        print(name + " мужчина")
    else:
        print(name + " женщина")




#########PODUMAT!!!!!


# Задание 4
# Даны группы учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
# ???

print("Всего {} группы.".format(len(groups)))
for i in groups:
    print("В группе {} ученика".format(len(i)))


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
# ???

group_count = 1
for i in groups:
    print("Группа {}: {}".format(group_count, i))
    group_count += 1
