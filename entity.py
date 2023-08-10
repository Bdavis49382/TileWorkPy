import pygame
from vector import Vector
from path import get_next_step
from entityEvent import EntityEvent
class Entity(pygame.sprite.Sprite):

    def __init__(self,position,materials,tile_size,tilemap,events = [],animated = False,frame = 0,health = 10,animation_delay = 100):
        super().__init__()
        # self.rect = pygame.Rect(position[0],position[1],tile_size,tile_size)
        self.tile_size = tile_size
        self.position = position
        self.materials = materials
        self.frame = frame
        self.health = health
        self.state = 'neutral'
        self.tilemap = tilemap
        self.image = self.materials[self.state].images[self.frame]
        self.velocity = Vector(0,0)
        self.tags = []
        self.events = events
        if animated:
            self.events.append(EntityEvent("animate",self.animate,[],animation_delay))
    
    def follow(self,screen,map,target):
        self.velocity = get_next_step(map,self,target)
        self.move(screen,map)
    
    def update(self,screen,map):
        '''Checks all events and updates them accordingly, removing any events which have no more uses'''
        remove_i = None
        for i,event in enumerate(self.events):
            if not event.check():
                remove_i = i
        if remove_i:
            self.events.pop(remove_i)
    
    def animate(self):
        self.frame += 1
        self.frame %= self.materials[self.state].frames
        self.image = self.materials[self.state].images[self.frame]

    def get_tile_pos(self):
        return (self.position + self.tilemap.offset).divide_by_int(self.tile_size)
    
    def move(self,screen,map):
        if self.valid_move(screen,map,self.velocity):
            self.position += self.velocity

    def collide(self,other,screen,map):
        if self.health <= 0:
            self.kill()
    
    def on_screen(self,screen):
        rect = pygame.Rect(self.position.x + self.tilemap.offset.x,self.position.y + self.tilemap.offset.y,self.tile_size,self.tile_size)
        return screen.get_rect().contains(rect)
    
    def draw(self,screen):
        screen.blit(self.materials[self.state].images[self.frame],(self.position + self.tilemap.offset).tuple()) 

    def valid_move(self,screen,map,velocity):
        # rect = pygame.Rect(self.position.x,self.position.y,self.tile_size,self.tile_size)
        # new_rect = rect.move(velocity[0],velocity[1])
        # if not screen.get_rect().contains(new_rect):
        #     return False
        new_pos = (self.position + self.tilemap.offset + velocity).divide_by_int(self.tile_size)
        tile = map.tiles[new_pos.x][new_pos.y]
        if tile.material.collides:
            return False
        return True
            
