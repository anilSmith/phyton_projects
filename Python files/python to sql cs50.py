import mysql.connector
mydb=mysql.connector.connect(host ="localhost",user= "root",passwd="Mysql@123",database="instagram")
mycursor=mydb.cursor()
mycursor.execute("select * from customers")
result=mycursor.fetchall()
print(result)