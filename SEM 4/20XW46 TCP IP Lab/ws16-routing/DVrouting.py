#the graph (ADJACENCY LIST)
comp={'A':{'B':2,'C':4},'B':{'A':2,'C':1},'C':{'A':4,'B':1,'D':2},'D':{'C':2}}
vertices=['A','B','C','D']

#accessing dict
# print(comp['A']) #neighbours of A
# print(comp['A']['B']) #cost of the neighbour

#statpadding
for i in comp:
    comp[i][i]=0
    for j in vertices:
        if j not in comp[i]:
            comp[i][j]='inf'

#dict after statpadding
print(comp)

#initial routing table
for i in comp:
    print(f"{i} routing table:")
    for j in comp[i]:
        print(f"{j}:{comp[i][j]} ",end='')
    print()




