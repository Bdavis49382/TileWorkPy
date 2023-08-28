import json
from ui.material import Material
def save_tilemap(filename,text_maps,tilemap,index):
    '''Saves a tilemap into json format on the file.
    filename: destination file name, .json format
    text_maps: list of text_maps
    tilemap: the tilemap that's been changed
    index: the index of the changed tilemap in the list'''
    if index < len(text_maps):
        text_maps[index] = [[tile.parse() for tile in column] for column in tilemap.tiles]
    else:
        text_maps.append([[tile.parse() for tile in column] for column in tilemap.tiles])

    with open(filename, 'w') as file:
        json.dump(text_maps,file)

def save_entities(filename,text_entities,entities,index):
    if index < len(text_entities):
        text_entities[index] = [entity.parse() for entity in entities] 
    else:
        text_entities.append([entity.parse() for entity in entities])

    with open(filename, 'w') as file:
        json.dump(text_entities,file)

def load_file(filename):
    '''Loads a json file and returns the jsonified data'''
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        print(filename,"did not exist. Loading an empty list")
        return []

def load_materials(filename,image_extension,tile_size):
    '''Loads the materials in a file and returns them as a dictionary of material objects and a list of the materials still in json format, together in a tuple.
    Parameters:
    filename: name of the file in .json format containing a list of objects with the following structure:
        {
        "name": "grass",
        "columns": 2,
        "frames": 3, NOTE: this is the total number of frames, not rows
        "collides": true
        }
    image_extension: a string of the filepath to the images, to be formatted with the material name. For example: ui/images/{0}.png
    tile_size: the tile_size in the tilemap
    '''
    with open(filename,"r") as file:
        materials_list = json.load(file)
        materials = {}
        for material in materials_list:
            name = material['name']
            materials[name] = Material(name,image_extension.format(name),material['columns'],material['frames'],material['collides'],tile_size)
        
        return materials,materials_list

import os

def create_files(parent_folder_path):
    print(f'Generating files for {parent_folder_path} ...\n\n')
    parent_folder_path = create_res_folder(parent_folder_path)
    catalog = {}
    catalog['image_path'] = create_image_folder(parent_folder_path)
    example = [{
                "name":"example_material",
                "columns":2,
                "frames":3,
                "collides":False
            }]
    message = "Remember that the name of the material is used as part of the filename for the image and in the text_map."
    catalog['materials'] = create_file(parent_folder_path,example,message,'materials')
    catalog['entities'] = create_file(parent_folder_path,[],"This file is only for the program, not to be added to manually.",'entities')

    example = [[["example_material","example_material"],
                ["example_material","example_material"],
                ["example_material","example_material"]]]
    message = "You can use the editor's add_random_text_map function to generate a map to you liking."
    catalog['text_maps'] = create_file(parent_folder_path,example,message,'text_maps')

    with open(f'{parent_folder_path}/catalog.json', 'w') as file:
        json.dump(catalog,file)

def create_res_folder(parent_folder_path):
    try:
        path = os.path.join(parent_folder_path,'res')
        os.mkdir(path)
        return path
    except:
        print("res folder already exists, or failed for another reason")
        return os.path.join(parent_folder_path,'res')

def create_image_folder(parent_folder_path):
    try:
        path = os.path.join(parent_folder_path,'images')
        os.mkdir(path) 
        print(">Created images folder: image reference will be \"images/{0}.png\" or jpg if preferred.")
    except:
        print('image folder already present')
    return 'res/images/{0}.png'
    
def create_file(parent_folder_path,example,message,name):
    try:
        with open(f'{parent_folder_path}/{name}.json','w') as file:
            json.dump(example,file)
            print(f">Created {name} file with one example at {parent_folder_path}/{name}.json. \n\t{message}")
    except:
        print(f'error creating {name} file.')
    return f'res/{name}.json'



# create_files('C:/Users/Bdude/OneDrive/Desktop/Code/TileWorkPy')