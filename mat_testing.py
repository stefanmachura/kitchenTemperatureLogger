import sqlite3
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import os

from datetime import datetime
import sys


conn = sqlite3.connect('app.db')
c = conn.cursor()

how_many = 60 if len(sys.argv) == 1 else sys.argv[1]
data = []
time = []
for row in c.execute('SELECT * FROM temperature ORDER BY timestamp DESC LIMIT ?', (how_many, )):
    data.append(float(row[2]))
    tm = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
    time.append(tm)

print(data)

fig, ax = plt.subplots()
ax.plot(time, data)

myFmt = DateFormatter("%H:%M")
ax.xaxis.set_major_formatter(myFmt)


fig.autofmt_xdate()

basedir = os.path.abspath(os.path.dirname(__file__))
fname = os.path.join(basedir, 'logger', 'static', 'plot.png')
plt.savefig(fname)

conn.close()
