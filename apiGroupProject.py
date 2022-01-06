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
#print(json_data)

id = json_data['data'][10]['id']
name = json_data['data'][10]['title']
print(id)

