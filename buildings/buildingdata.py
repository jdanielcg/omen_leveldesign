
import pygame


class BuildingData:   
  
    def __init__(self, name, size = (1,1), center_tile=(0,0), filename =""):
        self.name = name
        self.size = size
        self.center_tile = center_tile        
        self.surf = pygame.image.load("assets/buildings/" + filename)        
        
        self.surf.set_colorkey((255, 0 , 255))
        self.surf.convert_alpha()


