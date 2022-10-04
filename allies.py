from pygame import mixer
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import pygame


#para determinar a posição que eu quero que o boneco vire
def setposition(atual,quero):
    ally = quero
    ally.x = atual.x
    ally.y = atual.y
    return ally

#para fazer o boneco se movimentar
def move(janela, keyboard, checkpos, ally, velx, vely):
    if keyboard.key_pressed("W") and ally.y >= 0:
        ally.y -= vely * janela.delta_time()
        checkpos = 'W'
    if keyboard.key_pressed("S") and ally.y + ally.height <= janela.height:
        ally.y += vely * janela.delta_time()
        checkpos = 'S'
    if keyboard.key_pressed("D") and ally.x + ally.width <= janela.width:
        ally.x += velx * janela.delta_time()
        checkpos = 'D'
    if keyboard.key_pressed("A") and ally.x >= 0:
        ally.x -= vely * janela.delta_time()
        checkpos = 'A'
    return checkpos

