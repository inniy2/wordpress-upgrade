#!/usr/bin/python

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="bae",
  database="test_database"
)

mycursor = mydb.cursor()

mycursor.execute("show tables")

myresult = mycursor.fetchall()

for row in myresult:
  table = row[0]
  mycursor = mydb.cursor()
  print("altering "+table)
  mycursor.execute("alter table "+table+" engine=InnoDB")

