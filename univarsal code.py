# a=[[1,2,3],4,[5,6],7,[8,9],10]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if type(a[i])==list:
#         b.append(a[i])
#     else:
#         c.append([a[i]])
#     i+=1
# # print(b+c)
# # print(c)
# for i in range(len(c)):
#     b[i].extend(c[i])
# print(b)


a=[[1,2,3],4,[5,6],7,[8,9],10]
i=0
b=[]
c=[]
while i<len(a):
    if type(a[i])==list:
        b.append(a[i])
    else:
        c.append([a[i]])
    i=i+1
for i in range(len(c)):
    b[i].extend(c[i])
print(b)

