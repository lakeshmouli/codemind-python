n=int(input())
c=True
for i in range(1,n+1):
    if n==i*i:
        c=True
        break
    else:
        c=False
print(c)