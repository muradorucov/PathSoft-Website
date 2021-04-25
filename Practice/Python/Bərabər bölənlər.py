m= int(input())
n=1
i=0
while (n<m):
    if (m//n == m%n):
        i+=1
    n+=1
print(i)