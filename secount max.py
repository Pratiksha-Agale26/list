a=[50,40,23,70,56,12,5,10,1]
i=0
max1=0
max2=0
while i<len(a):
    j=0
    while j<len(a):
        if a[j]>max1:
            max1=a[j]
        if a[j]>max2 and a[j]!=max1:
            max2=a[j]
        j+=1
    i+=1
# print(max1)
print(max2)