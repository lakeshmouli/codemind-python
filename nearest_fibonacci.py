n=int(input())
a=0
b=1
t=a+b
k1=0
k2=0
x=False
while True:
    a,b=b,t
    t=a+b
    if n==t:
        x=True
        k1=t
    if n<t:
        k1=b
        k2=t
        break
if x==True:
    print(k1)
else:
    l1=abs(n-k1)
    l2=abs(k2-n)
    if l1>l2:
        print(k2)
    elif l1<l2:
        print(k1)
    else:
        print(k1,k2)