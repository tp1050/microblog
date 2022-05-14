from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<Name: {self.username}"

    def is_active(self):
        return True

    def is_authenticated(self):
        return False

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    post=db.relationship('Post',backref='author',lazy='dynamic',)

class Top_model(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    ganush=db.Column(db.String(64), index=True, unique=True)

class U2(Top_model):
    gijooo=db.Column(db.String(65),default="Zoootal")


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
class meals(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
