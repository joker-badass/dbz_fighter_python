import pygame as pg
import os
from pygame.locals import*
from sys import exit
from random import randint , randrange
from OpenGL.GL import*
pg.init()

#files
file_principal = os.path.dirname(__file__)
file_image = os.path.join(file_principal, 'image')
file_song = os.path.join(file_principal, 'song')

#class
class Lutador():
    def __init__(self,x,y):
        self.rect = pg.Rect((x,y ,80,180))
        self.y = y
        self.image = 0
        self.atual = 0
        self.saude = 100
        
    def update(self, screen, lutador, oponente, lut_dic):
        lutador_image = lut_dic['idle'][self.atual]
        self.atual += 1
        if self.atual >= len(lut_dic['idle']):
           self.atual = 0
           
        move = pg.key.get_pressed()
        if move[pg.K_q] and lutador == 1 or move[pg.K_y] and lutador == 2:
           if self.atual >= len(lut_dic['ki']):
              self.atual = 0
           lutador_image = lut_dic['ki'][self.atual]
           self.saude += 5
           if self.saude > 100:
              self.saude = 100
              
              
        if move[pg.K_a] and lutador == 1 or move[pg.K_LEFT] and lutador == 2:
           if self.atual >= len(lut_dic['run1']):
              self.atual = 0
           lutador_image = lut_dic['run1'][self.atual]
           self.rect.x -= 60
           if self.rect.x < 150:
              self.rect.x = 150
              
           if self.rect.centerx < oponente.rect.centerx:
              lutador_image = lut_dic['run2'][self.atual]
           if self.rect.centerx > oponente.rect.centerx:
              lutador_image = lut_dic['run1'][self.atual]
              
        if move[pg.K_d] and lutador == 1 or move[pg.K_RIGHT] and lutador == 2:
           if self.atual >= len(lut_dic['run2']):
              self.atual = 0
           lutador_image = lut_dic['run2'][self.atual]
           self.rect.x += 60
           if self.rect.x > 950:
              self.rect.x = 950
              
           if self.rect.centerx < oponente.rect.centerx:
              lutador_image = lut_dic['run1'][self.atual]
           if self.rect.centerx > oponente.rect.centerx:
              lutador_image = lut_dic['run2'][self.atual]
              
        if move[pg.K_SPACE] and lutador == 1 or move[pg.K_m] and lutador == 2:
           if self.atual < len(lut_dic['jump']):
              self.atual = 0
           lutador_image = lut_dic['jump']
           self.rect.y -= 200
           if self.rect.y < 300:
              self.rect.y = 300
         
        if self.y != self.rect.y:
           self.rect.y += 80
           if self.atual >= len(lut_dic['jump']):
              self.atual = 0
           lutador_image = lut_dic['jump'][self.atual]
           if self.rect.y > 500:
              self.rect.y = 500

        if move[pg.K_w] and lutador == 1 or move[pg.K_UP] and lutador == 2:
           if self.atual >= len(lut_dic['idle']):
              self.atual = 0
           lutador_image = lut_dic['idle'][self.atual]
           self.rect.y -= 200
           if self.rect.y < 150:
              self.rect.y = 150           
           
        if move[pg.K_s] and lutador == 1 or move[pg.K_DOWN] and lutador == 2:
           if self.atual >= len(lut_dic['jump']):
              self.atual = 0
           lutador_image = lut_dic['jump'][self.atual]
           self.rect.y += 80
           if self.rect.y < 500:
              self.rect.y = 500
              
        if self.image != 0:
           if self.image < len(lut_dic['attack']):
              lutador_image = lut_dic['attack'][self.image]
              self.image += 1
           else:
              self.image = 0
              
              
        if move[pg.K_t] and lutador == 1 and self.image == 0 or move[pg.K_p] and lutador == 2 and self.image == 0:
           som = pg.mixer.Sound(os.path.join(file_song, 'sword.wav'))
           som.set_volume(0.5)
           som.play()
           lutador_image = lut_dic['attack'][self.image]
           self.image = 1
           self.rect.x -= 60
           if self.rect.x < 150:
              self.rect.x = 150
              
           if self.rect < oponente.rect:
              self.rect.x += 120
              if self.rect.x > 950:
                 self.rect.x = 950
                 
           if self.rect.centerx < oponente.rect.centerx:
              ataque = pg.Rect((self.rect.right, self.rect.y,80,180))
           else:
              ataque = pg.Rect((self.rect.left-80, self.rect.y,80,180))
              
           if ataque.colliderect(oponente.rect) and oponente.image == 0:
              som2 = pg.mixer.Sound(os.path.join(file_song, 'gokudesgracado.ogg'))
              som2.set_volume(0.5)
              som2.play()
              oponente.saude -= 10
              if oponente.saude < 0:
                 oponente.saude = 0
                 
        if move[pg.K_r] and lutador == 1 or move[pg.K_o] and lutador == 2:
           if self.atual >= len(lut_dic['defense']):
              self.atual = 0
           lutador_image = lut_dic['defense'][self.atual]
           self.atual += 1
              
           if self.rect.centerx < oponente.rect.centerx:
              defesa = pg.Rect((self.rect.right, self.rect.y,80,180))
           else:
              defesa = pg.Rect((self.rect.left-80, self.rect.y,80,180))
              
           if defesa.colliderect(oponente.rect) and oponente.image == 1:
              self.saude += 10
              
        if self.rect.centerx > oponente.rect.centerx:
           lutador_image = pg.transform.flip(lutador_image, True,False)
        if lutador == 1:
           screen.blit(lutador_image, (self.rect.x-100, self.rect.y-100))
        else:
           screen.blit(lutador_image, (self.rect.x-100, self.rect.y-100))        