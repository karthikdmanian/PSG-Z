a=set()
print(a,type(a))
n=int(input("Enter the no of values:"))
print("enter the elements of the set:")
for i in range(0,n):
    elt=int(input("Enter the element"))
    a.add(elt)
print(a)
a.pop(1)
