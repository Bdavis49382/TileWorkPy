import pygame
class Material:

    def __init__(self,name,file_name,columns,frames,collides,tile_size,sprite_size=32) -> None:
        self.name = name
        self.collides = collides
        self.original_images = []
        self.images = self.get_images(file_name,columns,frames,tile_size,sprite_size)
        self.frames = frames
    


    def get_images(self,file_name,columns,number,tile_size,sprite_size=32):
        '''Returns a list of images for a material'''
        images = []
        sheet =  pygame.image.load(file_name).convert_alpha()
        sheet.set_alpha(255)

        for counter in range(number):
            x = counter % columns
            y = counter // columns
            rect = pygame.Rect(x*sprite_size,y*sprite_size,sprite_size,sprite_size)
            image = pygame.Surface(rect.size).convert()
            image.blit(sheet,(0,0), rect)
            image.set_colorkey((0,0,0))
            self.original_images.append(image)
            images.append(pygame.transform.scale(image,(tile_size,tile_size)).convert_alpha())
        return images
    
    def resize(self,new_tile_size):
        self.images = [pygame.transform.scale(image,(new_tile_size,new_tile_size)).convert_alpha() for image in self.original_images]

