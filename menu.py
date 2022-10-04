from tokenize import Triple
from pygame import mixer
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import allies
import pygame

#musica do menu
p_musica = True
mixer.init()
mixer.music.load('assets\menu.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

#dimensões
janela_largura = 1280
janela_altura = 720

#-> menu
#criando a janela do menu
janela = Window(janela_largura, janela_altura)
janela.set_title("Omen of Ericis")

#pegando a entrada do usuário
teclado = janela.get_keyboard()
click = janela.get_mouse()

#fundo do menu
background = Sprite("assets\dragao.webp")

#titulo
titulo = Sprite("assets\Titulo.png")
titulo.set_position(1280/2 - 280, 50)

#janela help
janelahelp = Sprite("assets\submenu.png")
janelahelp.set_position(1280/2 - 460, 65)
p_help = True

#janela settings
janelasettings = Sprite("assets\submenu.png")
janelasettings.set_position(1280/2 - 460, 65)
p_settings = True

#botao play
play = Sprite("assets\Buttons\play.png")
play.set_position(1280/2 - 120, 250)

#botao settings
settings = Sprite("assets\Buttons\settings.png")
settings.set_position(1280/2 - 120, 350)

#botao exit
exit = Sprite("assets\Buttons\exit.png")
exit.set_position(1280/2 - 120 , 450)

#botao help
help = Sprite("assets\Buttons\help.png")
help.set_position(1260 - 70 , 630)

#botao music
music = Sprite("assets\Buttons\music.png")
music.set_position(1260 - 150, 630)

#botao quit
quit = Sprite("assets\Buttons\quit.png")
quit.set_position(1280/2 - 120, 570)

#creditos
creditos = Sprite("assets\creditos.png")
creditos.set_position(1280/2 - 280 , 550)

#portal level
portal_level_counter = 1
portal_level_percent = 0

#-> jogo
#botao menu jogo
menu_jogo = Sprite("assets\Buttons\menu_jogo.png")
menu_jogo.set_position(12,12)
#barra botoes jogo
barra_botoes_jogo = Sprite("assets\Buttons\Barra_botoes_jogo.png")
barra_botoes_jogo.set_position(janela_largura/2 - 340,7)
p_barra_botoes_jogo = True
#portal level
portal_level = Sprite("assets\Buttons\portal_level.png")
portal_level.set_position(janela_largura/2 + 450, 12)
#botao jogo construct
botao_jogo_construct = Sprite("assets\Buttons\Botao_jogo_construct.png")
botao_jogo_construct.set_position(janela_largura/2 - 265, 20)
p_construct = True
#botao jogo resources
botao_jogo_resources = Sprite("assets\Buttons\Botao_jogo_resources.png")
botao_jogo_resources.set_position(janela_largura/2 - 165, 20)
p_resources = True
#botao jogo research
botao_jogo_research = Sprite("assets\Buttons\Botao_jogo_research.png")
botao_jogo_research.set_position(janela_largura/2 - 65, 20)
p_research = True
#botao jogo reports
botao_jogo_reports = Sprite("assets\Buttons\Botao_jogo_reports.png")
botao_jogo_reports.set_position(janela_largura/2 + 35, 20)
p_reports = True
#botao jogo options
botao_jogo_options = Sprite("assets\Buttons\Botao_jogo_options.png")
botao_jogo_options.set_position(janela_largura/2 + 135, 20)
p_options = True
#botao jogo close
botao_jogo_close = Sprite("assets\Buttons\Botao_close.png")
botao_jogo_close.set_position(140, janela_altura/2 - 210)
#barra botoes2 jogo
barra_botoes2_jogo = Sprite("assets\Buttons\Barra_botoes2_jogo.png")
barra_botoes2_jogo.set_position(20,janela_altura/2 - 220)
p_barra_botoes2_jogo = True


#velocidade universal dos movables
velx = 400
vely = 400

# -> Kobold Laborer
#cima
laborercima = Sprite("assets\movables\Allies\kobold_laborer\cima.png", 9)
laborercima_idle = Sprite("assets\movables\Allies\kobold_laborer\cima9.png")
laborercima.set_position(janela_largura/2,janela_altura/2)
laborercima_idle.set_position(janela_largura/2,janela_altura/2)
laborercima.set_total_duration(1000)

#baixo
laborerbaixo = Sprite("assets\movables\Allies\kobold_laborer\Baixo.png", 9)
laborerbaixo_idle = Sprite("assets\movables\Allies\kobold_laborer\Baixo9.png")
laborerbaixo.set_position(janela_largura/2,janela_altura/2)
laborerbaixo_idle.set_position(janela_largura/2,janela_altura/2)
laborerbaixo.set_total_duration(1000)

#esquerda
laboreresquerda = Sprite("assets\movables\Allies\kobold_laborer\esquerda.png", 9)
laboreresquerda_idle = Sprite("assets\movables\Allies\kobold_laborer\esquerda9.png")
laboreresquerda.set_position(janela_largura/2,janela_altura/2)
laboreresquerda_idle.set_position(janela_largura/2,janela_altura/2)
laboreresquerda.set_total_duration(1000)

#direita
laborerdireita = Sprite("assets\movables\Allies\kobold_laborer\direita.png", 9)
laborerdireita_idle = Sprite("assets\movables\Allies\kobold_laborer\direita9.png")
laborerdireita.set_position(janela_largura/2,janela_altura/2)
laborerdireita_idle.set_position(janela_largura/2,janela_altura/2)
laborerdireita.set_total_duration(1000)

#começo
laborer = laborerbaixo_idle
checkpos = 'S'


while True:
    #desenhar tudo
    background.draw()
    titulo.draw()
    play.draw()
    settings.draw()
    music.draw()
    exit.draw()
    help.draw()
    creditos.draw()

    #botao play
    if click.is_over_object(play) and click.is_button_pressed(True):
        janelajogo = Window(janela_largura,janela_altura)
        janela.set_title("Omen of Ericis")
        tecladojogo = janelajogo.get_keyboard()
        clickjogo = janelajogo.get_mouse()
        while True:
            janelajogo.set_background_color([255,255,255])

                #movimentação do laborer
            checkpos = allies.move(janelajogo, tecladojogo, checkpos, laborer, velx, vely)
            if checkpos == 'W':
                if tecladojogo.key_pressed("W"):
                    laborer = allies.setposition(laborer,laborercima)
                    laborer.update()
                else:
                    laborer = allies.setposition(laborer,laborercima_idle)
            if checkpos == 'A':
                if tecladojogo.key_pressed("A"):
                    laborer = allies.setposition(laborer,laboreresquerda)
                    laborer.update()
                else:
                    laborer = allies.setposition(laborer,laboreresquerda_idle)
            if checkpos == 'S':
                if tecladojogo.key_pressed("S"):
                    laborer = allies.setposition(laborer,laborerbaixo)
                    laborer.update()
                else:
                    laborer = allies.setposition(laborer,laborerbaixo_idle)
            if checkpos == 'D':
                if tecladojogo.key_pressed("D"):
                    laborer = allies.setposition(laborer,laborerdireita)
                    laborer.update()
                else:
                    laborer = allies.setposition(laborer,laborerdireita_idle)
                #fim

            laborer.draw()
            menu_jogo.draw()
            portal_level.draw()

                #escrever as coisas dentro do visor portal level
            janelajogo.draw_text("Portal Level: ", janela_largura/2 + 470, 23, size=20, bold=True, color=(0, 0, 0))
            janelajogo.draw_text(str(portal_level_counter), janela_largura/2 + 595, 23.5, size=20, bold=True, color=(0, 0, 0))
            janelajogo.draw_text(str(portal_level_percent), janela_largura/2 + 482, 47, size=17, bold=True, color=(0, 0, 0))
            janelajogo.draw_text("% Chance of", janela_largura/2 + 493, 48, size=17, bold=True, color=(0, 0, 0))
            janelajogo.draw_text("spawning Ericis", janela_largura/2 + 474, 68, size=17, bold=True, color=(0, 0, 0))
                #fim
            
            if clickjogo.is_over_object(menu_jogo) and clickjogo.is_button_pressed(True):
                pygame.event.clear() #pra só capturar o input do mouse 1x
                if p_barra_botoes_jogo == True:
                    p_barra_botoes_jogo = False
                    while True:
                        janelajogo.set_background_color([255,255,255])
                        #redesenhar tudo
                        barra_botoes_jogo.draw()
                        botao_jogo_construct.draw()
                        botao_jogo_resources.draw()
                        botao_jogo_research.draw()
                        botao_jogo_reports.draw()
                        botao_jogo_options.draw()
                        menu_jogo.draw()
                        laborer.draw()

                        portal_level.draw()
                        #escrever as coisas dentro do visor portal level
                        janelajogo.draw_text("Portal Level: ", janela_largura/2 + 470, 23, size=20, bold=True, color=(0, 0, 0))
                        janelajogo.draw_text(str(portal_level_counter), janela_largura/2 + 595, 23.5, size=20, bold=True, color=(0, 0, 0))
                        janelajogo.draw_text(str(portal_level_percent), janela_largura/2 + 482, 47, size=17, bold=True, color=(0, 0, 0))
                        janelajogo.draw_text("% Chance of", janela_largura/2 + 493, 48, size=17, bold=True, color=(0, 0, 0))
                        janelajogo.draw_text("spawning Ericis", janela_largura/2 + 474, 68, size=17, bold=True, color=(0, 0, 0))
                        #fim


                        #menu construct
                        if clickjogo.is_over_object(botao_jogo_construct) and clickjogo.is_button_pressed(True):
                            while True:
                                barra_botoes2_jogo.draw()
                                botao_jogo_close.draw()
                                if clickjogo.is_over_object(botao_jogo_close) and clickjogo.is_button_pressed(True):
                                    break
                                janelajogo.update()

                        #menu resources
                        if clickjogo.is_over_object(botao_jogo_resources) and clickjogo.is_button_pressed(True):
                            while True:
                                barra_botoes2_jogo.draw()
                                botao_jogo_close.draw()
                                if clickjogo.is_over_object(botao_jogo_close) and clickjogo.is_button_pressed(True):
                                    break
                                janelajogo.update()

                        #menu research
                        if clickjogo.is_over_object(botao_jogo_research) and clickjogo.is_button_pressed(True):
                            while True:
                                barra_botoes2_jogo.draw()
                                botao_jogo_close.draw()
                                if clickjogo.is_over_object(botao_jogo_close) and clickjogo.is_button_pressed(True):
                                    break
                                janelajogo.update()

                        #menu reports
                        if clickjogo.is_over_object(botao_jogo_reports) and clickjogo.is_button_pressed(True):
                            while True:
                                barra_botoes2_jogo.draw()
                                botao_jogo_close.draw()
                                if clickjogo.is_over_object(botao_jogo_close) and clickjogo.is_button_pressed(True):
                                    break
                                janelajogo.update()

                        #menu options
                        if clickjogo.is_over_object(botao_jogo_options) and clickjogo.is_button_pressed(True):
                            while True:
                                barra_botoes2_jogo.draw()
                                botao_jogo_close.draw()
                                if clickjogo.is_over_object(botao_jogo_close) and clickjogo.is_button_pressed(True):
                                    break
                                janelajogo.update()

                        #fechar a barra de botões
                        if clickjogo.is_over_object(menu_jogo) and clickjogo.is_button_pressed(True):
                            break

                        janelajogo.update()
                else:
                    p_barra_botoes_jogo = True
            if tecladojogo.key_pressed("ESC"):
                break
            
            janelajogo.update()





    #botao settings
    if click.is_over_object(settings) and click.is_button_pressed(True):
        if p_settings == True:
            p_settings = False

            #janela do settings
            while True:
                janelasettings.draw()
                quit.draw()
                
                janela.draw_text("Settings", janela_largura/2 - 127, 90, size=60, bold=True, color=(224, 224, 222))
                janela.update()
                if click.is_over_object(quit) and click.is_button_pressed(True):
                    break
        else:
            p_settings = True

    #botao exit
    if click.is_over_object(exit) and click.is_button_pressed(True):
        janela.close()

    ###################

    #nos captamos o evento da mudanca se estado do bota
    #dessa forma o click so e registrado no primeiro momento
    #em que ocorre
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and click.is_over_object(music):
            if event.button == 1:
                if p_musica == True:
                    mixer.music.pause()
                    p_musica = False
                else:
                    mixer.music.unpause()
                    p_musica = True
    ###################
    
    #botao help
    if click.is_over_object(help) and click.is_button_pressed(True):
        if p_help == True:
            p_help = False

            #janela do help
            while True:
                janelahelp.draw()
                
                quit.draw()
                
                janela.draw_text("About", janela_largura/2 - 100, 90, size=60, bold=True, color=(224, 224, 222))
                janela.update()
                if click.is_over_object(quit) and click.is_button_pressed(True):
                    break
        else:
            p_help = True

        
        

    janela.update()
  