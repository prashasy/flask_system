import sqlite3 as sql

print("STUDENT DATABASE!!")
con=sql.connect('student_database.db')
print ("Database Created Successfully!!")
cur=con.cursor()
cur.execute("create table login_data (enrollment numeric,username text,password text)")
print("Table login_data created successfully!!")
cur.execute("create table user_data (enrollment numeric,name text, phone numeric, user_pass text )")
print("Table user_data created successfulyy!!")
print("All operations done Successfully!!")

print("FACULTY DATABASE!!")
con=sql.connect('faculty_database.db')
print ("Database Created Successfully!!")
cur=con.cursor()
cur.execute("create table login_data (id integer primary key,username text,password text)")
print("Table login_data created successfully!!")
cur.execute("create table user_data (id integer primary key, name text, phone numeric, user_pass text )")
print("Table user_data crea    ted successfulyy!!")
con.commit()
print("All operations done Successfully!!")


con=sql.connect('leave_requests.db',detect_types=sql.PARSE_DECLTYPES)
cur=con.cursor()
cur.execute('create table requests(serial integer primary key,enrollment integer,request_stamp timestamp,leave_start date, leave_end date, reason_for_leave text, address_on_leave text, approval text )  ')
print ("Table requests created Successfully")
con.commit()
print("All operations done Successfully!!")


con.close()
