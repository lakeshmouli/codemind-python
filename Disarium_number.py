n=input()
c=int(n)
k=len(n)
p=c
s=0
while c:
    d=c%10
    s+=d**k
    c=c//10
    k-=1
if (s==p):
    print(True)
else:
    print(False)