#!/usr/bin/python3
""" A module that lists all states from
the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database, port=3306)
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states")

    myrows = mycursor.fetchall()

    for records in myrows:
        print(records)

    mycursor.close()
    db.close()
