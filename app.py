import sqlite3 as sql
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from forms import LoginForm


appy=Flask(__name__)
appy.secret_key="Hi"


def insertData(form):
    con=sql.connect("database.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    
	



@appy.route('/',methods=['GET','POST'])
def home():
	if ((session.get('logged_in'))):
		return "Hello!!"


	else:
		form = LoginForm()
		return render_template('login.html', 
		                       title='Sign In',
		                       form=form)



@appy.route('/<username>')
def profile(username):
		if():
			return "<h1>Welcome {} !!</h1>".format(uname)



@appy.route('/register',methods=['GET','POST'])
def register():
	form=LoginForm(request.form)
	if(request.method=='POST'):
		if(form.validate_on_submit()==False):
			print (form.errors)
			return render_template('register.html',form=form)
		else:
			return insertData(form)
	elif(request.method=="GET"):
		return render_template('register.html',form=form)
if(__name__=='__main__'):
	appy.secret_key="Hi"
	appy.run(debug=True)






	