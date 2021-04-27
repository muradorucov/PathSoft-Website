n=int(input())
i=0
while (n>1):
    if n%2==0:
        i+=1
        n=n/2
    elif n%2==1:
       
        n=n+1
        i+=1
print(i)