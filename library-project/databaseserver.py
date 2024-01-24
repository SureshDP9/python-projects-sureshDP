import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()


def createDb():
    cursor.execute(
        "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


def addData(id,title,author,rating):
    cursor.execute(f"INSERT INTO books VALUES({id}, {title}, {author}, {rating})")
    db.commit()


# createDb()
