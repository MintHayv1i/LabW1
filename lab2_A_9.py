#Лабораторная работа №2 (task A 9.1)

sName = input('Введите ФИО: ')
sAge = input('Введите возраст: ')
sHeigh = float(input('Введите вес: '))
sGroup = input('Введите свою группу: ')
print(sName+', '+sAge+', '+str(sHeigh)+', '+sGroup)

#(task A 9.2)
nc = input('Введите названия стран: ')
mas = nc.split()
print(mas)

elem_st = mas[0]
elem_end = mas[-1]

mas[0] = elem_end
mas[-1] = elem_st

print(mas)
print('Россия' in mas)