n=int(input())
num=n
while n:
        d=n%10
        n=n//10
        if num%2==0 and d%2==1:
               print("Mixed")
               break
        if num%2==1 and d%2==0:
               print("Mixed")
               break
else:
       if num%2==0:
               print("Even")
       else:
               print("Odd")