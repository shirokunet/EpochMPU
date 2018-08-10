# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing

dbname = 'database.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    select_sql = 'select * from sensor'
    for row in c.execute(select_sql):
        print(row)

    conn.close()
