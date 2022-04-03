import sqlite3

def dict_factory(cursor, row):
    dict = {}
    for idx, col in enumerate(cursor.description):
        dict[col[0]] = row[idx]
    return dict


class HardwareDatabase():
    def __init__(self):
        self.con = sqlite3.connect('database/RollsignDB.db', check_same_thread=False)
        self.con.row_factory = dict_factory
        self.cur = self.con.cursor()
    

    def GetHardwareData(self):
        self.cur.execute('SELECT * FROM "HardwareData" WHERE "_rowid_"=1')
        return self.cur.fetchone()