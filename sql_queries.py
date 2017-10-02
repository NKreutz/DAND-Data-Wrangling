#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import pprint

connection = sqlite3.connect("edmonton_openstreetmaps.db")
cursor = connection.cursor()
query = "select value from nodes_tags where key = 'street'"
cursor.execute(query)
rows = cursor.fetchall() # or use cursor.fetchone() for one at a a time
pprint.pprint(rows) # or loop over the rows

query2 = "select value from nodes_tags where key = 'city'"
cursor.execute(query2)
rows = cursor.fetchall() # or use cursor.fetchone() for one at a a time
pprint.pprint(rows) # or loop over the rows
connection.close
