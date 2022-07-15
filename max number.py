# a=[50,40,23,70,56,12,5,10,1]
# i=0
# max=0
# while i<len(a):
#     if max <a[i]:
#         max=a[i]
#     i+=1
# print(max)

a=[2,10,6,1,4,8,9,10,5,3,4]
i=1
k=0
s=[]
while i<len(a):
    if k<a[-i]:
        k=(a[-i])
        s.append(k)
    i+=1
print(s)

