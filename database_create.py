# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing


dbname = 'database.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    # delete old one
    drop_table = '''drop table if exists sensor'''
    conn.execute(drop_table)

    # create new one
    create_table = '''create table sensor (id int,
                                           time varchar(64),
                                           temp int,
                                           accel_x double,
                                           accel_y double,
                                           accel_z double,
                                           gyro_x double,
                                           gyro_y double,
                                           gyro_z double,
                                           mag_x double,
                                           mag_y double,
                                           mag_z double)'''
    c.execute(create_table)
    conn.close()
