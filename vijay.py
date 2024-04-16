# n=int(input())
# k=n
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(j==i):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     for j in range(2,n+1):
#         if(j==k):
#             print("* ",end=" ")
#         else:
#             print("  ",end=" ")
#     for j in range(2,n+1):
#         if(j==i):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     for j in range(2,n+1):
#         if(j==k):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     for j in range(2,n+1):
#         if(j==i):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     for j in range(2,n+1):
#         if(j==k):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
#     k-=1

a=int(input())
b=int(input())
count=0
sum=0
for i in range(a,b+1):
    if n%i==0:
        count+=1
    if count==2:
        print("yes")
    else:
        print("no")