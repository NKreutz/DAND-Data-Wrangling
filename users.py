#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return


def process_map(filename):
    users = set()
    poss = ['node', 'way', 'relation']
    for _, element in ET.iterparse(filename):
        if element.tag in poss:
            users.add(element.attrib['uid'])

    return users


def test():

    users = process_map('sample_k1000.osm')
    pprint.pprint(users)
    #assert len(users) == 6



if __name__ == "__main__":
    test()
