mylist=list()
n=int(input("Enter the no of values:"))
print("enter the values for the list")
for i in range(0,n):
    ele=float(input())
    mylist.append(ele)
print("OG LIST:")
print(mylist)
emax=max(mylist)
emin=min(mylist)
normlist=list()
for i in mylist:
    temp=(float(i)-emin)/(emax-emin)
    normlist.append(temp)
print("NORMALIZED LIST:")
print(normlist)

