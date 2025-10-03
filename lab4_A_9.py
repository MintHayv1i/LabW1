# Лабараторная номер 4 Task A 9
#Задание 1
print('Задача: 1')
s = input()
s = list(s.split())
#x.append(s)
#print(x)
for i, elem in enumerate((s), start =1):
    print(i,int(elem)**2)

print('Задача: 2')
#Задание 2
mon=0
for x in range(1000,1221,20):
    mon+=1
    if x>1200:
        print(mon)
        print(x)

