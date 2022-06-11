a=int(input())
b=int(input())
f=0
f1=0
i=1
j=1
x=a
y=b
for i in range(1,a):
    if a%i==0:
        f+=i
for j in range(1,b):
    if b%j==0:
        f1+=j
if f==b and f1==a:
    print('Amicable')
else:
    print('Not Amicable')