def self_divide(n):
    k=str(n)
    j=list(k)
    count=0
    for i in j:
        if(int(i)==0):
            continue
        if(n%int(i)==0):
            count+=1
        if (count==len(k)):
            return True
    return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(self_divide(i)==True) :
        print(i,end=" ")