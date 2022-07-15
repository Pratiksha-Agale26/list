a=["tanuja","dimple","sakshi"]
i=0
b=[]
while i<len(a):
    j=1
    while j<len(a[i])+1:
        s=a[i][-j]
        b.append(s)
        j+=1
    i+=1
print(b)

# a=[[1],[1,2,3],[10,12,13,14,15],[7,8,9]]
# i=0
# max=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]>max:
#             max=a[i][j]
#             b=a[i][j]
#         j+=1
#     i+=1
# print(max)

# a=[[1],[1,2,3],[10,12,14,16],[7,8,9]]
# i=0
# max=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         b=a[i]
#     i+=1
# print(max,b)

# a=[1,2,3,4,5]
# b=[2,3,5,6,7]
# i=0
# sum=0
# s=0
# s1=0
# while i<len(a):
#     s+=a[i]
#     s1+=b[i]
#     sum=s+s1
#     i+=1
# print(s)
# print(s1)
# print(sum)

# a=[[1],[2,3],[4,5]]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     s=0
#     j=0
#     while j<len(a[i]):
#         s+=a[i][j]
#         j+=1
#     sum+=s
#     b.append(sum)
#     i+=1
# print(b)

