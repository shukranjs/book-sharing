from run import db


class User(db.Model):
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, auto_now_add=True)
