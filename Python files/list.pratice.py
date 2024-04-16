# # n=int(input())
# # a=input().split()
# # for i in range(n): a[i]=(a[i])
# # x=["anil",24,"puli","karri"]
# # for i in x:
# #     print(x)
# # a=" marathalli, Bangalore, Karnataka "
# # a=a.split(" ")
# # print(a)
#
# # n=int(input())
# # a=input().split() # split the nume=bers eg. '24' '34' '23'
# # for i in range (len(a)): # to definr the lenfgth of the num n=5 or  n=3
# #     a[i]=int(a[i]) # to convert string to integer
# #
# # for x in a:
# #     if x%2==0:
# #         print(x,end=" ")
# # '''
# # 4
# # 3 5 7 8
# # even number in a list is 8 '''
#
# # n=int(input())
# # a=input().split() # split the nume=bers eg. '24' '34' '23'
# # for i in range (len(a)): # to definr the lenfgth of the num n=5 or  n=3
# #     a[i]=int(a[i]) # to convert string to integer
# #
# # for x in a:
# #     if x%2==1:
# #         print(x,end=" ")
# # '''
# # 5
# # 1 5 9 13 34
# # odd number in a list is 1 5 9 13  '''
#
#
# # n=int(input())
# # a=input().split() # split the nume=bers eg. '24' '34' '23'
# # for i in range (len(a)): # to definr the lenfgth of the num n=5 or  n=3
# #     a[i]=int(a[i]) # to convert string to integer
# #
# # for x in a:
# #         print(x,end=" ")
#
# '''
# 5
# 1 3 7 4 2
# numbers in a list is 1 3 7 4 2  '''
#
#
# # wap to print the prime numbers
# # n=int(input())
# # a=input().split()
# # for i in range(len(a)):
# #     a[i]=int(a[i])
# #
# # for x in a:
# #     if ( x>1 ):
# #         print(x,end=" ")
#
# #Wwap to sum the all elements in the list
# # n=int(input())
# # a=input().split()
# # for i in range(len(a)):
# #     a[i]=int(a[i])
# #     sum=0
# # for x in a:
# #     if x>0:
# #         sum+=x
# # print(sum,end="")
# #
# # '''5
# # 1 2 3 4 4
# # sum of the list is 14'''
#
#
# #Wwap to sum of all evens in the list
# # n=int(input())
# # a=input().split()
# # for i in range(len(a)):
# #     a[i]=int(a[i])
# #     sum=0
# # for x in a:
# #     if x%2==0:
# #         sum+=x
# # print(sum,end="")
# #
# # '''5
# # 1 2 3 4 5
# # sum of the even numbers in the above list is 6'''
#
# #Wwap to sum of all evens in the list
# # n=int(input())
# # a=input().split()
# # for i in range(len(a)):
# #     a[i]=int(a[i])
# #     sum=0
# # for x in a:
# #     if x%2==1:
# #         sum+=x
# # print(sum,end="")
# #
# # '''5
# # 1 2 3 4 5
# # sum of the odd numbers in the above list is 9 '''
#
# #wap to print the prime numbers
# n=int(input())
# a=input().split()
# for i in range(len(a)):
#     a[i]=int(a[i])
# for x in a:
#     f=0
#     for y in range(1,x+1):
#         if(x%y==0) :
#             f+=1
#     if(f==2):
#         print(x,end=" ")
#
#
# #wap to print the count of even numbers
# # n=int(input())
# # a=input().split()
# # for i in range(len(a)):
# #     a[i]=int(a[i])
# # count=0
# # for x in a:
# #     if ( x%2==0):
# #         count+=1
# #         print(x,end=" ")
# #
# '''3
# 1 2 3
# count of the prime numbers is 2 '''

n=6
a=[1 ,2, 100,3, 4, 5]
max=a[0]
for i in range(1,n):
    if max<a[i]:
        max=a[i]
print(max)
#
# # wap to print the count of odd numbers
# # n = int(input())
# # a = input().split()
# # for i in range(len(a)):
# #     a[i] = int(a[i])
# # count = 0
# # for x in a:
# #     if (x % 2 == 1):
# #         count += 1
# #         print(count, end=" ")
#
# '''3
# 1 2 3
# count of the prime numbers is 2 '''
# '''
# 5
# 1 2 3 4 5
# max=a[0]
# for i in range(1,n):
#     if max<a[i]:
#         max=a[i]
#
# '''