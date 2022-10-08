from PPlay.sprite import *
from pygame import mixer

class MainMenu:
    def __init__(self,g, gamewindow):
        self.g = g      
        self.gameWindow = gamewindow

        #musica do menu
        self.p_musica = True
        self.is_playing_music = True
        mixer.init()
        mixer.music.load('assets\menu.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)        
        
        #pegando a entrada do usuário
        self.teclado = gamewindow.get_keyboard()
        self.mouse = gamewindow.get_mouse()
        
        #fundo do menu
        self.background = Sprite("assets\dragao.webp")
        
        #titulo
        self.titulo = Sprite("assets\Titulo.png")
        self.titulo.set_position(1280/2 - 280, 50)
        
        #janela help
        self.janelahelp = Sprite("assets\submenu.png")
        self.janelahelp.set_position(1280/2 - 460, 65)
        self.p_help = True
        
        #janela settings
        self.janelasettings = Sprite("assets\submenu.png")
        self.janelasettings.set_position(1280/2 - 460, 65)
        self.p_settings = True
        
        #botao play
        self.play = Sprite("assets\Buttons\play.png")
        self.play.set_position(1280/2 - 120, 250)
        
        #botao settings
        self.settings = Sprite("assets\Buttons\settings.png")
        self.settings.set_position(1280/2 - 120, 350)
        
        #botao exit
        self.exit = Sprite("assets\Buttons\exit.png")
        self.exit.set_position(1280/2 - 120 , 450)
        
        #botao help
        self.help = Sprite("assets\Buttons\help.png")
        self.help.set_position(1260 - 70 , 630)
        
        #botao music
        self.music = Sprite("assets\Buttons\music.png")
        self.music.set_position(1260 - 150, 630)
        
        #botao quit
        self.quit = Sprite("assets\Buttons\quit.png")
        self.quit.set_position(1280/2 - 120, 570)
        
        #creditos
        self.creditos = Sprite("assets\creditos.png")
        self.creditos.set_position(1280/2 - 280 , 550)

    def update(self, delta_time):
        self.background.draw()
        self.titulo.draw()
        self.play.draw()
        self.settings.draw()
        self.music.draw()
        self.creditos.draw()
        self.exit.draw()       
        self.help.draw()

        #botao play
        if self.mouse.is_over_object(self.play) and self.mouse.is_button_pressed(True):
            self.g.current_screen = self.g.gamescreen

        #botao exit
        if self.mouse.is_over_object(self.exit) and self.mouse.is_button_pressed(True):
            self.gameWindow.close()

        #botão music
        if self.mouse.is_over_object(self.music):              
            if self.mouse.is_button_pressed(True):
                if not self.p_musica:                    
                    self.p_musica = True
            #a ação ocorre ao soltar o botão, evitando erros
            elif self.p_musica: 
                if self.is_playing_music:
                    mixer.music.pause()               
                else:
                    mixer.music.unpause()   
                self.is_playing_music = not self.is_playing_music             
                self.p_musica = False
        else:                 
            self.cliked = False       

        #botao help
        #if self.click.is_over_object(self.help) and self.click.is_button_pressed(True):
        #    if self.p_help == True:
        #        self.p_help = False
        #        #janela do help
        #        while True:
        #            self.janelahelp.draw()
        #            self.quit.draw()
        #            self.gameWindow.draw_text("About", self.gameWindow.width/2 - 100, 90, size=60, bold=True, color=(224, 224, 222))                    
        #            if self.click.is_over_object(quit) and self.click.is_button_pressed(True):
        #                break
        #    else:
        #        self.p_help = True

        #botao settings
        #if self.click.is_over_object(self.settings) and self.click.is_button_pressed(True):
        #    if self.p_settings == True:
        #        self.p_settings = False
#
        #        #janela do settings
        #        while True:
        #            self.janelasettings.draw()
        #            self.quit.draw()
#
        #            self.gameWindow.draw_text("Settings", self.gameWindow.width/2 - 127, 90, size=60, bold=True, color=(224, 224, 222))                        
        #            if self.click.is_over_object(self.quit) and self.click.is_button_pressed(True):
        #                break
        #    else:
        #        self.p_settings = True

        
        
