#Лабораторная работа №5 (task A 9.1)
#Задача 1

a=[]

s = input()
s=s.split()
print(s)

coun = [s[i] for i in range(len(s)) if "ро" in s[i] or "Ро" in s[i] or "рО" in s[i] or "РО" in s[i]]
#print(a)

print(coun)

#Задача 2
g = [[[1,2,3],[4,5,6]],[[7,8,9],[9,8,7]],[[0,1,2],[-1,-2]]]
res = [ k for i in g for j in i for k in j ]
print(res)

