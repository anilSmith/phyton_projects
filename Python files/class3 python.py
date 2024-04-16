# # # # # wap to print true in the given persons age is eggigible for voting otherwise print false
# # # # # age=input()
# # # # # age=int(age)
# # # # # print(age> 18)
# # # # #
# # # # # # we can change the above condition by
# # # # # age=input()
# # # # # age=int(age)
# # # # # print(age> 17)
# # # # #
# # # # # wap to print true if the first num is > 2nd num
# # # # # a=int(input())
# # # # # b=int(input())
# # # # # print(a>b)
# # # # # # if the first number is divisible by second num are not
# # # # # a=int(input())
# # # # # b=int(input())
# # # # # print(a%b==0) # a multiple b factor
# # # # # # a is divisible by b,
# # # # # # b is the factor(division) of a, (denominator)
# # # # # # a is the multiple of b (numerator)
# # # # # #wap to print true if the second is factor of first number or not
# # # # # b=int(input())
# # # # # a=int(input())
# # # # # print(b%a==0)
# # # # # # a is the multiple of b (numerator)
# # # # # b=int(input())
# # # # # a=int(input())
# # # # # print(b%a==0)
# # # # # #wap to print true if the given is multiple of 8 or not print false
# # # # # # #
# # # # # a=int(input())
# # # # # print(a%8==0)
# # # # # #wap to print true if the given is factor of 100 otherwise false
# # # # # a=int(input())
# # # # # print(100%a==0)
# # # # # value factor means numerator multiple means  denomeator
# # # # # # #wap to print true if the given first num greatest among three otherwise false
# # # # # a=int(input())
# # # # # b=int(input())
# # # # # c=int(input())
# # # # # print(a>b and a>c)
# # # # # #wap to print true if the given num is positive as well as multiple of 3 otherwise false
# # # # # n=int(input())
# # # # # print(n>0 and n%3==0)
# # # # # #wap to print true if the given num is multiple of both 3 and 5  otherwise false
# # # # # n=int(input())
# # # # # print(n%3==0 and n%5==0 )
# # # # # #wap to print true if the given num is multiple of  10 and factor of second num  otherwise false
# # # # # a=int(input())
# # # # # b=int(input())
# # # # # print(a%10==0 and b%a==0 )
# # # # # #wap to print true if the first num is second greast among three numbers  otherwise false note all distinct values
# # # # # a=int(input())
# # # # # b=int(input())
# # # # # c=int(input())
# # # # # print(b>a and a<c) or (c>a and a<b)
# # # # # # print(c>a>b or b>a>c)
# # # # # # #wap to print true if the first num is  greast among three numbers  otherwise false note all distinct values
# # # # # a=int(input())
# # # # # b=int(input())
# # # # # c=int(input())
# # # # # # print(a>b)
# # # # # a=int(input())
# # # # # c=int(input())
# # # # # print(a%3==0 and a%5==0) and (150%c==0) #  true and false returns true is wrong
# # # # # #
# # # # # # wap to print the value between 100 and 200 then print true
# # # # # n=int(input())
# # # # # print(n>100 and n<200)
# # # # #
# # # # # import keyword
# # # # # print(keyword.kwlist)
# # # # # n=int(input())
# # # # # if n>=0:
# # # # #      print("number is poaitive",1)
# # # # # if n<0:
# # # # #     print(-1)
# # # # # else:
# # # # #     print(0)
# # # # #
# # # # # numbers=[1,2,3,4,5]
# # # # # numbers[1:3]=[8,9]
# # # # # print(numbers)
# # # # # a=20
# # # # # b=5
# # # # # result=(a>b) or (a<b) and (a==0)
# # # # # print(result)
# # # # # n=int(input())
# # # # # i=1
# # # # # while i <= n:
# # # # #  if i%2 != 0:
# # # # #    print(i)
# # # # #  i += 1
# # # # # n=int(input())
# # # # # i = 0
# # # # # while i <= n:
# # # # #      if (i % 5 == 0 or i==0):
# # # # #          print(i*2)
# # # # #      i += 1
# # # # #  n=int(input())
# # # # # i=0
# # # # #
# # # # # while i<=n:
# # # # #     if(i<=0 or i%2==0 or i%2 != 0):
# # # # #         print(i**2)
# # # # #
# # # # #     i+=1
# # # #
# # # # # printing values in the reverse order
# # # # # n=int(input())
# # # # # i=10
# # # # # while i>=n:
# # # # #      print(i,end=" ")
# # # # #      i-=1
# # # #
# # # # #  # printing values in the  order
# # # # # n = int(input())
# # # # # i = 1
# # # # # while i <= n:
# # # # #      print(i, end=" ")
# # # # #      i += 1
# # # # #sum of n natural numbers
# # # # # n=int(input())
# # # # # i=0
# # # # # sum=0
# # # # # while i<=n:
# # # # #     sum+=i
# # # # #     i+=1
# # # # # print(sum)
# # # # # n=int(input())
# # # # # i=0
# # # # # while i<=n:
# # # # #      if i%2==0:
# # # # #           print(i)
# # # # #      i+=1
# # # #
# # # # # n=int(input())
# # # # # i=1
# # # # # while i<=n:
# # # # #      if i%5==0 and i%2!=0:
# # # # #           print(i)
# # # # #      i+=1
# # # # #factors of n natural numbers
# # # # # n=int(input())
# # # # # i=1
# # # # # while i<=n:
# # # # #      if n%i==0:
# # # # #           print(i)
# # # # #      i+=1
# # # #
# # # # # n=int(input())
# # # # # i=5
# # # # # while n<=i:
# # # # #      print(i,end=" ")
# # # # #      i -= 1
# # # # #wap to print even natural numbers example 5
# # # # # n = int(input())
# # # # # i = 0
# # # # # while n <= i:
# # # # #       if i%2==0:
# # # # #           print(i, end=" ")
# # # # #       i -= 1
# # # #
# # # #       #wap to print the count of even numbers
# # # # # n=int(input())
# # # # # i=1
# # # # # count_even=0
# # # # # while i<=n:
# # # # #      if i%2==0:
# # # # #           count_even+=1
# # # # #      i+=1
# # # #
# # # # # print(count_even)
# # # #
# # # #
# # # # #WAP to print the sum of even numbers upto ‘n’
# # # # # n=int(input())
# # # # # i=0
# # # # # sum_even=0
# # # # # while i<=n:
# # # # #      if i%2==0:
# # # # #           sum_even+=i
# # # # #      i+=1
# # # #
# # # # # print(sum_even)
# # # #
# # # # #WAP to print the count of factors of ‘n’
# # # # n=int(input())
# # # # i=1
# # # # count_factors=0
# # # # while i<=n:
# # # #      if n%i==0:
# # # #           count_factors+=1
# # # #      i+=1
# # # # print(count_factors)
# # # #
# # # # #WAP to print the sum of factors of ‘n’
# # # # # n=int(input())
# # # # # i=1
# # # # # sum=0
# # # # # while i<=n:
# # # # #      if n % i == 0:
# # # # #          sum+=i
# # # # #      i+=1
# # # # #
# # # # # print(sum)
# # # # n = int(input())
# # # # i = 1
# # # # sum_factors = 0
# # # #
# # # # while i <= n:
# # # #     if n % i == 0:
# # # #         sum_factors += i2
# # # #     i += 1
# # # #
# # # # print("Sum of factors for", n, ":", sum_factors)
# # # # n=int(input())
# # # # i=1
# # # # while n>0:
# # # #    r=n%10
# # # #    print(r)
# # # #    print(n//10)
# # # #    print(n)
# # # #    i+=1
# # #
# # # #wap to print the sum of individual digits
# # # # n=int(input())
# # # # sum=0
# # # # pro=1
# # # # while n>0:
# # # #    r=n%10
# # # #    sum+=r
# # # #    pro*=r
# # # #    print(r)
# # # #    n=n//10
# # # #    print(n)
# # # # print("sum of the digits is", sum)
# # # # print("product of the digits is",pro)
# # # #wap to print the sum of individual digits
# # # n=int(input())
# # # sum=0
# # # pro=1
# # # while n>0:
# # #    r=n%10
# # #    sum+=r
# # #    n = n // 10# n values becomes zero input is 76543 it becomes
# # #    # n=76543,7654,765,76,7,7,0
# # #    #r=3,4,5,6,7
# # #    #sum=3+4+5+6+7
# # #
# # # while n>0:
# # #    r=n%10  # n=76543,7654,765,76,7,7,0
# # #    #r=3,4,5,6,7
# # #    #pro=3*4*5*6*7
# # #    pro *= r
# # #    n=n//10
# # #
# # # print(sum == pro)# this statement is wrong because  in the line 247  value becomes zero
# # #
# # #
# # n=int(input())
# # temp=n
# # sum=0
# # while n>0:
# #    r=n%10
# #    sum+=r
# #    n = n // 10
# #
# # n=temp
# # pro = 1
# # while n>0:
# #    r=n%10
# #    pro *= r
# #    n=n//10
# #
# # print(sum == pro)
#
# #wap to print the sum of even digits and odd count
# # n=int(input())
# # temp=n
# # sum=0
# # while n>0:
# #    r=n%10
# #    n=n//10
# #    if r%2==0:
# #       sum += r
# # print(sum)
# #
# #
# # n=temp
# # count_odd=0
# # while n>0:
# #    r=n%10
# #    n = n // 10
# #    if r%2!=0:
# #       count_odd +=1
# # print(count_odd)
#
# n=int(input())
# evensum=0
# count_odd=0
# while n>0:
#    r=n%10
#    n = n // 10
#    if r%2==0:
#       evensum += r
#    elif r % 2 != 0:
#       count_odd += 1
# print(count_odd)
# print(evensum)

n=int(input())
res=0
while n>0:
   r=n%10
   res=res*10+r
   print(res)
   n=n//10
print(res)

