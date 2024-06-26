import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="college"
)

if mydb.is_connected():
    print("Connected to MySQL database")

mycursor = mydb.cursor(dictionary=True)
myquery = "SELECT * FROM student"
mycursor.execute(myquery)
result = mycursor.fetchall()
for row in result:
    print(row)
# print(result)

mydb.close()
