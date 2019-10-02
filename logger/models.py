from logger import db
from datetime import datetime


class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(128))
    tmp = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'location: {} time: {} temperature: {}'.format(self.location, self.timestamp, self.tmp)
