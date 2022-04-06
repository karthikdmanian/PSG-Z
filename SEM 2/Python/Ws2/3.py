l1=[1,3,6,78,35,55,88]
l2=[12,24,35,24,88,120,155]
inter=list()
for x in l1:
    for y in l2:
        if(y==x):
            inter.append(y)
print(inter)
