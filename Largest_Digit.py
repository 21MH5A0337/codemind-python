x=int(input())
s=[]
while x!=0:
 r=x%10
 x=x//10
 s.append(r)
print(max(s))