n=int(input())
r=n**2
c=0
while r:
    d=r%10
    c+=d
    r=r//10
if n==c:
    print("Neon Number")
else:
    print("Not Neon Number")