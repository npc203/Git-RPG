import sqlite3
import os

"""Db structure:
   {
    user_name = ...
   file_path = ...
   level = {
       lvl_no: ["init","commit",....],
   }
"""

basepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "user.sqlite3")


class User:
    def __init__(self, path=None):
        """Takes a file-path"""
        if path is None:
            path = basepath
        self.db = sqlite3.connect(path)
        self.cursor = self.db.cursor()
        if (
            self.db.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='Users';"
            ).fetchone()
            == None
        ):
            self.cursor.execute(
                "create table if not exists Users (id integer primary key autoincrement, path text, level int, sublevel int)"
            )
            self.cursor.execute("insert into Users values (1,NULL,1,1)")
            self.db.commit()

    def update(self, item: dict):
        if len(item) > 1:
            safe_text = ", ".join(f"{i} = ?" for i in item.keys())
        else:
            safe_text = " ".join(f"{i} = ?" for i in item.keys())
        res = self.cursor.execute(f"update Users set {safe_text} where id=1", tuple(item.values()))
        self.db.commit()
        return res

    def get(self, item):
        res = self.cursor.execute(f"select {item} from Users where id=1").fetchone()
        if len(res) > 1:
            return res
        else:
            return res[0]

