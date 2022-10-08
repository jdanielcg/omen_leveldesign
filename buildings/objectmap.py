from distutils.command.build import build
import pygame

from buildings.buildingcatalog import BuildingCatalog

class Objectmap:
    def __init__(self, objectset):
        self.objectset = objectset
        self.tile_w, self.tile_h = objectset.tile_size
        #self.buildings = Buildings()

    def draw(self, game_window, world):
        height = world.height
        width = world.width

        screen = game_window.get_screen()
        for building in world.building_list:
            building.draw(screen)


