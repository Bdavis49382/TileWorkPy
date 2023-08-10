# TileWorkPy: A python framework for tile-based python games
## Using pygame

### Getting Started:
* Create a folder for your game.
* Import and run the function file_handling.create_files to create necessary files and folders.
* Populate the image folder and materials file with images and information for you game.
* Populate the saved_maps file in one of three ways:
    1. Manually enter in values yourself of each material you want on each tile.
    2. Run the editor.add_random_text_map function to create a random text map by your specifications.
    3. Call the editor.run function to run the editor which will generate a random map and allow you to adjust it.
* Create an instance of the tileWorkPy class
* Add any events and entities to the tileWorkPy instance
* Call the tileWorkPy run method.