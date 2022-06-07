import sys
MAX_INT = sys.maxsize

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
            comp[i][j]=MAX_INT

#dictgraph
print(f"The graph as a dict \n {comp}")

# readable display
def print_routing_table(graph):
    for i in graph:
        print(f"{i} routing table:")
        for j in graph[i]:
            if graph[i][j]==MAX_INT:
                k='inf'
            else:
                k=graph[i][j]
            print(f"{j}:{k} ",end='')
        print()

print("-------------------INITIAL ROUTING TABLE ------------------------- \n")
print_routing_table(comp)
print()

def find_cost(path_graph,curr_node):
    costs=list()
    for i in path_graph:
        if i==curr_node:
            pass
        else:
            costs.append(comp[i][curr_node]+path_graph[i])

    return min(costs)

def set_cost(node):

    for i in comp[node]:
        k = find_cost(comp[node],i)
        if k < comp[node][i]:
            comp[node][i]=k

    return comp

# comp=set_cost('A')
# print_routing_table(comp)
# print()
# comp=set_cost('B')
# print_routing_table(comp)
# print()
# comp=set_cost('C')
# print_routing_table(comp)
# print()
# comp=set_cost('D')
# print_routing_table(comp)
# print()

for i in vertices:
    comp=set_cost(i)

print("\n\n-----------------------------FINAL ROUTING TABLE--------------------------\n")
print_routing_table(comp)
