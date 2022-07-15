# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# i=0
# b=[]
# c=[]
# count=0
# sum=0
# sum1=0
# while i<len(a):
#     if a[i]%2==0:
#         sum=sum+a[i]
#         b.append(a[i])
#         count+=1
#     else:
#         c.append(a[i])
#         count+=1
#         sum+=a[i]
#     i+=1
# print("even number",b)
# print("odd number",c)
# print(sum)
# print(count)
# print("average",sum/count)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
i=0
count=0
count1=0
sum=0
sum1=0
b=[]
c=[]
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
        sum=sum+a[i]
        count=count+1
    else:
        c.append(a[i])
        sum1=sum1+a[i]
        count1=count1+1
    i+=1
print(b,sum,count,"averge",sum/count)
print(c,sum1,count1,"averge",sum1/count)

# # i=0
# l=[]
# while i<100:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         l.append(i)
#     i+=1
# # print(l)

# a=[5,3,7,8]
# i=0
# # b=[]
# while i>0:
#     i=i*a[i]
#     a=a-1
#     # b.apeend(a[i])
# print(a)

# a=[1,342,75,23,98]
# b=[75,25,98,12,78,10,1]
# i=0
# k=[]
# while i<len(a):
#     if a[i] in b:
#         k.append(a[i])
#     i+=1
# print(k)

# a=[124,156,153,167]
# i=0
# sum=0
# # for i in a:
# while i>0:
#     sum=sum+i%10
#     i=i//10
#     print(sum)
# if i%sum==0:
#     print("harshad number")
# else:
#     print("not")


# a=[156,1242,3,6,7]
# i=0
# sum=0
# b=a
# while i<len(a):
#     c=a[i]%10
#     sum=sum+c
#     a[i]=a[i]//10
#     if a[i]%sum==0:
#         print("harshad",a[i])
#     else:
#         print("not",a[i])
#     i+=1