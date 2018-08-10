# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing
import time
import random
import datetime


dbname = 'database.db'
i = 0

while True:
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        sql = '''insert into sensor (id,
                                     time,
                                     temp,
                                     accel_x,
                                     accel_y,
                                     accel_z,
                                     gyro_x,
                                     gyro_y,
                                     gyro_z,
                                     mag_x,
                                     mag_y,
                                     mag_z) values (?,?,?,?,?,?,?,?,?,?,?,?)'''
        sensor = (i,
                  int(time.mktime(datetime.datetime.now().timetuple())),
                  int(random.random() * 1000),
                  random.random() * 1000,
                  random.random() * 1000,
                  random.random() * 1000,
                  random.random() * 1000,
                  random.random() * 1000,
                  random.random() * 1000,
                  random.random() * 1000,
                  random.random() * 1000,
                  random.random() * 1000)
        c.execute(sql, sensor)
        conn.commit()

        print(sensor)
        time.sleep(1)
        i += 1

        conn.close()
