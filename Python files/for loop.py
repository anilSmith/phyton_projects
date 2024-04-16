#for loop: for loop is a execute a block of code a fixed number of times.
#          you can iterate over a range,string,sequence etc.
# credit_crad="3637638"
# for i in credit_crad:
# #     print(i)
# for x in range(1,21):
#     if x==13:
#        break
#     else:
#         print(x)
# a=range(10)
# print(a)
# n=int(input())
# a=range(1,n+1)
# print("first ten natural numbers",list(a))
#
# a="python"
# for i in a:
#     print(i)
#
# n=int(input())
# for i in range(1,n+1):
#     print(i)

# n=int(input())
# for j in range(1,n+1):
#     for k in range(1,n+1):#2 input
#
#         print(k,end=" ")#output:1212
#
# n=int(input())
# for j in range(1,n+1):
#     for k in range(1,n+1):
#
#         print(j,end=" ")#output:1122
# x=8
# y=2
# print(x//y)
# print(x/y)
#
# a="""
# this is a multiple string
# in a line
# """
# print(a)
# n=int(input())
# for i in range (n):
#     for j in range (2*n-1):
#         print("*",end="")
#     print()


# side=int(input())
# for i in range(side):
#     for j in range(2*(side-i)):
#      print(" ",end="")
#
#     for j in range(i+1):
#         print("*",end=" ")
#         print("")
# n=int(input())
# for i in range(2,n):
#     if n%i==0:
#         print("not a prime")
# else:
#         print("prime")
# n=15
# factors=0
# for i in range(1,15):
#     if n%i==0:
#         factors+=i
#         print(i,end=" ")

# n= int(input())
# for n in range(n + 1):
#     count = 0
#     for i in range(1, n + 1):
#          if n % i == 0:
#            count += 1
#     if count == 2:
#         print(n, end=' ')
# a = int(input())
# b = int(input())
# for n in range(a, b + 1):
#     count = 0  # Reset count for each number n
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:  # Check if the number has exactly 2 factors
#         print(n, end=' ')

# n=10
# for n in range(n + 1):
#     count = 0
#     for i in range(1, n + 1):
#          if n % i == 0:
#            count += 1
#     if count == 2:
#        print(i,sep="",end=",")
# else:
#         print(i,sep=',',end=" ")
# n = int(input())
# primes = []
# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)
#
# print(*primes, sep=",")
# a = int(input())
# b = int(input())
# count = 0
# sum = 0
#
# for n in range(a, b + 1):
#     count = 0
#     for i in range(2, n + 1):
#         if n % i == 0:
#             count += 1
#
#     if count == 2:
#         sum += n
#         if count==sum:
#             print("yes")
#         else:
#             print("no")
#     else:
#         print("no")
#
# print("Sum of numbers with exactly 2 prime factors:", sum)

# a, b = map(int, input().split())
# for n in range(a, b + 1):
#     count = 0
#     for i in range(1, n + 1):
#          if n % i == 0:
#            count += 1
#     if count == 2:
#         print(n, end=' ')

# n = int(input())  # Takes an integer input from the user
# prime_numbers = []  # Initialize an empty list to store prime numbers
#
# for num in range(n + 1):  # Loops from 0 to n (inclusive)
#     count = 0  # Initializes a count variable to count the factors of num
#     for i in range(1, num + 1):  # Loops from 1 to num (inclusive)
#         if num % i == 0:  # Checks if i is a factor of num
#             count += 1  # If i is a factor, increments the count
#     if count == 2:  # Checks if num has exactly two factors (prime number condition)
#         prime_numbers.append((str(num)))  # Append the prime number to the list as a string
# # # Join the prime numbers list into a single string separated by commas
# output = ",".join(prime_numbers)
# #
# print(output)  # Prints the prime numbers separated by commas


# a,b= map(int,input().split())
# count = 0
# sum = 0
#
# for n in range(a, b + 1):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         sum += n
#         if count==sum:
#             print("yes")
#         else:
#             print("no")
#     else:
#         print("no")

# colours = ["black", "orange", "green", "yellow"]
# # for i in range(1,3):
#
# for i in colours:
#
#          print(i,end=" ")
x=0
x = int(input())

while (1<=x<=100):
    print(x)
    break
print("valid no")