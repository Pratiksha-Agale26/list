# a=[11000,2000,32000,400,5200]
# i=0
# b=[]
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             b.append(a[i])
#             break
#         a[i]//=10
#     i+=1
# print(b)

# list1 = [2, -7, 5, -64, -14]
# i=0
# count=0
# count1=0
# while i<len(list1):
#     if list1[i]>=0:
#         count+=1
#     else:
#         count1+=1
# print("positive",count)
# print("negative",count1)

a=[12, 67, 98, 34]
i=0
b=[]
while i<len(a):
    a[i]=str(a[i])
    j=0
    s=0
    while j<len(a[i]):
        s+=int(a[i][j])
        j+=1
    b.append(s)
    i+=1
print(b)

         
