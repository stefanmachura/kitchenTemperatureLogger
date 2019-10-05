import w1thermsensor

import sqlite3
import datetime

def get_temperature():
    sensor = w1thermsensor.W1ThermSensor()
    temperature = sensor.get_temperature()
    try:
        print(temperature)
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("INSERT INTO temperature (location, tmp, timestamp) VALUES ('kitchen', ?, ?)", (str(temperature), datetime.datetime.utcnow()) )
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close()

get_temperature()