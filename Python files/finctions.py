#
# # def isprime(n):
# #     count = 0
# #     for i in range(1, n+1):
# #
# #         if n % i == 0:
# #
# #             count += 1
# #
# #     print("yes" if count == 2 else "no")
# # isprime(5)
# # isprime(7)
# # isprime(4)
# # n=int(input())
# # def iseven(n):
# #         if n % 2 == 0:
# #             print(n)
# # iseven(2)
# # iseven(3)
# # iseven(6)
# # def iseven(n):
# #     if n % 2 == 0:
# #         print(n)
# #
# # iseven(8)2
#
# # iseven(2)
# # iseven(4)
#
#
# # def add(a,b):
# #     print(a+b)
# # add(10,5)
# #
# # def pro(a,b,c):
# #     print(a*b*c)
# # pro(10,5,1)
# #
#
#
# # sum of individual digits
# # n=int(input())
# # sum=0
# # mul=0
# # while n>0:
# #         r=n%10
# #         sum+=r
# #         mul*=r
# #         n=n//10
# #         if sum==mul:
# #             print("yes")
# #         else:
# #             print("no")
# #
# # #
# # n= 6
# # sum_of_divisors = 0
# # for i in range(1, n):
# #     if n % i == 0:
# #         sum_of_divisors += i
# #
# # if sum_of_divisors == n:
# #     print("Perfect")
# # else:
# #     print("Not perfect")
#
# # while n > 0:
# #     r = n % 10
# #     sum_of_digits += r
# #     product_of_digits *= r
# # #     n = n // 10
# # def greatings():
# #     print("hi good morning")
# #     print("how are you")
# #
# # res=greatings()
# # print(res)
# # print(res)
# # print(res)
#
# # def isprime(n):
# #     count=0
# #     for i in range(1,n+1):
# #         if n%i==0:
# #             count+=1
# #
# #     return (count==2) # return the value and stored in a value and give back to the control statement
# #     print(n,end=" ")
# #
# #
# # n=int(input())
# # res_no=isprime(n)
# # print(res_no)
# # print(res_no)
# # print(res_no)
# # print(res_no)
# # print(res_no)
#
# # def isprime():
# #     count=0
# #     for i in range(1,n+1):
# #         if n%i==0
# # def great():
# #     print("hello world")
# #     print("good morning")
#
# # def add(a,b):
# #         c=a+b
# #         print(c)
# # add(5,4)
# # great()
# def happy_bithday():
#     print("happy birthday")
#     print("how old are you")
#     print("happy birthday to you")
#     print()
#
# happy_bithday()
#
# def happy_bithday(name,age):
#     print(f"happy birthday{name}")
#     print(f"how old are you {age}")
#     print("happy birthday to you")
#     print()
#
# happy_bithday("bro",20)
# happy_bithday("steve",20)
# happy_bithday("joe",20)
# #return=statement used to end end a function and send  a result back to the caller
#
# # def add(x,y):
# #     z=x+y
# #     return(z)
# # def subtract(x,y):
# #     z=x-y
# #     return(z)
# # st)
# # print(add(1,2))
# def create_name(first_name,last_name):
#     first_name=first_name.capitalize
#     last_name = last_name.capitalize
#     return(first_name+" "+last_name)
# full_name=create_name("bro","code")
#
# print(full_name)
#

# def isperfect(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     return ("no" if sum==n else "yes")
#
# n=list(map(int,input().split()))
# red=list(map(isperfect,n))
# print(red)
# res=list(filter(isperfect,n))
# print(res)
# '''6 28 30 40 #input
# [1, 1, 0, 0] # map uses to store the results value
# [6, 28]# filter uses to store the original data value'''
# print(*res) # * usess to unpacking all the elements in the list

# right shift
# n=list(map(int,input().split()))
# for i in range(2):
#     x=n.pop()
#     n.insert(0,x)
# print(n)


# left shift
# n=list(map(int,input().split()))
# for i in range(2):
#     x=n.pop(0)
#     n.append(x)
# print(n)

