from flask_wtf import Form as _Form
from wtforms import *
from wtforms.fields.html5 import *
from wtforms.widgets.html5 import *
#from flask.ext.wtf.html5 import NumberInput,TelField
class SignUpForm(_Form):
	name=TextField("Name",[validators.Required("Plese Enter Your Name!!")])
	enrollment=IntegerField("Enrollment Number",[validators.Required("Please enter your enrollment number!!")],widget=NumberInput())
	phone=TelField("Your Contact Number please!",[validators.Required("Please enter your phone number")])
	username=TextField("Choose Username",[validators.Required("Plese Enter Your Username!!")])
	password=PasswordField("Chosse a password",[validators.Required("Plese Enter Your Password!!")])
	submit=SubmitField("Submit")


class LoginForm(_Form):
	uname=TextField("User-Name",[validators.Required("Plese Enter Your User-Name!!")])
	pw=PasswordField("Your Password",[validators.Required("Plese Enter Your Password!!")])
	submit=SubmitField("Login")


class faculty_signup_form(_Form):
	username=TextField("Choose Username",[validators.Required("Plese Enter Your Username!!")])
	password=PasswordField("Chosse a password",[validators.Required("Plese Enter Your Password!!")])
	name=TextField("Name",[validators.Required("Plese Enter Your Name!!")])
	phone=TelField("Your Contact Number please!",[validators.Required("Please enter your phone number")])
	submit=SubmitField("Submit")


class Leave_Request_Form(_Form):
	enrollment=IntegerField("Enrollment Number",[validators.Required("Please enter your enrollment number!!")],widget=NumberInput())
	leave_start=DateField("Leave From:",[validators.Required("Please enter the date!!")])
	leave_end=DateField("Leave Till:",[validators.Required("Please enter the date!!")])
	reason=TextField("Reason for Leave:",[validators.Required("Please tell us a reason for your leave")])
	address=TextField("Adress while on Leave:",[validators.Required("Please tell us your address while at leave")])
	submit=SubmitField("Submit")	

class Query_Form(_Form):
	enrollment=IntegerField("Enrollment Number",[validators.Required("Please enter your enrollment number!!")],widget=NumberInput())
	submit=SubmitField("Submit")
	




