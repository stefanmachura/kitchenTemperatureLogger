import sqlite3
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import os

from datetime import datetime
import sys
import timeit


def generate_graph_from_db(days):
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    how_many = 60 if len(sys.argv) == 1 else sys.argv[1]
    data = []
    time = []
    for row in c.execute("SELECT * FROM temperature WHERE timestamp > DATETIME('now', ?) ORDER BY timestamp", (days, )):
        data.append(float(row[2]))
        tm = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
        time.append(tm)

    fig, ax = plt.subplots()
    ax.plot(time, data)

    plt.xticks([time[0], time[-1]], visible=True, rotation="horizontal")

    basedir = os.path.abspath(os.path.dirname(__file__))

    fname = days.replace('-', '').replace(' ', '') + '.png'
    plot_file = os.path.join(basedir, 'logger', 'static', fname)
    plt.savefig(plot_file)

    conn.close()


generate_graph_from_db('-1 day')
generate_graph_from_db('-3 days')
generate_graph_from_db('-10 days')
