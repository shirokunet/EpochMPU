# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing
import time
import FaBo9Axis_MPU9250
import random
import datetime


mpu9250 = FaBo9Axis_MPU9250.MPU9250()

dbname = 'database.db'
i = 0

while True:
    temp = mpu9250.readTemperature()
    accel = mpu9250.readAccel()
    gyro = mpu9250.readGyro()
    mag = mpu9250.readMagnet()

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
                  int(temp),
                  accel['x'],
                  accel['y'],
                  accel['z'],
                  gyro['x'],
                  gyro['y'],
                  gyro['z'],
                  mag['x'],
                  mag['y'],
                  mag['z'])
        c.execute(sql, sensor)
        conn.commit()

        print(sensor)
        time.sleep(1)
        i += 1

        conn.close()
