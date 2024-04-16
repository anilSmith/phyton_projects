# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)

#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")

# fib(10)
# '''0
# 1
# 1 2 3 5 8 13 21 34'''

n=int(input())
temp=n
pal=0
while n>0:
    r=n%10
    pal=pal*10+r
    n//=10
print(pal==temp)

