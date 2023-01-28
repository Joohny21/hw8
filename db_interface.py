import sqlite3
from queries import queries


def execute_query(sql: str) -> list:
    with sqlite3.connect('education.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


def get_response():
    with open("hw.sql", "r") as f:
        new = f.read()
        new = new.split(';')
        for each in queries:
            print(execute_query(each))


if __name__ == '__main__':
    get_response()
