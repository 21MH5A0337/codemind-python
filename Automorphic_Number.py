a=int(input())
s=a*a
b=str(a)
c=str(s)
if c.endswith(b):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")