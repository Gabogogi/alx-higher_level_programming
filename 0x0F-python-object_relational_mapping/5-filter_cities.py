#!/usr/bin/python3
'''
name of a state as an argument and lists
all cities of that state
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
    state_name = sys.argv[4]

    


    db = MySQLdb.connect(user=username, password=password, database=db_name)

    
    cursor = db.cursor()
    #get state id
    state_id_query = "SELECT id FROM states WHERE name = %s"
    cursor.execute(state_id_query, (state_name,))
    state_id_result = cursor.fetchone()
    state_id = state_id_result[0]

    cities_query = "SELECT name FROM cities WHERE state_id = %s"
    cursor.execute(cities_query, (state_id,))

    cities = cursor.fetchall()
    for i in cities:
        print(i)
 
    cursor.close()
    db.close()
