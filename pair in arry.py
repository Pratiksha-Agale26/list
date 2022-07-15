n=[10,11,12,14,15,16,17,18,19]
number=30
list=[]
i=0
while i<len(n):
    j=0
    while j<len(n):
        a=n[i]
        b=n[j]
        if n[i]+n[j]==number:
            list.append([a,b])
        j+=1
    i+=1
print(list)

# a=int(input("enter the number"))
# if a>"0" and a<"9":
#     print("int")
# elif 
# print("floa")
# else:

# print(type(a))

# a=["mom","dad","aabiru","madam","nitin"]
# # i=length-1
# i=0
# count=0
# b=[]
# # length=len(a)
# while i<len(a):
#     # length=length-i
#     b.append(a[i])
#     if a[i][0]==a[i][-1]:
#         print(a[i])
#         # count=count+1
#     else:
#         count=count+1
#         # print(a[i])
#     i=i+1
# print(count,"palindrome",b)


# i=0
# c=0
# while i<len(a):
#     if a[i][0]==a[i][-1]:
#         print(a[i])
#         c+=1
#     i+=1
# print(c)