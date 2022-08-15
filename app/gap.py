from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField, StringField
from wtforms.fields import DateField
from flask_admin.form.fields import DateTimeField
from datetime import date

from flask import render_template
from flask import request
from flask import json
from flask import jsonify

app = Flask(__name__)
from forms import *
app.config['SECRET_KEY'] = '#$%^&*'

class InfoForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d',default=date.today)
    enddate = DateField('End Date', format='%Y-%m-%d', default=date(2000,11,9))
    user_name=StringField(label='User_Name', description="User_Name", id='User_Name',name='User_Name')
    submit = SubmitField('Submit')

@app.route('/echoJSON', methods=['POST','GET'])
def echoJSON():
    if request.method=='POST':
        if request.form:
            _html=f'<html><body>{json.dumps(request.form.to_dict())}</body></html>'
            return _html
        data = request.json
        return jsonify(data)
    else:
        return "{}"#Inventory
# @app.route('/echoForm',methods=['POST'])
# def echoForm():
#    if request.method == 'POST':
#        result = request.form
#        if form.validate_on_submit():
#            return render_template("form_data.html",result = result)
#     pass



@app.route('/qrs',methods=['GET','POST'])
def qr():
    import glob
    qrlist=glob.glob('*.jpg')
    return f""

@app.route('/qrSHOW',methods=['GET','POST'])
def qrSHOW():
    from flask import send_file
    import pathlib
    p=pathlib.Path().resolve()

    qrlist=list(p.glob('*.jpg'))
    return send_file(qrlist[0])




@app.route('/', methods=['GET','POST'])
def index():
    form = Kooft()
    if form.validate_on_submit():
        # session['startdate'] = form.startdate.data
        # session['enddate'] = form.enddate.data
        return redirect('echoJSON')
    return render_template('index.html', form=form)

@app.route('/date', methods=['GET','POST'])
def date():
    startdate = session['startdate']
    enddate = session['enddate']
    return render_template('date.html')


app.run(debug=True)
