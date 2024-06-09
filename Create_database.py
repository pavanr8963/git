import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root"
)

c = mydb.cursor()
c.execute("CREATE DATABASE Rental_Management_System")