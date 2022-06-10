a=int(input())
is_negative=0
rev=0
if a<0:
    a=-a
    is_negative=1
    
while a>0:
    b=a%10
    rev=rev*10+b
    a=a//10
    
if is_negative==0:
    print(rev)
else:
    print(-rev)