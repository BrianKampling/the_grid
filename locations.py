import json
from location import Location

#Convert this into json, getting stuck in recusrion.
def starting_tavern():
    name = 'The Silvery Moon Tavern'
    desc = 'This is a simple tavern with a bar and several tables'
    exits = {'s': main_street_1()}
    loc = Location(name, desc, exits)
    return loc


def main_street_1():
    name = 'Main Street'
    desc = 'Cobblestone street'
    exits = {'n': starting_tavern()}
    loc = Location(name, desc, exits)
    return loc

def get_location(location_id):
    with open('locations.json', 'r') as l:
        loc = l.read()
        loc = json.loads(loc)
        loc = loc[u'locations'][location_id]
        get_loc = Location(loc[u'name'],loc[u'desc'],loc[u'exits'])
        return get_loc

get_location('The Silvery Moon Tavern')