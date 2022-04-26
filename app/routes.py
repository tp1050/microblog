from constructs import file_cats
import os.path
from app import app
from app import Inventory
from flask import jsonify
from app import logs
from flask import render_template
from flask import request
from flask import json
from forms import ADDInv
from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename
from pathlib import Path





#Defining default for route leads to closed routing system
# and allows for totall control of incoming requests.
# @app.route('/', defaults={'path': ''},methods=['POST','GET'])
# @app.route('/<path:path>')
# def default(path):
#     return f"{path} is kosher"



# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     return response
# #
# #
# # @app.before_request()
# # def before_request():
# #     print(request.form)

# @app.before_request
# def before_request():
#     print('before')
#     # print(request.get_data())
#     print('beforish')

@app.route('/echoJSON', methods=['POST','GET'])
def echoJSON():
    if request.method=='POST':
        data = request.json
        return jsonify(data)
    else:
        return Inventory

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    ip = 'Unknown Visitor'
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    logs.append(ip)
    print('index')
    print(request.environ.items())
    print('indexed')
    return render_template("index.html", title=str(logs),user={'name':ip},ip=ip)

@app.route('/addProduct')
def addProducts():
    return render_template("index.html",title="add your product",form=ADDInv(),user="doolsaz")

@app.route('/anbar')
def anbar():
    return "<html> <td>Glabi<td></html>"

@app.route('/test')
def test():
    return render_template("basePage.html")
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():

    if request.method == 'POST':
        f = request.files['file']
        f_name = secure_filename(f.filename)
        suff=Path(f_name).suffix
        print(suff)
        directory=file_cats.File_Cat.get(suff[1:],'.misc')
        print(directory)

        if Path(os.path.join(app.instance_path, directory, f_name )).is_file():
            return render_template('upload.html',message='file already exists')
        else:
            f.save(Path(os.path.join(app.instance_path, directory, f_name )))
        return render_template('upload.html',message='file uploaded successfully')
    else:
        return render_template('upload.html')
