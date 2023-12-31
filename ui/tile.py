from vector import Vector
class Tile:
    def __init__(self, position,material,frame,tilemap,offset=None):
        self.material = material
        self.position = position
        self.frame = frame
        self.tilemap = tilemap
        if offset == None:
            self.offset = Vector(0,0)
        else:
            self.offset = offset
        
    
    def get_tile_position(self):
        return (self.position + self.offset) / Vector(self.tilemap.tile_size,self.tilemap.tile_size)
    
    def draw(self,screen):
        screen.blit(self.material.images[self.frame],(self.position + self.offset).tuple())
    
    def parse(self):
        return f'{self.material.name}:{self.frame}'
    
    def __str__(self):
        return f'{self.material.name} at {self.position}'

