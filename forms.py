from flask_wtf import Form as _Form
from wtforms import *
from wtforms.fields.html5 import *
from wtforms.widgets.html5 import *
#from flask.ext.wtf.html5 import NumberInput,TelField
class LoginForm(_Form):
	name=TextField("Name",[validators.Required("Plese Enter Your Name!!")])
	enrollment=IntegerField("Enrollment Number",[validators.Required("Please enter your enrollment number!!")],widget=NumberInput())
	phone=TelField("Your Contact Number please!",[validators.Required("Please enter your phone number")])
	username=TextField("Choose Username",[validators.Required("Plese Enter Your Username!!")])
	password=PasswordField("Chosse a password",[validators.Required("Plese Enter Your Password!!")])
	submit=SubmitField("Submit")
