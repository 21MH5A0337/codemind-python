x=int(input())
c=0
y=0
z=1
s=0
print(y,z,end=' ')
while c<x-2:
 s=y+z
 c+=1
 y=z
 z=s
 print(s,end=' ')