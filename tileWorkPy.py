import pygame
from eventHandler import EventHandler
from file_handling import load_materials,load_file
from vector import Vector
from ui.tilemap import TileMap
class TileWorkPy:
    def __init__(self,material_file,image_path,tilemap_file,tile_size,screen_width,screen_height,caption,tilemap_index=0):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.materials,self.materials_list = load_materials(material_file,image_path,tile_size)
        pygame.display.set_caption(caption)
        self.text_maps = load_file(tilemap_file)
        self.tilemap = TileMap(self.text_maps[tilemap_index],self.materials,tile_size)
        self.entities = pygame.sprite.Group()
        self.event_handler = EventHandler(self.screen,self.tilemap,self.entities)
    
    
    def add_camera(self,speed):
        '''Adds a camera which moves by wasd controls at the given speed.'''
        self.event_handler.add_event('keydown',pygame.K_w,self.tilemap.set_camera_velocity,[Vector(0,speed)])
        self.event_handler.add_event('keydown',pygame.K_s,self.tilemap.set_camera_velocity,[Vector(0,-speed)])
        self.event_handler.add_event('keydown',pygame.K_a,self.tilemap.set_camera_velocity,[Vector(speed,0)])
        self.event_handler.add_event('keydown',pygame.K_d,self.tilemap.set_camera_velocity,[Vector(-speed,0)])
        self.event_handler.add_event('keyup',0,self.tilemap.set_camera_velocity,[Vector(0,0)])


    def run(self,fps = 60):
        clock = pygame.time.Clock()
        clock.tick(fps)
        while True:
            self.screen.fill((50,0,0))
            self.tilemap.draw(self.screen)
            self.tilemap.change_offset(self.tilemap.camera_velocity)
            
            for entity in self.entities:
                if entity.on_screen(self.screen):
                    entity.draw(self.screen)
                    entity.update(self.screen,self.tilemap)

            if self.event_handler.handle_events() == False:
                return False
            
            pygame.display.flip()