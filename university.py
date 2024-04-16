# words = set()
#
# def check(word):
#     return word.lower() in words
#
# def load(dictionary):
#     with open(dictionary) as file:
#         words.update(file.read().splitlines())
#     return True
#
# def size():
#
#     return len(words)
#
# def unload():
#     return True
# x=int(input())
# y=int(input())
# if x > y:
#     print("x is greather than y")
# elif x < y:
#     print("x is less than y")
# else:
#     print("x is equal to y")
# s=input("s:")
# t=input("t:")
#
# if s == t:
#     print("same")
# else:
#     print("different")

# s = input("do you agree ").lower()
# # s=s.lower()
# if s in ["y" , "yes"]:
#     print("agree")
# elif s in ["n", "no"]:
#     print("not agree")
# if s == "y" or s == "Y":
#     print("agreed")
# elif s == "n" or s == "N":
#     print("not agreed")

# i=0
# while i<5:
#     print("meow")
#     i+=
# def main():
#   meow(3)
# def meow(n):
#     for i in range(n):
#       print("meow")
# main()
# before=input("before: ")
# print("after: ",end="")
# for i in before:
#     print(i.lower(),end="")
# before=input("before: ")
# print(f"after: {before.upper()}")
# x=int(input())
# y=int(input())
# z=x/y
# print(f"{z:.5f}")
# scores=[4,5,7,9,12,15]
# average= sum(scores)/len(scores)
# # print(f"Average:{average}")
# print(average)

# # wap to find the right half avg
# num = [4, 5, 7, 9, 12, 15]
# half=num[3:6]
# average= (sum(half))/len(half)
# print(average)

# Example list
# my_list = [1, 2, 3]
# print(*my_list)
#
# # Unpacking the elements into individual variables
# var1, var2, var3 = my_list
#
# # Now var1, var2, and var3 hold the values of the corresponding elements in the list
# print(var1)  # Output: 1
# print(var2)  # Output: 2
# print(var3)  # Output: 3

# num = [4, 5, 7, 9, 12, 15]
# rev=num.sort(reverse=True)
# print(num[1])
# n=6
# a=[56,89,34,55,12,27]
# if 34 in a:
#     print("yes")
# else:
#     print("no")

# dic={6,3,4,6,1,3,2}
# output=print(dic)
# if output%2==0:
#     print(output)
# Example list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

# Using list comprehension to filter even numbers
# for num in my_list:
#     if num%2==0:
#         print(num)

# even_numbers = [num for num in my_list if num % 2 == 0]
#
# print("Even numbers in the list:", even_numbers)
