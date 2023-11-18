#!/usr/bin/python3
'''
takes in an argument and displays all values in the states
'''
import MySQLdb
import sys


if __name__ =="__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <databaseName>")
        exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    


    connection = MySQLdb.connect(user=username, password=password, database=name)
    cursor = connection.cursor()
    
    state_name = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4])
    cursor.execute(state_name)
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    connection.close()
   

