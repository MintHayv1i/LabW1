# Лабараторная номер 6 Task A 9
#Задача 1

dict = {}
str = input()

while str != '':
    key = str[:2]

    if key in dict:
        dict[key].append(str)
    else:
        dict[key] = [str]
    print(dict)

    str = input()

#Задача 2

dc1= set(input().split())
dc2 = set(input().split())
if dc1 <= dc2:
    print('Да')
else:
    print("Нет")

