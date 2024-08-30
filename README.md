# ShellForge
## Goals

Implement a pagination system.
Set up image caching for faster load times.
Create a mod favoriting system.

    Develop an author page displaying all of their creations.

## TODO
### In Progress

- [ ] Get images to visualize on the window.
- [ ] Implement favorites.
- [ ] Implement image caching.
- [ ] Allow installation from pre-installed versions to save bandwidth/space.
- [ ] Refactor API data collection in data_collecting.py - will eventually become .java.

- [ ] Fetch data with customizable parameters for filtering.

- [ ] Parse necessary information:

      Name
      Authors
      Download count
      Categories
      Class ID
      Links (all)
      Logo thumbnail URL
      ID
      Screenshots (title, description, URL)
      Date created
      Date modified
      Date released
      Primary category ID

- [ ] Consider if these are needed:

      Latest files indexes
      Main file ID
      Game ID
      Slug
      Status
      Is featured
      Allow mod distribution
      Game popularity rank
      Is available
      Thumbs up count

- [ ] Store data:

      Write to CSV
      Write to JSON
      Write directly to the app

### Completed

Add error message for when not connected to the internet.

    Create a method for easily commenting out image creation.

## API Call Commands/Params

    Class IDs:
        6552: Shaders
        6: Mods
        4471: Mod Packs
        5: Customization
        4546: Addons
        4559: Texture Packs
        17: Bukkit Plugins
        12: Worlds

    Mod Loader Types:
        1: Forge Mods
        4: Fabric Mods
        5: Quilt Mods
        6: NeoForge Mods

    Sort Orders:
        'desc': Descending
        'asc': Ascending

    Sort Fields:
        1: Featured
        2: Popularity
        3: Last Updated
        4: Name
        5: Author
        6: Total Downloads
        7: Category
        8: Game Version
        9: Early Access
        10: Featured Released
        11: Release Date
        12: Rating

## Future Plans

### Find all category IDs.
### Image Caching:

    Params: mod_Id, thumbnail_Url
    Download thumbnail from URL.
    Save the thumbnail as the mod_Id in the logos directory.
    Retrieve the logo by mod_Id when needed.

### Check Internet Connection:

Utilize the existing method check_internet_connection():

    python

        def check_internet_connection(self, thumbnail_url, url='https://www.google.com/', timeout=5):
            try:
                response = requests.get(url, timeout=timeout)
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

