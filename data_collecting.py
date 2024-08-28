import time
import requests
import csv
import json
import os
import apikey

headers = {
    'Accept': 'application/json',
    'x-api-key': apikey.get_api_key()
}

data_directory = 'data/'
curse_api_url = 'https://api.curseforge.com'
mod_search_url = 'https://api.curseforge.com/v1/mods/search'

def clear_data_dir():
    for filename in os.listdir(data_directory):
        file_path = os.path.join(data_directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f'{file_path} is removed')


# Get
def get_response_data(url, parameters, min_downloads=0):
    r = requests.get(url, headers=headers, params=parameters)
    r.raise_for_status()
    response_data = r.json()
    return response_data.get('data',[])
    #return [item for item in response_data['data'] if item['downloadCount'] >= min_downloads]

# Parse
def parse_data_mainmenu(data):

    with open(data_directory + 'mainmenu.csv', 'w', newline='', encoding='utf-8') as mainmenu:
        fieldnames = ['Mod_Id', 'Mod_Name', 'Description', 'Thumbnail_URL', 'WebPage_URL', 'Author_Name', 'Downloads']
        writer = csv.DictWriter(mainmenu, fieldnames=fieldnames)
        writer.writeheader()

        for item in data:
            writer.writerow({
                'Mod_Id': item['logo'].get('modId')if item['logo'] else None,
                'Mod_Name': item['name'],
                'Description': item['summary'],
                'Thumbnail_URL': item['logo'].get('url') if item['logo'] else None,
                'WebPage_URL': item['links'].get('websiteUrl') if item['links'] else None,
                'Author_Name': item['authors'][0].get('name') if item['authors'] else 'Unknown',
                'Downloads': item['downloadCount'],

            })
    print("Successfully wrote to file")

params = {
    'gameId': 432,
    'classId': 6,
    # 'status': 6,
    'sortOrder': 'desc',
    'sortField': 6,
    'index': 0,
    'pageSize': 50,
}

response_data = get_response_data(mod_search_url, params)
parse_data_mainmenu(response_data)




''' 
TODO:
Parse data from response into json
- downloadCount


- hold on to ids so that when I make this a bit more advanced, I can just querry the API for the 
  mod rather than collect every mod
- I curious to see how long it actually would take in time to do specific queries rather than
  do what I like to call catching the wave
- A tree for the dependents for installed items in a pack
- Author profile of thier mods they made


#######( Data parse study )#######
- https://docs.curseforge.com/?python#tocS_ModLoaderType

- latestFilesIndexes is good for faster searchs as the info is more condensed
- What I might do is figure something out with caching

'''