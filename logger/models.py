from logger import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(128))
    tmp = db.Column(db.String(10))
    datetime = db.Column(db.String(128))

    def __repr__(self):
        return 'location: {} time: {} temperature: {}'.format(self.location, self.time, self.tmp)
