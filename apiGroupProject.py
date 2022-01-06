#https://api.artic.edu/docs/#introduction

import requests
from dataclasses import dataclass

def getHTML(url):
    response = requests.get(url)
    return response.text

@dataclass
class art:
    id: int
    name: str
    type: str
    artist: str
    year: int

@dataclass
class artist:
    id: int
    name: str
    artList: list

@dataclass
class exhibitions:
    id: int
    title: str
    featured: bool
    list_description: str

@dataclass
class location:
    id: int
    title: str

@dataclass
class gallery:
    id: int
    title: str
    type: str
    isClosed: bool
    floor: int

json_data = requests.get('https://api.artic.edu/api/v1/artworks').json()
# level 0
for x in json_data.keys(): # iterate through level 0 keys
    if x == 'data': 
        # level 1
        for y in json_data['data'][0]: # y is a list
            z = json_data['data'][0] # z is a dict
            #print(z)
            for w in z:
                #print(w)
                if w == 'title':
                    print(z[w])
               
         
    else:
        continue

        