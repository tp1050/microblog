import pathlib
class Conf(object):
    SECRET_KEY = "22111357"
    UPLOAD_FOLDER='/img'
    instance_relative_config=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
