# import mysql.connector
# mydb=mysql.connector.connect(host ="localhost",user= "root",passwd="Mysql@123",database="instagram")
# mycursor=mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# result=mycursor.fetchall()
# print(result)
# [('ani22',), ('anil',), ('anil32',), ('apple',), ('chan',), ('charitha',), 
# ('charitha1',), ('codecamp',), ('codecamp1',), ('codecamp11',), ('codecamp111',), 
# ('db_LibraryManagement',), ('harsha',), ('hemanth',), ('hlo',), ('hlo1',), ('indu',), 
# ('information_schema',), ('insta',), ('insta1',), ('instagram',), ('instagram user',), 
# ('ipl',), ('iqqq',), ('jack',), ('jack1',), ('joindelete',), ('joinsrecent',), 
# ('joinsrecent0',), ('joinsrecent1',), ('joinsrecent2',), ('keys1',), ('keys11',), 
# ('keyss',), ('LibraryManagement',), ('mysql',), ('performance_schema',), ('pilli',), 
# ('poli',), ('poli2',), ('pooja1',), ('pratice_joins',), ('pub',), ('puli0',), ('puli1',),
#  ('query',), ('rai',), ('rai22',), ('sai',), ('sales',), ('shiva',), ('sree',), ('store',),
#   ('sunil',), ('sys',), ('test',), ('users',), ('users200',), ('users20000',), ('users32',),
#    ('vijay',), ('vijay1',), ('warehouse',), ('yash',)]

import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mysql@123",
    database="instagram"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute SQL query
mycursor.execute("SHOW DATABASES")

# Fetch one row
result = mycursor.fetchall()

# Print the result
print(result)

# # Close cursor and connection
# # mycursor.close()
# # mydb.close()


# #positional Arguments
# def greet( greeting,name):
#     return f"{greeting}, {name}!"

# res=greet("anil","hi")
# print(res)

# #keyword arguemnts
# def greet( greeting,name):
#     return f"{greeting}, {name}!"

# res=greet(name="anil",greeting="hi")
# print(res)


def great(name,greeting="hello"):
    return f"{greeting},{name}"


res=great("anil")
res2=great("sunil")
print(res)
print(res2)

# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# greet("Alice")  # Output: "Hello, Alice!"

def multi_sum(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

multi_sum(1, 2, 3)  # Output: 6
print_info(name="Alice", age=30, city="New York")
