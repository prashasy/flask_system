import sqlite3 as sql
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from forms import *


appy=Flask(__name__)
appy.secret_key="Hi"


def insertData(form):
    con=sql.connect("database.db")
    cur=con.cursor()
    a=form.enrollment.data
    un=form.username.data
    co=cur.execute("select count(*) from login_data where enrollment=?",(a,))
    co2=cur.execute("select count(*) from login_data where username=?",(un,))
    if ((co.fetchall())[0][0]!=0 or (co2.fetchall())[0][0]!=0) :
	    return "ERROR"
	    return render_template('register.html',form=form)
    else:
    	b=form.username.data
    	c=form.password.data
    	d=form.name.data
    	e=form.phone.data
    	cur.execute("insert into login_data(enrollment,username,password)values(?,?,?)",(int(a),str(b),str(c)))
    	print("Data inserted into login_data successfully!!")
    	cur.execute("insert into user_data(enrollment,name,phone)values(?,?,?) ",(int(a),str(d),int(e)) )
    	print("Data inserted into user_data successfully!!")
    	con.commit()
    	return render_template('index.html')




def do_login(form):
	user=form.uname.data
	pa=form.pw.data
	con=sql.connect('database.db')
	cur=con.cursor();
	count=cur.execute('select count(*) as count from login_data where username=? and password=? ',(user,pa,)  )
	n=(count.fetchall())[0][0]
	if (n==1):
		session['logged_in']=True
		r=((cur.execute('select enrollment from login_data where username=? and password=? ',(user,pa,)  )).fetchall())[0][0]
		result=(con.execute("select name from user_data where enrollment=?",(r,)).fetchall())[0]
		session['login_user']=result[0]
		return redirect('/')
	else:
		return render_template('login.html',form=form,msg="Invalid Credentials")

def do_logout():
	form=LoginForm()
	session['logged_in']=False
	session['login_user']=""
	return render_template('login.html',form=form,msg="You have logged out")


    
	



@appy.route('/',methods=['GET','POST'])
def home():
	if ((session.get('logged_in'))):
		return render_template('index.html',user=session['login_user'])


	else:
		return render_template('index.html',title="Home")



@appy.route('/<username>')
def profile(username):
		if():
			return "<h1>Welcome {} !!</h1>".format(uname)



@appy.route('/register',methods=['GET','POST'])
def register():
	form=SignUpForm(request.form)
	if(request.method=='POST'):
		if(form.validate_on_submit()==False):
			return render_template('register.html',form=form)
		else:
			 return insertData(form)
	elif(request.method=="GET"):
		return render_template('register.html',form=form)


@appy.route('/login',methods=['GET','POST'])
def login():
	if(session.get('logged_in')):
		return redirect('/')
	form=LoginForm(request.form)
	if(request.method=='POST'):
		if(form.validate_on_submit()==False):
			return render_template('login.html',form=form)
		else:
			return do_login(form)
	elif(request.method=='GET'):
		return render_template('login.html',form=form)

@appy.route('/logout')
def logout():
	if(session.get('logged_in')):
		return do_logout() 
	else:
		return redirect('/')


if(__name__=='__main__'):
	appy.secret_key="Hi"
	appy.run(debug=True)






	