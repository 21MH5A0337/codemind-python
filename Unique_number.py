x=int(input())
i=[]
while x!=0:
    r=x%10
    x=x//10
    i.append(r)
    if(i.count(r))!=1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')