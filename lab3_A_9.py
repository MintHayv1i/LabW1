 #Лабораторная работа номер 3 (task A 9)

 #Задача 1
em = input('Введите адрес: ')
emsp = em.split('@')
print(em)
print(emsp)
if len(em) >= 5 and '.' in emsp[-1]:
         print('Да')
else:
     print('Нет')

#Задача 2
a = input()
if ',' in a:
    a = a.replace(',',' ')
    a = a.split()

print(a)
m = (list(map(int, a)))
print(sum(m))
sumM = (sum(m))
lenM = len(m)
print(lenM)
af = sumM/lenM
print(af)
