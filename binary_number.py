a=[1,0,0,1,1,0,1,1]
n=len(a)
i=0
sum=0
while i<n:
    sum=(2**i)*a[n-1-i]
    i+=1
print(sum)

