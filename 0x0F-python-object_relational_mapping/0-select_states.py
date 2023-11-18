#!/usr/bin/env python
import MySQLdb
import sys


def list_states(username, password, database):
    '''
    Connect to the MySQL server
    '''
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db = database
    )

    cursor = connection.cursor()

    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    if connection:
        connection.close()


if __name__ =="__main__":
    if len(sys.argv) != 4:
        print("Us: py script.py <username> <password> <name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)