'''sum of n natural numbers'''
# def fun(n:int)->int:
#     if n==0:
#         return 0
#     return n + fun(n-1)
#
# n=int(input())
# res=fun(n)
# print(res)


'''sum of individual digits'''

# def fun(n):
#     if n==0: return 0
#     if n%2==0:
#
#         return n % 10 + fun(n//10)


    # sum = 0
    # while n>0:
    #     r=n%10
    #     sum+=r
    #     n=n//10



def sumeven(n):
    if n==0:
        return 0
    sum = 0
    r=n%10
    n=n//10
    if n%2==0:
        sum+=r
    return sum
n=int(input())
res=sumeven(n)
print(res)
