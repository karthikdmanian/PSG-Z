# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:24:24 2022

@author: 20pw16
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#inputs
dataword='1001'
divisor='1011'

#final codeword
codeword=''

#converting to list for operation
divisorList=list(divisor)
datawordList=list(dataword)

print(f"The divisor is {divisorList}")

# getting the max. deg to append 0s to the dataword
def getDegree(bits):
    max_deg=0
    k=0
    for i in bits:
       if i=='1' and max_deg<k:
           max_deg=k
       k+=1 
    
    return max_deg

deg_of_divisor=getDegree(divisor)

#appending 0s in dataword

def appendZeros(datawordList,deg):
    i=0
    while(i<deg):
        datawordList.append('0')
        i+=1
    
    return datawordList

datawordList=appendZeros(datawordList,deg_of_divisor)

print(f"The dividend is {datawordList}")

#getting reminder
def getXOR(divisor,currDiv):
    res=list()
    k=0
    for i in currDiv:
        if (int(i)==int(divisor[k])):
            res.append('0')
            
        else:
            res.append('1')
    
    return res
    

def getReminder(divisor,dividend):
    reminder=''
    n=0
    currDiv=dividend[:len(divisor)]

    while(n<len(dataword)):

        if(currDiv[0]==divisor[0]):
            currDiv=getXOR(divisor,currDiv)
            
        else:
            zList=list()
            for i in range(0,len(divisor)):
                zList.append('0')
                
            currDiv=getXOR(zList,currDiv)        
            
        n+=1
    
    #reminder 
    get_one=0
    for i in currDiv:
        if i=='1':
            get_one=currDiv.index(i)
            break
    
    reminder="".join(currDiv[get_one:])
    
    
    return reminder


reminder=getReminder(divisorList,datawordList)

codeword=dataword+reminder
print(f"this is the reminder {reminder}.")
print(f"this is the codeword {codeword}.")    