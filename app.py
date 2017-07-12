import sqlite3 as sql
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from forms import *


appy=Flask(__name__)



def insertData(form,u_pass):
	if(u_pass=="student"):
	    con=sql.connect("student_database.db")
	    cur=con.cursor()
	    a=form.enrollment.data
	    un=form.username.data
	    co=cur.execute("select count(*) from login_data where enrollment=?",(a,))
	    co2=con.execute("select count(*) from login_data where username=?",(un,))
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
	    	cur.execute("insert into user_data(enrollment,name,phone,user_pass)values(?,?,?,?) ",(int(a),str(d),int(e),u_pass) )
	    	print("Data inserted into user_data successfully!!")
	    	con.commit()
	    	con.close()
	    	return render_template('index.html')

	elif(u_pass=="faculty"):
		con=sql.connect('faculty_database.db')
		cur=con.cursor()
		a=form.username.data
		b=form.password.data
		c=form.name.data
		d=form.phone.data
		co2=cur.execute("select count(*) from login_data where username=?",(a,))
		if ( (co2.fetchall())[0][0]!=0):
			return redirect('/admin?'+"msg=Credentials Pre-Exist")

		else:
			cur.execute("insert into login_data(username,password)values(?,?)",(str(a),str(b)))
			print ("Data inserted into login_data successfully!!")
			cur.execute("insert into user_data(name,phone,user_pass)values(?,?,?) ",(str(c),int(d),u_pass) )
			print ("Data inserted into user_data successfully!!")
			con.commit()
			con.close()
			return redirect("/admin?"+"msg=Faculty SignedUp Successfully!!")





#Student User Code Start
def do_login(form):
	user=form.uname.data
	pa=form.pw.data
	con=sql.connect('student_database.db')
	cur=con.cursor();
	count=cur.execute('select count(*) as count from login_data where username=? and password=? ',(user,pa,)  )
	n=(count.fetchall())[0][0]
	if (n==1):
		session['logged_in']=True
		r=((cur.execute('select enrollment from login_data where username=? and password=? ',(user,pa,)  )).fetchall())[0][0]
		result=(con.execute("select name, user_pass from user_data where enrollment=?",(r,)).fetchall())[0]
		session['login_user']=result[0]
		session['login_pass']=result[1]
		return redirect('/')
	else:
		con=sql.connect('faculty_database.db')
		cur=con.cursor()
		count=cur.execute('select count(*) as count from login_data where username=? and password=? ',(user,pa,)  )
		n=(count.fetchall())[0][0]
		if (n==1):
			session['logged_in']=True
			r=((cur.execute('select id from login_data where username=? and password=? ',(user,pa,)  )).fetchall())[0][0]
			result=(con.execute("select name, user_pass from user_data where id=?",(r,)).fetchall())[0]
			session['login_user']=result[0]
			session['login_pass']=result[1]
			return redirect('/')

		else:
			return render_template('login.html',form=form,msg="Invalid Credentials")

def do_logout():
	form=LoginForm()
	session['logged_in']=False
	session['login_user']=""
	return redirect("/login?"+"msg=You have logged out")

#Student User Code End



#Admin User Code Start

def do_admin_login(form):
	user=form.uname.data
	pa=form.pw.data
	if((user=="Prashasy") and (pa=="admin")):
		session['logged_in']=True
		session['login_user']="Admin"
		session['login_pass']="admin"
		return redirect('/admin')

	return render_template('admin_login.html',form=form,msg="Invalid Credentials")

#Admin User Code Stop



#Faculty User Code Start



#Faculty User Code Stop

    
	



@appy.route('/',methods=['GET','POST'])
def home():
	if ((session.get('logged_in'))):
		if(session.get('login_pass')):
			if(session['login_pass']=="admin"):
				return redirect('/admin')
			else:
				return render_template('dashboard.html')


	else:
		return render_template('index.html',title="Home")



@appy.route('/<username>')
def profile(username):
		if():
			return "<h1>Welcome {} !!</h1>".format(uname)



@appy.route('/register',methods=['GET','POST'])
def register():
	if(session.get('logged_in')):
		return redirect('/')
	form=SignUpForm(request.form)
	if(request.method=='POST'):
		if(form.validate_on_submit()==False):
			return render_template('register.html',form=form)
		else:
			 return insertData(form,"student")
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
		m=request.args.get("msg")  #YOU HAVE LOGGED OUT MESSAGE
		if (m is None):
			return render_template('login.html',form=form)
		else:
			return render_template('login.html',form=form,msg=m)

@appy.route('/logout')
def logout():
	if(session.get('logged_in')):
		return do_logout() 
	else:
		return redirect('/')

@appy.route('/admin_login',methods=['GET','POST'])
def admin_login():
	if(session.get('logged_in')):
		return redirect('/')

	form=LoginForm(request.form)
	if(request.method=='POST'):
		if(form.validate_on_submit()==False):
			return render_template('admin_login.html',form=form)
		else:
			return do_admin_login(form)
	elif(request.method=='GET'):
			return render_template('admin_login.html',form=form)


@appy.route('/admin',methods=['GET','POST'])  #ADMIN DASHBOARD
def admin():
	if ((session.get('logged_in'))):
		if(session['login_pass']=="student"):
			return render_template('dashboard.html',session)


	else:
		return render_template('index.html',title="Home")

	form=faculty_signup_form(request.form)
	if(request.method=='GET'):
		m=request.args.get('msg')
		if(m is None):
			return render_template('admin.html',form=form)
		else:
			return render_template('admin.html',form=form,msg=m)
	elif(request.method=='POST'):
		if(form.validate_on_submit()==False):
			return render_template('admin.html',form=form)
		else:
			return insertData(form,"faculty")








if(__name__=='__main__'):
	appy.secret_key="Hi"
	appy.run(debug=True)






	