# kitchenTemperatureLogger
This is a script for Rapsberry Pi that measures the  external temperature and saves it to a SQLite database. A Flask-based web interface is also provided to present the measurements and plot them using matplotlib.

Requirements:
Raspberry Pi (tested on Zero W)
DS18B20 thermometer
green LED to highlight saving to db.

To make it run in the background, measure.py and plot.py need to be added to the cron tasklist. Remember to update measure.py with your own LED GPIO pin numbers!
