#https://api.artic.edu/docs/#introduction

import requests
from dataclasses import dataclass

@dataclass
class Art:
    id: int
    title: str
    artist: str

@dataclass
class Artist:
    id: int
    title: str

@dataclass
class Exhibition:
    id: int
    title: str
    
@dataclass
class Place:
    id: int
    title: str
    type: str
    

@dataclass
class Gallery:
    id: int
    title: str
    type: str

art_data = requests.get('https://api.artic.edu/api/v1/artworks').json()
artist_data = requests.get('https://api.artic.edu/api/v1/artists').json()
place_data = requests.get('https://api.artic.edu/api/v1/places').json()
gallery_data = requests.get('https://api.artic.edu/api/v1/galleries').json()
exhibition_data = requests.get('https://api.artic.edu/api/v1/exhibitions').json()
# level 0
def populate(thing, api_data, keys): # thing is a class, json_data is json dictionary, keys is a list, returns a list of thing instances
    length = len(keys)
    data = []
    class_list = []
    for x in api_data.keys(): # iterate through level 0 keys
        if x == 'data': 
            # level 1
            for i in range(0, len(api_data['data'])): # json_data['data'] is a list of dictionaries
                for y in api_data['data'][i]:
                    for item in keys:
                        if y == item:
                            data.append(api_data['data'][i][y])
    # chunk data list grouped parameters
    for i in range(0, len(data), length):
        # create new class instance and append to list class_list
        class_list.append(thing(*data[i:i+length]))
    print(class_list)
    return class_list


populate(Art, art_data, ['id', 'title', 'artist_title'])
populate(Artist, artist_data, ['id', 'title'])
populate(Place, place_data, ['id', 'title', 'type'])
populate(Gallery, gallery_data, ['id', 'title', 'type'])
populate(Exhibition, exhibition_data, ['id', 'title'])


           