import w1thermsensor

import sqlite3

def get_temperature():
    sensor = w1thermsensor.W1ThermSensor()
    temperature = sensor.get_temperature()
    try:
        print(temperature)
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("INSERT INTO temperature (location, tmp) VALUES ('kitchen', ?)", temperature)
    except Exception as err:
        print(err)
    finally:
        conn.close()