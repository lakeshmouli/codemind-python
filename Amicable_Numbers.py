n=int(input())
k=int(input())
t=n
p=k
s=0
a=0
for i in range(1,n//2+1):
    if (n%i==0):
        s=s+i
for j in range(1,k//2+1):
    if (k%j==0):
        a=a+j
if (t==a and p==s):
    print("Amicable")
else:
    print("Not Amicable")