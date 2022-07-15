# a=[-1,2,3,4,-5,6,-7,8,-9,10]
# i=0
# count=0
# count1=0
# while i<len(a):
#     if a[i]>0:
#         count+=1
#     else:
#         count1+=1
#     i+=1
# print("negative",count)
# print("positive",count1)

a=[-1,2,3,-4,5,-6,7,-8,9,-10]
i=0
b=[]
while i<len(a):
    if a[i]>0:
        b.append(1)
    else:
        b.append(0)
    i+=1
print(b)
