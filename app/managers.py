import sqlite3

from app.models import Actor


class ActorManager():
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)

    def all(self):
        db_cursor = self.conn.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [
            Actor(id=db_row[0], first_name=db_row[1], last_name=db_row[2])
            for db_row in db_cursor
        ]

    def delete(self, pk: int):
        db_cursor = self.conn.execute(
            f"DELETE * FROM {self.table_name}"
            f"WHERE id = {pk}"
        )

        self.conn.commit()

    def create(self, first_name: str, last_name: str):
        db_cursor = self.conn.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)"
        )

        self.conn.commit()

    def update(self, pk: int, first_name: str, last_name: str):
        db_cursor = self.conn.execute(
            f"UPDATE {self.table_name}"
            f" SET  = {first_name}"
            f"WHERE id = {pk}"
        )