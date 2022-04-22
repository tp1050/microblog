from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class AddProduct(FlaskForm):
    productName=StringField(label='ProductName')
    price=StringField(label='price')
    datePurchased=StringField(label='datePurchased')
    submit=SubmitField(label='submit')

class ADDInv(FlaskForm):
    item_name=StringField(label="item_name",id="item_name")
    qty=StringField(label="qty",id="qty")
    description=StringField(label="description",id="description")
    submit=SubmitField(label='submit')

class upload(FlaskForm):
    file = FileField('uplod file')
    submit = SubmitField('Submit')
