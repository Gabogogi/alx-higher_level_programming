#!/usr/bin/python3
'''
takes in an argument and displays all values in the states
'''
import MySQLdb
import sys


if __name__ =="__main__":
    if len(sys.argv) != 5:
        print("Usage: <username> <password> <databaseName>")
        exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    


    db = MySQLdb.connect(user=username, password=password, database=db_name)

    
    cur = db.cursor()
    nmeSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4])
    cur.execute(nmeSr)

    rows = cur.fetchall()
    for i in rows:
        print(i)
 
    cur.close()
    db.close()

   

