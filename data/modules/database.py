import sqlite3


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("data/database/database.db")

    @staticmethod
    def get_data(price=False, table=None):
        con = sqlite3.connect("data/database/database.db")
        cur = con.cursor()

        if price:
            sql = """SELECT price FROM lives WHERE id = 0"""
            live = cur.execute(sql).fetchone()[0]
            sql = """SELECT price FROM speed WHERE id = 0"""
            speed = cur.execute(sql).fetchone()[0]

            con.close()

            return live, speed

        else:
            res = cur.execute(f"""SELECT value FROM {table} WHERE id = 0""").fetchone()[0]

            con.close()

            return res

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

    def buy_item(self, table, price):
        cur = self.con.cursor()
        sql = f"""UPDATE {table} SET 'value' = value + 1 WHERE id = 0"""
        cur.execute(sql)
        sql = f"""UPDATE balance SET 'value' = value - {price} WHERE id = 0"""
        cur.execute(sql)

        # делаем дороже на 100 рыбок
        cur.execute(f"""UPDATE {table} SET 'price' = price + 100 WHERE id = 0""")

        self.con.commit()
        cur.close()

    def terminate(self):
        self.con.close()
