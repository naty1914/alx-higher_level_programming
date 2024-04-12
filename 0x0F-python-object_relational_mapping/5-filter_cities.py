#!/usr/bin/python3
""" A module akes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    mycursor = db.cursor()
    sql_query = """ SELECT  cities.name \
                  FROM cities \
                  INNER JOIN states ON states.id=cities.state_id \
                  WHERE states.name =%s"""
    mycursor.execute(sql_query, (sys.argv[4],))

    sqlrows = mycursor.fetchall()

    records = [row[0] for row in sqlrows]
    print(', '.join(records))

    mycursor.close()
    db.close()
