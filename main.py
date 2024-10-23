import pygame as pg
import os
from pygame.locals import*
from sys import exit
from random import randint, randrange
from OpenGL.GL import*
from fighter import Lutador
pg.init()

#files
file_principal = os.path.dirname(__file__)
file_image = os.path.join(file_principal, 'image')
file_song = os.path.join(file_principal, 'song')

#variaveis
largura = 1024
altura = 776
sair = False
fonte = pg.font.SysFont('ariel',50,True,True)
fonte2 = pg.font.SysFont('ariel',90,True,True)
musica = pg.mixer.music.load(os.path.join(file_song, 'game_music.wav'))
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play(-1)
#lista_head = []
#lista_snake = []
#pos_x = randint(150, 950)
#pos_y = randrange(100, 700, 50)
#screen.fill((0,0,0))
#screen.blit(naruto, (n_x,n_y), (s_x,s_y,80,80))
#pg.draw.rect(screen, (0,0,0), nave_rect, 1)
#nave_rect.x = nave_x
#nave_rect.y = nave_y
#pg.display.delay()
#pg.draw.rect(screen, (0,0,0), (x,y,40,40))
#pg.draw.circle(screen, (0,0,0), (pos_x,pos_y),20)
#pg.draw.line(screen, (0,0,0), (460,0), (460,777), 1)
#if lista_head.colliderect(lista_snake):
#if lista_snake.count(lista_head) > 1:
#global

#display
screen = pg.display.set_mode((largura,altura))
pg.display.set_caption("game")

som = pg.mixer.Sound(os.path.join(file_song, 'sword.wav'))
som.set_volume(0.5)

clouds = pg.image.load(os.path.join(file_image, 'clouds.png')).convert_alpha()
clouds = pg.transform.scale(clouds, (largura,altura))
#clouds = pg.transform.flip(clouds, True,False)
#clouds = pg.transform.rotate(clouds, -90)

fundo = pg.image.load(os.path.join(file_image, 'backgrounds.png')).convert_alpha()
fundo = pg.transform.scale(fundo, (largura,altura))


goku_lista = [pg.image.load(os.path.join(file_image, 'goku_idle.png')),
               pg.image.load(os.path.join(file_image, 'goku_ki.png')),
                pg.image.load(os.path.join(file_image, 'goku_run2.png')),
                 pg.image.load(os.path.join(file_image, 'goku_run1.png')),
                  pg.image.load(os.path.join(file_image, 'goku_jump.png')),
                   pg.image.load(os.path.join(file_image, 'goku_defense.png')),
                    pg.image.load(os.path.join(file_image, 'goku_attack.png'))]
                    
goku_dic = {'idle' : [],
             'ki' : [],
              'run1' : [],
               'run2' : [],
                'jump' : [],
                 'defense' : [],
                  'attack' : [],
            }
            
vegeta_lista = [pg.image.load(os.path.join(file_image, 'vegeta_idle.png')),
                 pg.image.load(os.path.join(file_image, 'vegeta_ki.png')),
                  pg.image.load(os.path.join(file_image, 'vegeta_run2.png')),
                   pg.image.load(os.path.join(file_image, 'vegeta_run1.png')),
                    pg.image.load(os.path.join(file_image, 'vegeta_jump.png')),
                     pg.image.load(os.path.join(file_image, 'vegeta_defense.png')),
                      pg.image.load(os.path.join(file_image, 'vegeta_attack.png'))]
                    
vegeta_dic = {'idle' : [],
               'ki' : [],
                'run1' : [],
                 'run2' : [],
                  'jump' : [],
                   'defense' : [],
                    'attack' : [],
              }

def imagens (dic, lista):
   for x, tipo in enumerate(dic):
      img_l = lista[x].get_width()
      img_a = lista[x].get_height()
      for i in range(int(img_l/img_a)):
          img = lista[x].subsurface(i*img_a,0,img_a,img_a)
          dic[tipo].append(pg.transform.scale(img, (img_a*3,img_a*4)))
   return(dic)
   
goku = imagens(goku_dic,goku_lista)
vegeta = imagens(vegeta_dic,vegeta_lista)

def lutador_saude(saude,x,y):
    mensagem = f'Ki : {saude}'
    mensagem2 = f'KO'
    texto = fonte.render(str(mensagem),True,(255,0,0))
    texto2 = fonte2.render(str(mensagem2),True,(255,0,0))
    pg.draw.rect(screen, (0,0,0), (x-3,y-3, 406,36))
    pg.draw.rect(screen, (80,80,80), (x,y, 400,30))
    pg.draw.rect(screen, (255,255,255), (x,y, 400*saude/100, 30))
    screen.blit(texto2, (460,5))
    screen.blit(texto, (x,y+35))

lutador_1 = Lutador(350,500) 
lutador_2 = Lutador(680,500)

#event
while not sair:
  pg.time.Clock().tick(12)
  screen.blit(clouds, (0,0))
  rel_x = largura % clouds.get_rect().width
  screen.blit(clouds, (rel_x - clouds.get_rect().width, 0))
  if rel_x < 1024:
     screen.blit(clouds, (rel_x,0))
  largura += 12
  screen.blit(fundo, (0,0))
  lutador_saude(lutador_1.saude, 20,20)
  lutador_saude(lutador_2.saude, 600,20)
  lutador_1.update(screen, 1, lutador_2, goku)
  lutador_2.update(screen, 2, lutador_1, vegeta)
  
  for e in pg.event.get():
    if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == K_ESCAPE:
       sair = True
       
  pg.display.flip()
  
exit