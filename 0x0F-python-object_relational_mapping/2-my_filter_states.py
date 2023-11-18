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
    db_name = sys.argv[3]
    name = sys.argv[4]

    


    connection = MySQLdb.connect(user=username, password=password, database=db_name)
    cursor = connection.cursor()
    
    state_name = "SELECT * FROM states LIKE BINARY '{}'".format(name)
    cursor.execute(state_name)
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()

   

