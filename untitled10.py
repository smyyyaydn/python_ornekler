# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:55:39 2022

@author: smyyy
"""
from functools import reduce 
n=6
a=reduce(lambda a,b: a*b, [i for i in range(1,n+1)])
print(a)


x=["MerhaBA","PYTHON","pROGRAMLAMA","Dili"]
y=[i.title() for i in x]
print(' '.join(y))

x=["kayak","adana","yapay","kek","urfa","hatay"]
y=list(filter(lambda a:a==a[::-1],x))
print(y)

username=["ali","veli","fatma"]
passwords=["123","abc123","23e1z23"]
soz=map(lambda a,b : {a:b},username,passwords)
print(list(soz))


x=[1,2,3,4,5]
x=iter(x)
s=0
while True:
 try:
   s+=next(x)
 except StopIteration:
   break
 finally:
  print(s)
  
  
x=[1,2,3,256]
y=[2,3,3,0.5]
z=list(map(lambda a,b:int(a*b),x,y))
print(z)


x=[1,2,3]
y=[4,5,6]
z=list(zip(x+y))
print(z)


x=list (filter(lambda i: all([(i%7!=0),(i%5==0)]), (i for i in range(2000,3201))))
print(x)

names=["ali","ayşe","fatma","hasan"]
ages=[17,21,14,23]
adults=dict(filter(lambda zipped:18<=zipped[1],zip(names,ages)))
print(adults)

lista=["mer","bu","ay","1"]
listb=["haba","gün","ın","günü"]
listc=[i+j for i,j in zip(lista,listb)]
print(listc)


list1=["a","2"]
list2=["b","4"]
list3=[x+y for x in list1 for y in list2]
print(list3)

tuple1=(102,230,320,440,750)
tuple1=tuple1[::-1]
print(tuple1)

tuple2=("merhaba",[100,200,730],(15,125,245))
print(tuple2[1][1]+tuple2[2][0])


print(' '.join(map(lambda a: a[::-1] if len(a)>3 else a, "why do ı love python".split(" "))))


print (reduce(lambda a,b:a**b ,range(-1,6,2)))



y=lambda a,b:a*b

print(y(5,4))
