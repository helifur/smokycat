import sqlite3


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("data/database/database.db")

    def insert_rating(self, value):
        cur = self.con.cursor()
        sql = f"""INSERT INTO rating VALUES (0, {value}) WHERE id = 0"""
        cur.execute(sql)
        self.con.commit()
        cur.close()

    def update_balance(self, val):
        cur = self.con.cursor()
        sql = f"""UPDATE balance SET 'value' = value + {val} WHERE id = 0"""
        cur.execute(sql)
        self.con.commit()
        cur.close()

    def get_balance(self):
        cur = self.con.cursor()
        sql = """SELECT value FROM balance WHERE id = 0"""
        return cur.execute(sql).fetchone()[0]

    def terminate(self):
        self.con.close()
