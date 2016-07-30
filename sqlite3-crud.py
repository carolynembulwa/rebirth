#!/usr/bin/python3
# CRUD
import sqlite3

def insert(db, row):
	db.execute("insert into test (t1 , i1) values (? ,? ) , (row['t1'], row['i1'])")
	db.commit()

def retrieve(db, t1):
	cursor = db.execute("select * from test where t1 = ? ", (t1,))
	return cursor.fetchone(())

def update(db , row):
	db.execute('update test i1 = ? where t1 =? ', row['i1']) , row['t1']
	pass
def main():
	print("This is a syntax.py file")


if __name__ == "__main__": main()