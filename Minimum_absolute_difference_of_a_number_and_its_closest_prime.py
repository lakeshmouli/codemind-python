from math import sqrt
def isprime(n):
    if(n==1 or n==0):
        return false
    for i in range(2,int(sqrt(n)+1)):
        if(n%i==0):
            return False
    return True
a=int(input())
j,h,g=1,0,0
k,m=1,1
x,y=False,False
if isprime(a)==True:
    print(a-a)
else:
    while True:
        h=a+j
        g=a-j
        if(isprime(h)==True):
            x=True
        if(isprime(g)==True):
            y=True
        j+=1
        if(x==True or y==True):
            break
    if(x==False and y==True):
        print(abs(g-a))
    elif(x==True and y==False):
        print(abs(h-a))
    elif(x==True and y==True):
        k=abs(a-g)
        m=abs(a-h)
        if k>m:
            print(m)
        else:print(k)