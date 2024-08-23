import json

import requests
import apikey

headers = {
    'Accept': 'application/json',
    'x-api-key': apikey.get_api_key()
}

r = requests.get('https://api.curseforge.com/v1/mods/search', params={
    'gameId': 432,
    'classId': 6,
    'sortOrder': 'desc',
    'sortField': 6,


}, headers = headers)

with open('data/test_dump.json', 'w', encoding='utf-8') as file:
    json.dump(r.json(), file, indent=4)
    print('Successfully dumped')

r = requests.get('https://api.curseforge.com/v1/mods/search', params={
    'gameId': 432,
    'classId': 6,
    'sortOrder': 'desc',
    'sortField': 6,

}, headers = headers)

with open('data/test2_dump.json', 'w', encoding='utf-8') as file:
    json.dump(r.json(), file, indent=4)
    print('Successfully dumped')

# Api call commands / params
'''
'classId': 6552 # Shaders
'classId': 6    # Mods
'classId': 4471 # Mod packs
'classId': 5    # Customization
'classId':      # Data Packs
'classId': 4546 # Addons
'classId': 4559 # Texture Pacls
'classId': 17   # Bukkit Plugins
'classId': 12   # Worlds


'modLoaderType':1 # Forge mods
'modLoaderType':4 # Fabric mods
'modLoaderType':5 # Quilt mods
'modLoaderType':6 # NeoForge mods

'sortOrder': 'desc' # Biggest to smallest
'sortOrder': 'desc' # Smallest to biggest

'sortField': 1, # Featured
'sortField': 2, # Popularity
'sortField': 3, # LastUpdated
'sortField': 4, # Name
'sortField': 5, # Author
'sortField': 6, # Total Downloads
'sortField': 7, # Category
'sortField': 8, # Game Verison
'sortField': 9, # Early Access
'sortField': 10, # Featured Released
'sortField': 11, # Released Date
'sortField': 12, # Rating


'''