import w1thermsensor

from logger import db
from logger.models import Temperature
from sqlalchemy import desc

def get_temperature():
    sensor = w1thermsensor.W1ThermSensor()
    temperature = sensor.get_temperature()
    try:
        print(temperature)
        x = Temperature(location='kitchen', tmp=temperature)
        db.session.add(x)
        db.session.commit()
    except:
        pass
    finally:
        pass