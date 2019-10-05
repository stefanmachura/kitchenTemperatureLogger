import w1thermsensor

def get_temperature():
    sensor = w1thermsensor.W1ThermSensor()
    temperature = sensor.get_temperature()
    try:
        print(temperature)
    except:
        pass
    finally:
        pass