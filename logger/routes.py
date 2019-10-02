from flask import render_template
from logger import app, db
from logger.models import Temperature
import random


@app.route('/')
@app.route('/index')
def index():
    temp = str(random.randrange(1000) / 100)
    x = Temperature(location='kitchen', tmp=temp)
    db.session.add(x)
    db.session.commit()



    user = {'username': 'Miguel'}
    t = Temperature.query.all()
    data = {'temperatures': t}
    return render_template('index.html', user=user, data=data)
