#!/usr/bin/python3
from sys import argv

import MySQLdb


def main():
    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    ) as connexion:
        with connexion.cursor() as cur:
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            for row in cur.fetchall():
                print(row)


if __name__ == "__main__":
    main()
