import sqlite3

DATABASE='database.db'

def create_books_table():
  con=sqlite3.connect(DATABASE)
  con.execute("create table if not exists books(title,price,arrival_day)")
  con.close()
  