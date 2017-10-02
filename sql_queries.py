#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import pprint

connection = sqlite3.connect("edmonton_openstreetmaps.db")
cursor = connection.cursor()

# Create Views to speed up searches
view1 = '''create view ways_nodes_tags_view
as select * from nodes_tags
union all
select * from ways_tags
'''

# Count how unique users there are (copied from SQL project example)
query1 = ''' select count(distinct(e.uid))
from (select uid from nodes
union all
select uid from ways) as e
'''

# Count number of Nodes
query2 = ''' select count(*)
from nodes
'''

# Count number of Ways
query3 = ''' select count(*)
from ways
'''

# Count how many regions/cities are represented in the dataset
query4 = ''' select count(*)
from (select value, count(*) as num
from ways_nodes_tags_view
where key = 'city'
group by value)
'''

# Count how many entries there are for each community, and return the top 10
query5 = '''select value, count(*) as num
from ways_nodes_tags_view
where key = 'city'
group by value
order by num desc
limit 10
'''

# Count how many entries there are for each community, and return those
# with only 1 entry
query6 = '''select value, count(*) as num
from ways_nodes_tags_view
where key = 'city'
group by value
having num = 1
'''

#Find out what amenities are listed, return top 10
query7 = '''select value, count(*) as num
from ways_nodes_tags_view
where key = 'amenity'
group by value
order by num desc
limit 10
'''

#Find the names of the most common restaurants
query8 = ''' select value, count(*) as num
from (select b.value as value from ways_nodes_tags_view as a, ways_nodes_tags_view as b
where a.id = b.id
and (a.value = "fast_food" or a.value = "restaurant")
and b.key = "name"
group by a.id)
group by value
having num > 1
order by num desc
'''

all_views = [view1]
all_queries = [query1, query2, query3, query4, query5, query6, query7, query8]

cursor.execute(view1)
count = 0
for query in all_queries:
    count += 1
    cursor.execute(query)
    rows = cursor.fetchall()
    print "Query #" + str(count)
    pprint.pprint(rows)


connection.close
