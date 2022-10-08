
from PPlay.sprite import*
from buildings.building import Building
from buildings.buildingcatalog import BuildingCatalog
from globals import Globals
from interface.framerate import Framerate
from interface.gameinterface import Gameinterface
from mapa.tilemap import Tilemap
from mapa.tileset import Tileset
from world import World
from buildings.objectmap import Objectmap
from buildings.objectset import Objectset
from movables.creaturemap import Creaturemap
from movables.creatureset import Creatureset
import pygame

class Game: 
    def __init__(self, g, gameWindow):
        self.g = g      
        self.gameWindow = gameWindow
        self.framerate = Framerate()

        #world: gerencia a representação lógica do mundo, é onde estão as células (cell)
        self.world = World() 

        #tilemap: gerencia a representação visual do mapa fixo, apartir das cells
        #uma cell representa um tile
        self.tilemap = Tilemap(Tileset('otsp_tiles_01.png',(32, 32)))    

        #objectmap: gerencia a representação visual dos objetos
        #várias cell/tile podem representar um objeto
        self.objectmap = Objectmap(Objectset('otsp_town_01.png',(32, 32)))   

        #cria a biblioteca com informações sobre as contruções
        self.catalog = BuildingCatalog()

        #cria algumas construções para teste:
        self.buildings = [Building(self.catalog.get("dinner"),3,3)]
        self.world.building_list = self.buildings 

        #creaturemap: gerencia a representação visual das criaturas
        self.creaturemap = Creaturemap(Creatureset('otsp_creatures_01.png', (32,32)))    

        self.gameinterface = Gameinterface(g,gameWindow)

    #loop principal
    def update(self, delta_time):  
        #limpa a janela     
        self.gameWindow.set_background_color([128,128,128])  

        #atualiza a simulação
        self.world.update(self.gameWindow.delta_time())   

        #escreve a imagem do mapa na janela
        self.tilemap.draw(self.gameWindow, self.world) 

        #escreve a imagem dos objetos na janela
        self.objectmap.draw(self.gameWindow, self.world)   

        #escreve a imagem das criaturas na tela
        self.creaturemap.draw(self.gameWindow, self.world)  

        self.gameinterface.update(delta_time)

        #atualiza a janela e rendeniza tudo
        self.gameWindow.set_title(self.g.gameApplicationName + self.framerate.get_text(delta_time))
        #ideal < 16ms = 60fps

        