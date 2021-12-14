names=['simon','vicky',['frank','tony',['joseph','ann']]]
print(names[2][1])
print(names[2][2][0])
print(names[2][2][1])
print(names[2][0])

names2=['immanuel','jared',['frank','irene',['patterson','bruno'],'peter']]
# names.extend(names2[2][3])
# print(names)
names.insert(3,names2[2][3])
print(names)
# n=print(names2[2][1][1])
# print(n)
# names.insert([2][1],n)
# print(names)
names.insert(names[2].index('tony'),names2[2][2][1])
print(names)

num=1/3
repr(num)


a=6
b=5
c=4
print(a>b>c)
