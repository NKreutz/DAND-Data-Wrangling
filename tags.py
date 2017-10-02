#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
Before you process the data and add it into your database, you should check the
"k" value for each "<tag>" and see if there are any potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags. As we saw in the quiz earlier, we would like to change the data
model and expand the "addr:street" type of keys to a dictionary like this:
{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with
problematic characters.

Please complete the function 'key_type', such that we have a count of each of
four tag categories in a dictionary:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
See the 'process_map' and 'test' functions for examples of the expected format.
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def city_values(element):
    city = None
    if element.attrib['k'] == 'addr:city':
        city = element.attrib['v']
    return city



def key_type(element, keys):
    other = None
    if element.tag == "tag":
        k = element.attrib['k']
        if re.search(lower, k):
            keys['lower'] += 1
        elif re.search(lower_colon, k):
            keys['lower_colon'] += 1
        elif re.search(problemchars, k):
            keys['problemchars'] += 1
        else:
            keys['other'] += 1
            other = k

    return keys, other



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    others = set()
    key = set()
    cities = set()
    for _, element in ET.iterparse(filename):
        if element.tag == "tag":
            key.add(element.attrib['k'])
            keys, other = key_type(element, keys)
            others.add(other)
            cities.add(city_values(element))


    return keys, others, key, cities



def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys, others, key, cities = process_map('sample_k1000.osm')
    pprint.pprint(cities)
    #pprint.pprint(key)
    #pprint.pprint(keys)
    #pprint.pprint(others)
    #assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()
