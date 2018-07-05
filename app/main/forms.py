from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    #Make the user an opurtuinity to chose a UserName along with the Chatroom 
    name = StringField('Name', validators=[Required()])
    room = StringField('Room', validators=[Required()])
    submit = SubmitField('Enter Chatroom')
