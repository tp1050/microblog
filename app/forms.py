from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired

from wtforms.fields import DateField



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


class Kooft(FlaskForm):
    user_name = StringField(label='User Name', validators=[DataRequired()], description="User Name of the Koofter",id = "user_name", default="Zortom", name='User_Name')
    food_item = StringField(label='food_item', validators=[DataRequired()], filters=(), description="Food Item being Koofted", id='food_item', default="Kooft", name='food_item')
    calories=StringField(label='Calories', description="Calories", id='calories', default="0", name='calories')
    time_koofted= DateField(id='datepick',label='datepick',name='datepick',description='pick a date!')
    submit = SubmitField('Submit')
def html(self):
    _html=""
    _html=''' {{form.user_name.lable}} {{form.user_name()}} {{form.hidden_tag()}}
    {{form.food_item.label}} {{form.food_item()}} {{form.hidden_tag()}}
    {{form.calories.label}} {{form.calories()}} {{form.hidden_tag()}}
    {{form.time_koofted.label}}  {{form.time_koofted(class='datepicker')}} {{form.hidden_tag()}}
    {{form.submit()}}'''
    return _html
