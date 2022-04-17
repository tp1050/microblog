from app import app
from app import logs
from flask import render_template
from flask import request
from flask import json
from forms import ADDInv
from werkzeug.exceptions import HTTPException


#Defining default for route leads to closed routing system
# and allows for totall control of incoming requests.
@app.route('/', defaults={'path': ''},methods=['POST','GET'])
@app.route('/<path:path>')
def default(path):
    return f"{path} is kosher"



@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.before_request()
def before():
    print(request.form)



@app.route('/')
@app.route('/index')
def index():
    ip = 'Unknown Visitor'
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    logs.append(ip)
    return render_template("index.html", title=str(logs),user={'name':ip},ip=ip)

@app.route('/addProduct')
def addProducts():
    return render_template("index.html",title="add your product",form=ADDInv(),user="doolsaz")

@app.route('/anbar')
def anbar():
    return "<html> <td>Glabi<td></html>"
