a=int(input())
c=a
rev=0
while a>0:
    b=a%10
    rev=rev*10+b
    a=a//10
    
if c==rev:
    print("True")
else:
    print("False")