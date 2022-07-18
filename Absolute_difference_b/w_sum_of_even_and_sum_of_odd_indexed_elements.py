n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    if i%2==0:
        e+=l[i]
    if i%2==1:
        o+=l[i]
print(abs(e-o))