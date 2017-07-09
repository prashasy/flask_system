import sqlite3 as sql


con=sql.connect('database.db')
print ("Database Created Successfully!!")
cur=con.cursor()
cur.execute("create table login_data (enrollment numeric,username text,password text)")
print("Table login_data created successfully!!")
cur.execute("create table user_data (enrollment numeric,name text, phone numeric )")
print("Table user_data created successfulyy!!")
con.close()
print("All operations done Successfully!!")
