x=int(input())
s=x
a=0
b=1
while a<x:
    a,b=b,a+b
print(a==x)