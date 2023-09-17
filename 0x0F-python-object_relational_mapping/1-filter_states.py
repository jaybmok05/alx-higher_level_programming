#!/usr/bin/python3
import MySQLdb
from sys import argv

'''
a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
'''


if __name__ == "__main__":

    connect_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3])

    cursor = connect_db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name
                LIKE BINARY '%N%' ORDER BY states.id""")
    data_retrieved = cursor.fetchall()

    for states in data_retrieved:
        print(states)
    cursor.close()
    connect_db.close()
