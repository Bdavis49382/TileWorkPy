import pygame
class Material:

    def __init__(self,name,file_name,columns,frames,collides,tile_size,sprite_size=32) -> None:
        self.name = name
        self.collides = collides
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
            images.append(pygame.transform.scale(image,(tile_size,tile_size)).convert_alpha())
        return images