'''the difference between remove and pop is to remove the value permanently and
pop is used to store the remove value in  another variable '''
#
# n = list(input().split())
# c=0
# for x in range(len(n)-1,-1,-1):
#     if c==0:
#         print("Hi",end=" ")
#     if c==len(n)-1:
#         print("and",end=" ")
#     c += 1
#     print(n[x],end =" ")


# if a person have more income and high credit card bills
# person_has_higher_income=False
# person_has_higher_creditcard=True
#
# if person_has_higher_income or person_has_higher_creditcard:
# #     print("eligible for loan")
# secret_number=9
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     guess=int(input("guess: "))
#     guess_count +=1
#     if guess==secret_number:
#         print("own")
#
# command=""
# started=False
# while True:
#     command =input("> ")
#     if command.lower() == "start":
#         if started:
#             print("car already started")
#         else:
#             started=True
#         print("car started")
#     elif command.lower()=="stop":
#         if not started:
#             print("car is already started ")
#         else:False
#         print("car stopped")
#     elif command =="help":
#         print("""
# start-to stop the car
# stop-to stop the car
# quit-to quit the car""")
#     elif command=="quit":
#         break
#     else:
#         print("i dont understand that")

# for item in range(5,10,2):
#     print(item)
# prices=[10,20,30]
# total=0
# for price in prices:
#     total=total+price
# print(f"total:{total}")
# for x in range(4):
#     for y in range(3):
# #         print(f"({x},{y})")
# numbers=[1,1,1,1,5]
# for x_count in numbers:
#     output=""
#     for count in range(x_count):
#         output+="x"
#     print(output)

# names=["sarah","john","mosh","bob"]
# names[0]="jon"
# print(names[2:])
# print(names)
# numbers=[11,2,5,6,10]
# max=numbers[0]
# for number in numbers:
#     if number>max:
#        max=number
# print(max)
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # matrix[0][1]=20
# # print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)
#

# message=input(">")
# words=message.split(" ")
# emojis={
#     ":)":"😀",
#     ":(":"🥲"
# }
# output=""
# for word in words:
#     output+=emojis.get(word,word) + " "
# print(output)

# i=0
# while i<5:
#     print(i,end=" ")
#     i+=1
#     if i==3:
#         break
# else:
#     print(0)
#
# from sample import *
# a=10
# b=7
# issum(a,b)
# def isprime(n):
#     count=0
#     for i in range(1,n):
#         if n%i==0:
#            count+=1
#     return count==2
# n=int(input())
# isprime(n)
# def isprime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     return 1 if count == 2 else 0
# n=int(input())
# a = list(map(int,input().split()))
# # new=[]
# # for ele in a:
# #     res_ele=isprime(ele)
# #     new.append(res_ele)
# # for x in new:
# #     print(x,end=" ")
# # new=list(map(isprime,a))
# new=list(filter(isprime,a))
# print(*new)

# def square(x):
#     return x**2
# numbers=[2,3,4,5,6,7]
# squared_numbers=list(map(square,numbers))
# print(squared_numbers)



# def iseven(n):
#     if n%2==0: return
#      print(n)
#
# n=int(input())
# iseven(n)


# def even(n):
#     if n>0:
#         return
#     even(n - 1)
#     print(n,end=" ")
#
#
# a=int(input())
# even(a)

# def fun(n):
#     if n==1:
#         return
#
#     # fun(n-1) # for forward printing
#
#     if n%2==0:
#         print(n,end=" ")
#     fun(n - 1) # for backward printing
#
# n=5
# fun(n)

''' for even function forword printing 
     2 4     '''

# chat gpt code for better understanding
def fun(n):
    # Base case: if n is 1, return immediately
    if n == 1:
        return

    # Check if n is even
    if n % 2 == 0:
        # If n is even, print it without a newline
        print(n, end=" ")
  # in this  place for backward printing
    # Call the function recursively with n - 1
    fun(n - 1)  # for forward printing

# Example usage: call fun with n = 5
n = 5
fun(n)
 