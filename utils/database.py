import sqlite3


def create_book_table():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text PRIMARY KEY, author text, read number) ")

    con.commit()
    con.close()

def add_book(name,author):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("insert into books values(?,?,0)",(name,author))

    con.commit()
    con.close()

def get_all_books():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM BOOKS")
    books = [{'name': row[0], "author": row[1], "read":row[2]} for row in cursor.fetchall()]

    con.close()
    return books

def mark_book_as_read(name):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("UPDATE books SET read=1 WHERE name=?",(name,))

    con.commit()
    con.close()

def delete_book(name):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()

    cursor.execute("DELETE FROM books WHERE name=?",(name,))

    con.commit()
    con.close()






