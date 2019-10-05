from flask import render_template
from logger import app, db
from logger.models import Temperature
import random
from sqlalchemy import desc

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Antonio'}
    t = Temperature.query.order_by(desc(Temperature.timestamp)).limit(20).all()

    data = {'temperatures': t}
    return render_template('index.html', user=user, data=data)
