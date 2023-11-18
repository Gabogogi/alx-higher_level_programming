#!/usr/bin/python3
'''
Gets all states in hbtn_0e_0_usa dtabase
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
    cursor.execute("SELECT * FROM states ORDER BY id")
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
   

