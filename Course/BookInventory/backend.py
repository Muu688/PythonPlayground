import sqlite3

from h11 import Data

class Database: # The self parameter is required for functions of a class. 
    def __init__(self, db): #__init__ is a python keyword to tell it to run this when an instance of the class is created
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id,title="", author="", year="", isbn=""):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close
        
    # update(4, "title", "author", 1996, 922102)
    # insert("Book Title", "Jimi", 2022, 99221102)
    # print(view())

# db = Database()
# print(db.view())