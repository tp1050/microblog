from app import db

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
