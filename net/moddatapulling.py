"""

This will likely not be a long term file as i'll break it down to prevent overcomplicating

TODO:
- API key
- Find all categories id's

PLANNED:
- Image Caching
- Check Internet Connection
- Pulling data from api

"""

"""
Image Caching:
- Params: mod_Id, thumbnail_Url
- Download thumbnail from Url
- save the thumbnail as the mod_Id in dir logos
- when needing file pass in mod_Id and will 
    get the logo with corresponding id 
"""

"""
Checking Internet Connection:

# already made it lol
    def check_internet_connection(self, thumbnail_url, url='https://www.google.com/', timeout=5):
        try:
            response = requests.get(url, timeout=timeout)
            # status code is 200 (OK)
            if response.status_code == 200:
                thumbnail_label = self.populate_images(thumbnail_url)
                return thumbnail_label
            else:
                print("Failed to connect to the internet")
                thumbnail_label = self.populate_blank_images()
                return thumbnail_label
        except (requests.ConnectionError, requests.Timeout):
            print("Failed to connect to the internet. Check your internet connection.")
            thumbnail_label = self.populate_blank_images()
            return thumbnail_label
"""

"""
Pulling data from api: 
# I already made it, but need to refactor
# most of it is in data_collecting.py

- Fetch
    - I'll need to make it to where we can pass in params or something so 
        that there are different ways of filtering
        - Use this to find the filter types, make sure to apply as many as possible at first
        https://studios.curseforge.com/
    
    
- Parse
    Determine Necessary info:
    - name
    - authors
    - downloadCount
    - categories
    - classId
    - links (all links)
    - logo.thumbnailUrl
    - id
    - screenshots (title, description, url)
    - 
    - dateCreated
    - dateModified
    - dateRealeased
    - primaryCategoryId
    - Going the have to parse it more to my liking, but
        for now latestFiles(all)
    
    Not sure if need it:
    - latestFilesIndexes
    - "mainFileId": 4820053,
    - gameId
    - slug
    - status
    - isFeatured
    - allowModDistribution
    - gamePopularityRank
    - isAvailable
    - thumbsUpCount
    
    
- Store
    - Once we have the specified filters and have collected the data we wanted: 
    a) write to csv
    b) write to json
    c) write directly to app
    d)
"""

"""
# "categories" info:
"id": 415   # "Energy, Fluid, and Item Transport"
"id": 419   # "Magic"
"id": 420   # "Storage"
"id": 421   # "API and Library"
"id": 423   # "Map and Information"
"id": 424   # "Cosmetic"
"id": 425   # "Miscellaneous"
"id": 434   # "Armor, Tools, and Weapons"
"id": 435   # "Server Utility"
"id": 436   # "Food"
"id": 4773  # "CraftTweaker"
"id": 5191  # "Utility & QoL"


"""

"""
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

"""
