n=int(input())
k=n**2
n=str(n)
k=str(k)
l=len(n)
j=k[-l:]
if (int(j)==int(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")