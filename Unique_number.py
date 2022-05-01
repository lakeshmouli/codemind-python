n=int(input())
l=str(n)
k=[]
for i in l:
    k.append(i)
c=[]
for i in k:
    if i not in c:
        c.append(i)
if len(k)==len(c):
    print("Unique Number")
else:
    print("Not Unique Number")