a,m=list(map(int,input().split()))
i=1
while ((m-a)/2>=a):
    i+=1
    m=m-a
    a+=1
print(i)
