# n=int(input())
# for i in range (1,n+1):
#      for j in range(1,n+1):
#          if j % 2 == 1:
#              print(1,end=' ')
#          else:
#              print(0,end=' ')
#      print()
#output for the i values
''' #5
j = 12345
i=1 11111
i=2 22222
i=3 33333
i=4 44444
i=5 55555
'''
#output for the j values
'''#5
12345
12345
12345
12345
12345
'''

#revrse a number by using n*n
# n=int(input())
# p=n*n
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(p,end=" ")
#         p-=1
# print()

#4 table ,5 table,6 table and remainiing decending
# n=int(input())
# p=n*n
# for i in range(1,n+1):
#     p=n*i
#     for j in range(1,n+1):
#         print(p,end=" ")
#         p-=1
#     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

''' output  5  
1 1 1 1 1 
1 0 0 0 1 
1 0 0 0 1 
1 0 0 0 1 
1 1 1 1 1 '''

''' input is 4
1 1 1 1 
1 0 0 1 
1 0 0 1 
1 1 1 1 '''
# # 3rd row zeros and 3rd column zeros
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==3 or j==3:
#
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()
'''5
0 0 1 0 0 
0 0 1 0 0 
1 1 1 1 1 
0 0 1 0 0 
0 0 1 0 0 '''

'''6
0 0 1 0 0 0 
0 0 1 0 0 0 
1 1 1 1 1 1 
0 0 1 0 0 0 
0 0 1 0 0 0 
0 0 1 0 0 0 '''

# print 1's at four corners and middle
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (i == 1 and j == 1):
#             print(1, end=" ")
#         elif (i == 1 and j == n):
#             print(1, end=" ")
#         elif (i == 3 and j == 3):
#             print(1, end=" ")
#         elif (i == 5 and j == 1):
#             print(1, end=" ")
#         elif (i == 5 and j == n):
#             print(1, end=" ")
#         else:
#             print(0,end=' ')
#     print()

''' input 5
1 0 0 0 1 
0 0 0 0 0 
0 0 1 0 0 
0 0 0 0 0 
1 0 0 0 1
 '''

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 and j==5):
#             print(2,end=" ")
#         elif i==3 and j==5:
#             print(4,end=" ")
#         elif i==2 and j==1:
#             print(3,end=" ")
#         elif i==4 and j==1:
#             print(5,end=" ")
#         elif i == 5 and j == 5:
#             print(6, end=" ")
#         else:
#             print(i,end=" ")
#     print()
# '''5
'''1 1 1 1 2 
3 2 2 2 2 
3 3 3 3 4 
5 4 4 4 4 
5 5 5 5 6
''''''

'''
# wap to print the right angle triangle
# for i in range (1,6):
#     for j in range(6-i+1):
#         print(j,end=" ")
#     print()

'''0 0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 '''
# n=int(input())
# for i in range(1,n+1):
#     p = i * 3
#     for j in range(1,n+1):
#
#         print(p,end=" ")
#         p+=1
#     print()
# n=int(input())
# for i in range (1,6):
#     for j in range(1,6-1):
#         print(j,end=" ")
#     print()

# for i in range (0,3):
#     for j in range(0,3):
#
#          print("*",end=" ")
#     print()

# n=int(input())
# for i in range (n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

'''5
1 2 3 4 5 
1 2 3 4       # pattern 25
1 2 3 
1 2 
1'''

# n=int(input())
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
'''5
1 
1 2 
1 2 3     # pattern 24
1 2 3 4 
1 2 3 4 5 
'''


# n=int(input())
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(n-i+1,end=" ")
#     print()
'''5
5
4 4
3 3 3
2 2 2 2   #pattern 23
1 1 1 1 1 '''


# n=int(input())
# for i in range (1,n+1):
#     p=i
#     for j in range(1,i+1):
#         print(p,end=" ")
#         p-=1
#     print()

'''5
1 
2 1 
3 2 1   # pattern 26
4 3 2 1 
5 4 3 2 1 '''

# n=int(input())
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
'''5
5 4 3 2 1 
4 3 2 1 
3 2 1    # pattern 27
2 1 
1 '''


# n=int(input())
# for i in range (1,6):
#     for j in range (1,6-1):
#         print(j,end=" ")
#     print()
#
# n=int(input())
# for i in range (1,6):
#     for j in range(1,6+1-j):
#         print(j,end=" ")
#     print()
# n=int(input())
# for i in range(n,0,-1):
#     for j in range (i,0,-1):
#         print(j,end=" ")
#     print()


# for i in range (5,0,-1):
#     for j in range  (i,5+1):
#         print(j,end=" ")
#     print()

'''5 
4 5   #pattern 30
3 4 5 
2 3 4 5 
1 2 3 4 5 '''


# for i in range (5,0,-1):
#     for j in range  (i,i*2):
#         print(j,end=" ")
#     print()
'''5 6 7 8 9 
4 5 6 7 
3 4 5   #pattern33
2 3 
1 
'''
# n=int(input())
# for i in range (1,n+1):
#     for j in range  (i,5+1):
#         print(j,end=" ")
#     print()
'''5
1 2 3 4 5 
2 3 4 5   
3 4 5   #pattern 31
4 5 
5 '''

# n=int(input())
# for i in range (5,0,-1):
#     for j in range  (5,i-1,-1):
#         print(j,end=" ")
#     print()
#
'''5
5 
5 4   #pattern 28
5 4 3 
5 4 3 2 
5 4 3 2 1 '''

# n=int(input())
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         if i%2==1:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()
'''5
1 
0 0 
1 1 1 
0 0 0 0 
1 1 1 1 1 
'''
#
# n=int(input())
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         if i%2==1:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print(j, end=" ")
#     for j in range (i-1,0,-1):
#              print(j,end=" ")
#     print()
#
'''5
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 '''

# n=int(input())
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print(j*2, end=" ")
#     for j in range (i-1,0,-1):
#              print(j*2,end=" ")
#     print()
'''5
2 
2 4 2 
2 4 6 4 2 
2 4 6 8 6 4 2  #pattern 42
2 4 6 8 10 8 6 4 2 
'''

# n=int(input())
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print(j*2-1, end=" ")
#     for j in range (i-1,0,-1):
#              print(j*2-1,end=" ")
#     print()
'''5
1 
1 3 1 
1 3 5 3 1  #pattern 41
1 3 5 7 5 3 1 
1 3 5 7 9 7 5 3 1 '''

# n=int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range (1,i*2):
#              print("*",end=" ")
#     print()

# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range (1,i*2):
#              print("*",end=" ")
#     print()