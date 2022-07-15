# a=[[1,2,3],[4,5,6,7],[23,45,1]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum+=a[i][j]
#         j+=1
#     i+=1
# print(sum)

# a=[1,2,3,4,5,6,7,8]
# i=0
# sum=0
# pro=1
# while i<len(a):
#     if i<=4:
#         sum+=a[i]
#     else:
#         pro*a[i]
#     i+=1
# print("sum",sum)
# print("pro",pro)

# a=[1,2,3,4,5,6,7,8,9,10,12,11]
# i=0
# b=[]
# k=1
# c=2
# while i<len(a):
#     s=[a[i],a[k],a[c]]
#     b.append(s)
#     i+=3
#     k+=3
#     c+=3
# print(b)

# a=[[1,2,3],[4,5,6],[10,11,12],[7,8,9,11,2]]
# i=0
# b=[]
# max=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if (a[i][j])>max:
#             max=len(a[i])
#             b=a[i]
#         j+=1
#     i+=1
# print(max,b)

# a=[1,2,0,3,0,6,0,8,9,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(c+b)

# a=[1,342,75,23,98]
# b=[75,25,98,12,78,10,1]
# i=0
# k=[]
# while i<len(a):
#     if a[i] in b:
#         k.append(a[i])
#     i+=1
# print(k)
    
# a=[1100,1200,13000]
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

# a=[1,2,3,4,5]
# b=[2,3,0,5,1]
# i=0
# k=[]
# while i<len(a):
#     if a[i] not in b:
#         k.append(a[i])
#     i+=1
# print(k)

# a=["red","maroon","yellow","olive"]
# i=0
# b=[]
# while i<len(a):
#     c=(list(a[i]))
#     b.append(c)
#     i+=1
# print(b)

# a=[1,2,3,4,5]
# b=[2,3,4,7,8]
# i=0
# c=[]
# sum=0
# while i<len(a):
#     sum1=0
#     j=0
#     while j<len(b):
#         sum1+=a[i],b[i]
#         c.append(a[i])
#         j+=1
#     sum+=sum
#     i+=1
# print(c,sum)

# a=["tanuja","dimple","sakshi"]
# i=0
# b=[]
# while i<len(a):
#     j=1
#     while j<len(a[i])+1:
#         s=a[i][-j]
#         b.append(s)
#         j+=1
#     i+=1
# print(b)

# a=[[1,2,3],[4,5],[6,7]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)

# a=[1,2,3,4,5]
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     if i==2:
#         b.append(6)
#     i+=1
# print(b)

# a="pratiksha"
# i=0
# b=[]
# j=5
# while i<len(a):
#     if a[i] not in b:
#         c=a[i]
#         b.append(c)
#         b.append(j)
#         j+=5
#     i+=1
# print(b)

# a=[[2,4,3],[1,5,6],[7.9,10]]
# i=0
# b=[]
# s=0
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum+=a[i][j]
#         b.append(a[i][j])
#         j+=1
#     s+=sum
#     i+=1
# print(b,s)

# a=[[2,4,3],[1,5,6],[7.9,10,11]]
# i=0
# b=[]
# max=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         b=a[i]
#     i+=1
# print(max,b)

# a=[[2,4,3],[1,5,6],[7.9,10,11]]
# i=0
# b=[]
# max=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]>max:
#             max=a[i][j]
#             b=a[i][j]
#         j+=1
#     i+=1
# print(max,b)

# a=[10,20,30,40]
# b=[100,200,300,400]
# i=0
# c=[]
# while i<len(a):
#     j=1
#     while j<=len(b):
#         print(a[i],b[-j])
#         j+=1
#         i+=1


# a=[1234, 122, 1984, 19372, 100]
# i=0
# while i<len(a):



# x=float( input("enter the number") )
# if ( x== 1 ):
#     print("Yes")
# elif ( x== 2 ):
#     print ("Maybe")
# else:
#     print ("No")

# a = 12
# b = 26
# c = 4
# if a > b and a > c:
#     print("Number a is larger")
# if b > a and b > c:
#     print("Number b is larger")
# if c > a and c > b:
#     print("Number c is larger")

# a = 10
# if not a == 10:
#     print ("a not equals 10")
# else:
#     print("a equals 10")

a=[2,4,6,1,4,8,9,10,3,4]
i=0
b=[]
while i>len(a):
    if i>a[i]:
        



