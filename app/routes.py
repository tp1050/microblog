from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="doolsaz",user={'name':'ffff'})

@app.route('/golabi')
def golabi():
    return "<html> <td>Glabi<td></html>"
