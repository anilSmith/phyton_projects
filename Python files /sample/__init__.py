# # x=10
# # y=20
#
# # def issum(x,y):
# #     print(x+y)
# #
# # issum(x,y)
# #
# # def issub(x,y):
# #     print(x-y)
# # issub(x,y)
# #
# # def ismul(x,y):
# #     print(x*y)
# # ismul(x,y)
# #
# # def isdiv(x,y):
# #     print(x/y)
# # isdiv(x,y)
#
# # from sample import *
# # a=10
# # b=7
# # c=ismul(a,b)  # types of imports in modules
# #
# # import sample
# # a=10
# # b=7
# # issum(a,b)
# #
# # import sample.issum
# # a=10
# # b=7
# # issum(a,b)
#
# def fun(n):
#     sum=0
#     if(n==0):return 0
#
#     while n>0:
#         r=n%10
#         n=n//10
#         sum+=1
#     return sum
#
# a=int(input())
# result=fun(a)
# print(result)


# def fun(n):
#     if(n==0): return 0
#     if n%2==0:
#
#         return n%10 + fun(n//10)
#
# a=int(input())
# result=fun(a)
# print(result)

# def fun(n):
#     if n == 0:  # Base case: If n is 0, return 0
#         return 0
#     if n % 2 == 0:  # Check if n is even
#         return n % 10 + fun(n // 10)  # Add last digit to sum and recursively call fun with n//10
#     else:
#         return fun(n // 10)  # If n is odd, skip it and recursively call fun with n//10
#
# # Input value
# a = 5762
#
# # Call the function fun with input a and store the result
# result = fun(a)
#
# # Print the result
# print(result)

# def fun(n):
#     if(n==0):
#         return 0
#     r=n%10
#     if(r%2==1):
#         return  1 +fun(n//10)
#
#     else:
#         return fun(n//10)
#
# a=int(input())
# result=fun(a)
# print(result)

# '' '  febonaci series in python

# def fun(n):
#     a=0
#     b=1
#
#     if n==0:
#         print(a)
#     else:
#         print(a)
#         print(b)
#
#         for i in range(2,n):
#             c = a+b
#             a=b
#             b=c
#             print(c)
# n=int(input())
# fun(n)
# by using lamda febonacci series
# fib = lambda n: 0 if n == 0 else ( 1 if n == 1 else fib(n-1) + fib(n-2))
# for i in range(10):
#     print(fib(i))

#prime findout by using lambda
n=int(input())
factors=list(filter(lambda i:n%i==0,range(1,n+1)))
print(len(factors)==2)