# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing
import os
import json
import datetime
import random
import time
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from flask import Flask, request, render_template


app = Flask(__name__)
dbname = 'database.db'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/public')
def publish():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            with closing(sqlite3.connect(dbname)) as conn:
                c = conn.cursor()

                #select_sql = 'select * from sensor order by time desc limit 10'
                select_sql = 'select * from sensor order by time desc limit 1'
                for row in c.execute(select_sql):
                    ws.send(json.dumps([[{"time": row[1], "y": row[2]}],
                                        [{"time": row[1], "y": row[3]},
                                         {"time": row[1], "y": row[4]},
                                         {"time": row[1], "y": row[5]}],
                                        [{"time": row[1], "y": row[6]},
                                         {"time": row[1], "y": row[7]},
                                         {"time": row[1], "y": row[8]}],
                                        [{"time": row[1], "y": row[9]},
                                         {"time": row[1], "y": row[10]},
                                         {"time": row[1], "y": row[11]}]]))
                    # print(row)
                conn.close()
            time.sleep(1)
    return


if __name__ == '__main__':
    #app.debug = True
    server = pywsgi.WSGIServer(("0.0.0.0", 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()
