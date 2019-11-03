import w1thermsensor
import RPi.GPIO as GPIO
import time

import sqlite3
import datetime


def get_temperature():
    sensor = w1thermsensor.W1ThermSensor()
    temperature = sensor.get_temperature()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    try:
        print(temperature)
        conn = sqlite3.connect('/home/pi/python_projects/kitchenTemperatureLogger/app.db')
        c = conn.cursor()
        c.execute("""INSERT INTO temperature (location, tmp, timestamp)
                     VALUES ('kitchen', ?, ?)""", (str(temperature), datetime.datetime.utcnow()))
        conn.commit()
        GPIO.output(21, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(21, GPIO.LOW)
    except Exception as err:
        print(err)
    finally:
        conn.close()
        GPIO.cleanup()


get_temperature()
