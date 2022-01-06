#https://api.artic.edu/docs/#introduction

import requests
from dataclasses import dataclass

def getHTML(url):
    response = requests.get(url)
    return response.text

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
class Type:
    id: int
    title: str
    
@dataclass
class Style:
    id: int
    title: str

@dataclass
class Gallery:
    id: int
    title: str

json_data = requests.get('https://api.artic.edu/api/v1/artworks').json()
# level 0
def populate(thing, json_data, keys): # thing is a class, json_data is json dictionary, keys is a list
    length = len(keys)
    data = []
    class_list = []
    for x in json_data.keys(): # iterate through level 0 keys
        if x == 'data': 
            # level 1
            for i in range(0, len(json_data['data'])): # json_data['data'] is a list of dictionaries
                for y in json_data['data'][i]:
                    for item in keys:
                        if y == item:
                            data.append(json_data['data'][i][y])
    # chunk data list grouped parameters
    for i in range(0, len(data), length):
        # create new class instance and append to list class_list
        class_list.append(thing(*data[i:i+length]))
    print(class_list)
    return class_list

    
populate(Art, json_data, ['id', 'title', 'artist_title'])
populate(Artist, json_data, ['artist_id', 'artist_title'])
populate(Gallery, json_data, ['gallery_id', 'gallery_title'])
populate(Style, json_data, ['style_id', 'style_title'])
populate(Type, json_data, ['artwork_type_id', 'artwork_type_title'])

                            
                    
    
                

     
           
                