#!/usr/bin/python
# encoding: utf-8

import os
import sqlite3
import webbrowser


path = os.environ['WURMPW_LOCATION']

conn = sqlite3.connect(path + 'wurm.sqlite')
c = conn.cursor()

adjektiv = c.execute('''
SELECT * FROM ADJEKTIV ORDER BY RANDOM() LIMIT 1;
''').fetchall()
subjekt = c.execute('''
SELECT * FROM TIER ORDER BY RANDOM() LIMIT 1;
''').fetchall()
praedikat = c.execute('''
SELECT * FROM VERB ORDER BY RANDOM() LIMIT 1;
''').fetchall()
objekt = c.execute('''
SELECT * FROM TIER ORDER BY RANDOM() LIMIT 1;
''').fetchall()

query = subjekt[0][1]+'-'+praedikat[0][1]+'-'+objekt[0][1]+'-'+adjektiv[0][1]
print(query)
