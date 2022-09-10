#!/usr/bin/python3
""" Script that list all states from database hbtn_0e_0_usa
    that matches the input state
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                    WHERE BINARY name = '%s'\
                    ORDER BY id ASC" % sys.argv[4])

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
