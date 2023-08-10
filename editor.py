import pygame, json,random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from file_handling import save_file,load_file,load_materials
TILE_SIZE = 24
from ui.tilemap import TileMap
from tileWorkPy import TileWorkPy

def add_random_text_map(filename,num_rows,num_columns,regions,index=None):
    '''Generates a new random text map into the file, returning the index of the created text_map in the file.
    Parameters:
        filename: the name of the file
        num_rows: the desired number of rows of tiles
        num_columns: the desired number of columns of tiles
        regions: a 3d list containing a list of materials for each region on a 2d map, facilitating probability.
            For example: the region at [0][0] might have 8 grass strings and 2 water strings to create a grassland
        index: Optionally select the index of the file to access, if not provided, creates a new text_map in the file'''
    try:
        with open(filename,"r") as file:
            text_maps = json.load(file)
    except:
        text_maps = []
    # with open("assets/sheets.json","r") as file:
    #     materials_list = json.load(file)['materials']
    text_map = []
    last_material = regions[0][0][0]
    last_variety = 0
    for x in range(num_columns): 
        rows = []
        for y in range(num_rows):
            if random.random() > .2:
                material = last_material if random.random() > .5 else text_map[x-1][y].split(':')[0] if x != 0 else last_material
                if random.random() > .3 or material == 'water':
                    variety = last_variety
                else:
                    variety = random.randrange(3)
            else:
                
                region = regions[x // (num_columns//3)][y // (num_rows//3)]
                material = random.choice(region)
                variety = random.randrange(3)
            last_material = material
            rows.append(f'{material}:{variety}')
        text_map.append(rows)
    with open(filename,"w") as file:
        if index != None:
            text_maps[index] = text_map
        else:
            text_maps.append(text_map)
            index = len(text_maps) - 1
        json.dump(text_maps,file)
    return index

def run(regions,source_file,material_file,image_path,world=-1):
    '''Runs a mini version of the framework in a tilemap editing mode. Left clicks change the frame of the tile, right clicks change the material entirely
    Parameters:
        regions: a 3d list containing a list of materials for each region on a 2d map, facilitating probability.
            For example: the region at [0][0] might have 8 grass strings and 2 water strings to create a grassland
        source_file: a file with the text_maps. 
        material_file: a file with the material information in this format:
            {
            "name": "grass",
            "columns": 2,
            "frames": 3, NOTE: this is the total number of frames, not rows
            "collides": true
            }
        image_path:  a string of the filepath to the images, to be formatted with the material name. For example: ui/images/{0}.png
        world: if you'd like to run a world already in the source file, give the index here.
            '''

    # If no world is chosen, create a new one and use it
    if world == -1:
        world = add_random_text_map(source_file,99,198,regions)
    

    # Load information and create variables.
    # text_maps = load_file(source_file)
    # materials,materials_list = load_materials(material_file,image_path,TILE_SIZE) 
    # tilemap = TileMap(text_maps[world],materials,TILE_SIZE)
    
    # Create game object and assign tile flipping and changing events.
    game = TileWorkPy(material_file,image_path,source_file,TILE_SIZE,SCREEN_WIDTH,SCREEN_HEIGHT,'TileWorkPy Editor')
    game.add_camera(game.tilemap.tile_size//2)
    game.event_handler.add_event('mouse',1,game.tilemap.flip_tile,[pygame.mouse.get_pos])
    game.event_handler.add_event('mouse',3,game.tilemap.change_tile,[game.materials,game.materials_list,pygame.mouse.get_pos])

    # Run editor and save when finished.
    game.run()
    save_file(source_file,game.text_maps,game.tilemap,world)


if __name__ == '__main__':
    grassland = ['grass','rock','grass','grass','grass','grass','grass','grass','grass','water']
    ocean = ['water','water','water','water','water','water','water','water','water','water']
    mountains = ['rock','rock','rock','grass','grass','grass','grass','water','grass','grass']
    regions = [[grassland,mountains,mountains],
                [grassland,mountains,grassland],
                [ocean,grassland,grassland]]
    run(regions,'bigger_maps.json','materials.json','images/{0}.png')