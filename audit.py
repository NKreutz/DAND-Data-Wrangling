"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict, Counter
import re
import pprint

OSMFILE = "sample_k15.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "Point", "Crescent", "Highway", "Close", "Way", "Link", "Loop"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "ST": "Street",
            "street": "Street",
            "Rd.": "Road",
            "Rd": "Road",
            "N.": "North",
            "nw": "NW",
            "North-west": "NW",
            "North-West": "NW",
            "Northwest": "NW",
            "North-east": "NE",
            "North_East": "NE",
            "S": "South",
            "South-west": "SW",
            "Blvd": "Boulevard",
            "ave": "Avenue",
            "avenue": "Avenue",
            "Ave": "Avenue"
            }


def audit_street_type(street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            #street_types[street_type].add(street_name)
            return update_street_name(street_name, mapping)


def update_city_name(city):
    # change eg. "No. 7, County of" to "County"
    if "No." in city:
        return city.split("No.")[0] + 'County'
    # if there is a ;, discard string after ;
    if ";" in city:
        city = city.split(";")[0]
    # if there is a comma discard string after comma
    if "," in city:
        city = city.split(',')[0]
    # if there is a #, discard string after #
    if "#" in city:
            city = city.split("#")[0]
    return city


def update_postal_code(postcode):
    if len(postcode) < 6:
        return None
    if len(postcode) == 6:
        postcode =  postcode[:3] + " " + postcode[3:]
    if len(postcode) > 7:
        postcode =  postcode[:7]
    #Check that the first two characters are within the possibilities for AB
    if ((postcode[0] == "T") and (int(postcode[1]) in range(5,10)) and
        postcode[2].isalpha() and (postcode[3] == " ") and
        postcode[4].isdigit() and postcode[5].isalpha() and
        postcode[6].isdigit()):
            return postcode
    else:
        return None


def audit(tag):

    #"is_in" and "addr:city" tags are the same thing, so join them
    if tag.attrib['k'] == "is_in":
        tag.attrib['k'] = "addr:city"

    # some street names are listed under "name" instead of "addr:street"
    if tag.attrib['k'] == "name":
        for word in tag.attrib['v'].split(' '):
            if word in expected:
                tag.attrib['k'] = "addr:street"
                break

    #bus stops are listed as highways instead of amenities
    if tag.attrib['k'] == "highway" and tag.attrib['v'] == "bus_stop":
        tag.attrib['k'] = "amenity"

    # Clean postalcode data
    if tag.attrib['k'] == "addr:postcode":
        tag.attrib['v'] = update_postal_code(tag.attrib['v'])

    # Clean "addr:street" attribute
    if tag.attrib['k'] == "addr:street":
        change = audit_street_type(tag.attrib['v'])
        if change:
            tag.attrib['v'] = change

    #Clean "addr:city" attribute
    if tag.attrib['k'] == "addr:city":
        change = update_city_name(tag.attrib['v'])
        if change:
            tag.attrib['v'] = change


    return tag.attrib['k'], tag.attrib['v']



def update_street_name(name, mapping):
    for word in name.split(" "):
        if word in mapping.keys():
            replacement = mapping[word]
            name = name.replace(word, replacement)

    return name


def test():
    osm_file = open(OSMFILE, "r")
    tag_types = ['node', 'way', 'relation']
    default_set = set()

    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag in tag_types:
            for tag in elem.iter("tag"):
                tag.attrib['k'], tag.attrib['v'] = audit(tag)
                if tag.attrib['k'] == "addr:city":
                    default_set.add(tag.attrib['v'])

    pprint.pprint(default_set)

    osm_file.close()




if __name__ == '__main__':
    test()
