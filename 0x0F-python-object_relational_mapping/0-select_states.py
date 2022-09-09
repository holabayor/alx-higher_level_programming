#!/usr/bin/python3
# Script that list all states from database hbtn_0e_0_usa
import sys
import MySQLdb as mysql

def show(**args):
    db = mysql.connect(port=3306, **args)
    cursor = db.cursor()
    cursor.execute("SELECT id, \
        name FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    
    cursor.close()
    db.close()

if __name__ == __main__:
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    show(user, passwd, db)
