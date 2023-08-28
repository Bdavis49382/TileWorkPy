from ui.tile import Tile
from vector import Vector
class TileMap:
    def __init__(self,text_map, materials,tile_size,offset = Vector(0,0)):
        self.tile_size = tile_size
        self.rows = len(text_map[0])
        self.columns = len(text_map)
        self.screen_width = self.columns * tile_size
        self.screen_height = self.rows * tile_size
        self.tiles = self.load_tiles(text_map,materials,offset)
        self.materials = materials
        self.offset = offset
        self.camera_velocity = Vector(0,0)
    
    def set_camera_velocity(self,velocity):
        self.camera_velocity = velocity
    
    def change_offset(self,offset):
        self.offset += offset
        for column in self.tiles:
            for tile in column:
                tile.offset += offset
    
    def get_tile(self,pos):
        x = (pos[0]-self.offset.x)//self.tile_size
        y = (pos[1]-self.offset.y)//self.tile_size
        if 0 <= x < self.columns and 0 <= y < self.rows:
            return self.tiles[x][y]
        return None
    
    def get_tile_at_mouse(self,mouse):
        tile = self.get_tile(mouse())
        return tile
    def change_tile(self,materials,materials_list,mouse):
        tile = self.get_tile(mouse())
        for i,material in enumerate(materials_list):
            if material['name'] == tile.material.name:
                index = i
        tile.frame = 0
        tile.material = materials[materials_list[(index+1) % len(materials_list)]['name']]
        # print(tile.material)

    def change_tile_size(self,amount):
        self.tile_size += amount 
        for material in self.materials.values():
            material.resize(self.tile_size)
        # for row in self.tiles:
        #     for tile in row:
        #         tile.position += Vector(amount,amount)

    def flip_tile(self,mouse):
        # print(self.tiles[(mouse()[0]+self.offset.x)//self.tile_size][(mouse()[1]+self.offset.y)//self.tile_size])
        # x = (mouse()[0]-self.offset.x)//self.tile_size
        # y = (mouse()[1]-self.offset.y)//self.tile_size
        tile = self.get_tile(mouse())
        if tile:
            tile.frame += 1
            tile.frame %= tile.material.frames

    def load_tiles(self,text_map,materials,offset):
        tiles = []
        for x in range(0,self.screen_width,self.tile_size): 
            row = []
            for y in range(0,self.screen_height,self.tile_size):
                text = text_map[x//self.tile_size][y//self.tile_size]
                if text.find(":") == -1:
                    row.append(Tile(Vector(x,y) + offset,materials[text],0,self))
                else:
                    material,frame = text.split(":")
                    row.append(Tile(Vector(x,y) + offset,materials[material],int(frame),self))
            tiles.append(row)
        return tiles
    
    def check_tiles(self,point:tuple):
        for column in self.tiles:
            for tile in column:
                if tile.rect.collidepoint(point):
                    return tile
    
    def draw(self,screen):
        for column in self.tiles:
            for tile in column:
                tile.draw(screen)