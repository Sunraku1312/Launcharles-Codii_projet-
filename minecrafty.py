from random import *
import pygame
from time import *

pygame.init()

screen = pygame.display.set_mode((320,222))

def fill_rect(x, y, longueur, hauteur, couleur):
  pygame.draw.rect(screen, couleur, pygame.Rect(x, y, longueur, hauteur))

def draw_string(mot, x, y, couleur_texte, couleur_arriere):
  font = pygame.font.Font(None, 36)  
  texte = font.render(mot, True, couleur_texte) 
  text_rect = texte.get_rect(topleft=(x, y))
    

  pygame.draw.rect(screen, couleur_arriere, text_rect)
    
  screen.blit(texte, text_rect.topleft)



o=1
e=1
s=0
t=0
cx=-2
vie=100
armure=80
ex=(0,0)
direction=(0,0)

break_mode=(
(4,3,0,3,4),
(0,0,2,0,0),
(3,0,1,0,3),
(4,0,2,2,0),
(0,3,0,0,4),
)

map=[
[0,0,0,0,0,0,0,0,4,4,4 ,4,4 ,4,0 ,0 ,0,0 ,0 ,0,0 ,0 ,0 ,25,25,25,25,25,0 ,0 ,25,25,25,25,25,25,25,0,0,5,5,5,0,0,0,1,3 ,3 ,3 ,10,3,1 ,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5 ,5,0,0,0 ,0,0,1 ,2,3 ,11,3 ,2,1 ,0,0,0,0,0,0 ,0,0 ,0 ,0 ,0,0,0,0,0,1,2,2 ,3 ,3,11,3 ,3,3,11,3 ,3 ,10,3,11,3,3 ,3,3 ,3,2,1,0,0,0,5,5,5,5,0,0,0 ,0,1,0,0,0,0,0,48,16,14,14,16,16,16,16,16,16,34,34,34,16,16,14,14,16,16,30,30,22,22,30,30,30,30,30,30,16,16,16,34,34,22,22,22,22,22,22,14,22,45,45,45,22,22,22,43,22,22,22,48,0,5,5,5,0,0,0,0,1 ,2,2,3 ,11,2 ,1,0,0,0,0,5,5,5 ,0,0,0,1,2,3 ,3,3,3 ,3,0 ,0 ,0 ,0 ,0 ,0 ,0 ,20,23,23,23,23,23,23,23,23,23,27,27,23,23,23,23,23,23,23,23,23,23,20,20,20,20,20,20,20,20,47,47,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,38,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0,0,0,5,5,5,0,0],
[0,0,0,5,5,0,0,0,4,0,0 ,7,7 ,4,0 ,0 ,9,0 ,0 ,9,0 ,0 ,0 ,25,26,26,26,25,0 ,0 ,25,26,26,26,26,26,25,0,0,5,4,5,0,0,1,2,3 ,11,3 ,3 ,3,10,1,1,0,1,1,1,0,0,0,0,0,0,5,5,25,5,5,0,24,0,1,2 ,3,3 ,9 ,3 ,3,2 ,1,0,0,0,0,24,1,13,13,13,1,0,0,0,0,2,2,3 ,10,3,3 ,3 ,3,0,0 ,3,11,3 ,12,3 ,3,11,3,3 ,3,2,2,1,0,5,5,4,4,5,5,0,24,1,2,1,0,0,0,0,21,16,16,14,22,16,16,22,22,22,22,22,34,16,14,14,14,16,30,16,22,22,31,30,22,22,31,22,22,22,16,22,22,22,22,22,22,43,22,22,14,22,45,44,45,22,22,22,43,41,22,22,21,0,5,4,5,0,0,0,9,40,0,2,3 ,3 ,3 ,2,1,0,0,0,5,4,5 ,0,0,0,2,2,3 ,3,0,0 ,0,0 ,0 ,49,50,50,50,49,20,23,23,23,23,23,23,23,23,23,27,27,23,23,23,23,23,28,23,23,23,23,20,20,0 ,0 ,0 ,0 ,0 ,47,47,20,0 ,0 ,0 ,0 ,0 ,38,0 ,37,37,0 ,0 ,0 ,0 ,38,0 ,0 ,38,0 ,0 ,0 ,38,0 ,0 ,0 ,0,0,0,5,4,5,0,0],
[0,0,5,5,5,5,0,0,0,0,33,0,15,4,0 ,0 ,3,13,13,3,0 ,0 ,9 ,25,26,0 ,26,25,9 ,0 ,25,26,26,40,26,26,25,0,0,0,4,0,0,1,2,3,10,9 ,3 ,11,3,3 ,3,2,1,2,2,2,1,0,0,0,1,0,0,0,25,0,0,0,1 ,1,2,10,3,12,3 ,10,3,3 ,2,1,0,0,0,1 ,2,2 ,13,13,2,1,0,0,1,2,2,3 ,3 ,3,3 ,10,0,9,36,0,3 ,3 ,3 ,3 ,3,3 ,3,12,3,3,2,2,1,0,0,4,4,0,0,0,1 ,2,3,2,1,0,0,0,21,22,22,14,22,22,22,22,16,16,16,16,16,16,14,14,14,14,14,14,22,30,22,22,22,22,30,17,31,22,22,22,16,22,22,22,22,43,22,43,14,22,22,44,22,22,42,42,42,42,42,22,21,0,0,4,0,0,0,0,1,1 ,1,3,11,3 ,3 ,3,2,1,0,0,0,4,24,0,0,1,2,3,12,3,0,0 ,0,0 ,20,20,23,23,23,23,23,23,23,23,18,18,18,23,23,23,27,27,23,23,23,23,23,20,23,23,23,23,20,20,9 ,46,9 ,20,20,20,20,20,0 ,39,0 ,37,37,37,37,37,37,37,37,37,0 ,38,0 ,0 ,37,37,0 ,0 ,38,0 ,37,37,1,0,0,0,4,0,0,0],
[1,1,1,1,1,1,1,1,3,3,3 ,3,3 ,3,32,32,3,3 ,3 ,3,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,1,1,1,2,1,1,3,3,3,3 ,3 ,12,3 ,3,11,3,3,2,3,3,2,2,1,1,1,2,1,1,1,1 ,1,1,1,2 ,2,3,11,3,11,3 ,3 ,3,10,3,2,1,1,1,2 ,2,14,15,13,3,2,1,1,2,2,3,12,3 ,3,3 ,11,3,3,3 ,3,3 ,3 ,3 ,3 ,3,3 ,3,3 ,3,3,3,2,2,1,1,1,1,1,1,1,2 ,3,3,3,2,1,1,1,48,16,16,14,16,16,16,35,16,14,14,14,14,16,14,14,16,35,16,30,30,30,30,30,30,30,30,30,30,30,30,16,16,16,16,16,42,42,42,42,14,42,42,42,42,42,16,35,35,16,16,42,48,1,1,1,1,1,1,1,2,2 ,3,3,3 ,3 ,12,3,2,2,1,1,1,1,1 ,1,1,2,2,3,3 ,3,3,11,3,20,20,20,18,18,18,18,18,18,18,18,18,18,18,18,18,18,15,15,18,18,18,20,29,20,29,20,18,18,20,20,20,20,20,20,20,20,20,20,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,2 ,2,1,1,1,1,1,1,1],
]

max_map=len(map[1])

blocks=(
("air",10000,6,1,1,((0,0,50,50,(130,230,255)),)),
("gazon",10,4,0,0,((0,10,50,40,(190,90,0)),(0,0,50,10,(0,220,0)))),
("terre",10,4,0,0,((0,0,50,50,(190,90,0)),)),
("pierre",40,2,0,0,((0,0,50,50,(180,180,180)),)),
("buche",20,3,0,0,(((0,0,50,50,(200,100,10)),(20,0,10,50,(210,110,20))))),
("feuille",2,3,0,0.75,((0,0,50,50,(100,120,0)),)),
("table",15,3,0,0,()),
("planche",15,3,0,0,((0,0,50,50,(230,130,40)),(0,20,50,10,(210,110,20)),)),
("four",30,2,0,0,()),
("torche",10,3,1,1,((0,0,50,50,(130,230,255)),(20,20,10,30,(200,100,10)),(20,20,10,10,(255,255,0)),)),
("minerai_charbon",50,2,0,0,((0,0,50,50,(180,180,180)),(10,30,10,10,(20,20,20)),(30,10,10,10,(20,20,20)))),
("minerai_fer",50,2,0,0,((0,0,50,50,(180,180,180)),(10,30,10,10,(250,100,100)),(30,10,10,10,(250,100,100)))),
("diamant",40,2,0,0,((0,0,50,50,(180,180,180)),(10,30,10,10,(0,255,255)),(30,10,10,10,(0,255,255)))),
("eau",10000,5,0.75,0.5,((0,0,50,50,(0,0,180)),)),
("lave",10000,5,0.25,0.5,((0,0,50,50,(255,100,0)),)),
("obsidienne",200,2,0,0,((0,0,50,50,(0,0,20)),)),
("pierre_trefond",40,2,0,0,((0,0,50,50,(100,20,256)),)),
("spawner",200,2,0,0,((0,0,50,50,(230,30,20)),(0,0,50,10,(0,0,1)),(0,40,50,10,(0,0,1)),(0,20,50,1,(0,0,1)),(0,30,50,1,(0,0,1)),(20,0,1,50,(0,0,1)),(30,0,1,50,(0,0,1)),(10,0,1,50,(0,0,1)),(40,0,1,50,(0,0,1)))),
("pierre_ender",80,2,0,0,((0,0,50,50,(220,220,130)),)),
(),
("bedrock",10000,2,0,1,((0,0,50,50,(150,150,150)),)),
("portail_n",10000,0,1,1,((0,0,50,50,(210,0,150)),)),
("air_netheur",10000,6,1,1,((0,0,50,50,(230,30,20)),)),
("air_end",10000,6,1,1,((0,0,50,50,(0,0,120)),)),
("zombie",1,1,1,1,((0,0,50,50,(130,230,255)),(15,10,20,40,(0,0,200)),(15,0,20,20,(0,100,0)),(5,22,10,10,(0,100,0)),(17,5,5,5,(255,255,255)),(24,5,5,5,(255,255,255)),(18,7,2,2,(0,0,1)),(25,7,2,2,(0,0,1)))),
("buche_fake",10000,3,1,0,(((0,0,50,50,(200,100,10)),(20,0,10,50,(210,110,20))))),
("planche_f",10000,3,1,0,((0,0,50,50,(230,130,40)),(0,20,50,10,(210,110,20)),)),
("obsidienne_f",10000,2,1,0,((0,0,50,50,(0,0,20)),)),
("euf_dragon",10,2,0,0,((0,0,50,50,(0,0,120)),(5,30,40,20,(0,0,20)),(10,20,30,10,(0,0,20)),(15,15,20,5,(0,0,20)),)),
("portal_e_f",10000,2,1,0,((0,0,50,50,(0,0,1)),)),
("br_f",400,2,0,1,((0,0,50,50,(100,30,0)),(0,25,50,5,(0,0,1)),(15,0,5,25,(0,0,1)),(40,50,-5,-25,(0,0,1)),)),
("blaze",1,2,1,0,((0,0,50,50,(230,30,20)),(5,10,5,20,(230,230,0)),(40,17,5,20,(230,230,0)),(15,5,20,20,(230,230,0)),(18,8,5,5,(255,255,255)),(31,8,-5,5,(255,255,255)),(27,27,5,20,(230,230,0)),(19,9,3,3,(0,0,1)),(27,9,3,3,(0,0,1)),(15,29,5,20,(230,230,0)),)),
("bk_che",10,4,0,0,((0,10,50,40,(190,90,0)),(0,0,50,10,(220,220,0)))),
("villa_forge",10000,1,1,1,((0,0,50,50,(130,230,255)),(15,0,20,20,(233,158,67)),(15,20,20,30,(157,90,0)),(22,13,7,12,(180,120,0)),(19,6,5,5,(255,255,255)),(20,7,3,3,(0,0,1)),(26,6,5,5,(255,255,255)),(27,7,3,3,(0,0,1)),)),
("mine_o",50,2,0,0,((0,0,50,50,(100,20,256)),(10,30,10,10,(250,250,0)),(30,10,10,10,(250,250,0)))),
("mine_q",50,2,0,0,((0,0,50,50,(100,20,256)),(10,30,10,10,(255,255,255)),(30,10,10,10,(255,255,255)))),
("villageois_mineure",10000,1,1,1,((0,0,50,50,(130,230,255)),(15,0,20,20,(233,158,67)),(15,20,20,30,(0,0,30)),(22,13,7,12,(180,120,0)),(19,6,5,5,(255,255,255)),(20,7,3,3,(0,0,1)),(26,6,5,5,(255,255,255)),(27,7,3,3,(0,0,1)),(15,0,20,4,(0,0,30)),(35,30,3,8,(200,100,10)),(31,27,10,3,(255,255,255)),)),
("sable",5,2,0,0,((0,0,50,50,(255,255,110)),)),
("cactus",5,2,1,0,((0,0,50,50,(130,230,255)),(5,0,40,50,(0,105,0)),(2,10,10,3,(200,200,200)),(2,20,10,3,(200,200,200)),(2,30,10,3,(200,200,200)),(2,40,10,3,(200,200,200)),(38,40,10,3,(200,200,200)),(38,10,10,3,(200,200,200)),(38,20,10,3,(200,200,200)),(38,30,10,3,(200,200,200)),)),
("villageois_marchand",10000,1,1,1,((0,0,50,50,(130,230,255)),(15,0,20,20,(243,168,77)),(15,20,20,30,(0,0,120)),(22,13,7,12,(200,140,0)),(19,6,5,5,(255,255,255)),(20,7,3,3,(0,140,0)),(26,6,5,5,(255,255,255)),(27,7,3,3,(0,140,0)),(15,0,20,4,(0,0,140)),)),
("villageois_coeure",10000,1,1,1,((0,0,50,50,(130,230,255)),(15,0,20,20,(233,158,67)),(15,20,20,30,(255,0,255)),(22,13,7,12,(180,120,0)),(19,6,5,5,(255,255,255)),(20,7,3,3,(0,0,1)),(26,6,5,5,(255,255,255)),(27,7,3,3,(0,0,1)),)),
("villageois_pingline",10000,1,1,1,((0,0,50,50,(230,30,20)),(15,0,20,20,(255,130,135)),(15,20,20,30,(170,80,60)),(22,13,7,9,(215,70,105)),(19,6,5,5,(255,255,255)),(20,7,3,3,(120,120,0)),(26,6,5,5,(255,255,255)),(27,7,3,3,(120,120,0)),)),
("gazon_netheure",10,4,0,0,((0,10,50,40,(100,20,256)),(0,0,50,10,(0,150,250)),)),
("liane_netheure",10,5,0.75,0.5,((0,0,50,50,(230,30,20)),(20,25,10,25,(0,150,255)),(10,0,10,25,(0,150,255)),)),
("bu_netheure",10000,3,1,0,(((0,0,50,50,(0,100,190)),(15,0,20,50,(0,150,255))))),
("fe_netheure",10000,3,1,0.75,((0,0,50,50,(0,150,250)),)),
("hero",10000,1,1,1,((0,0,50,50,(130,230,255)),(15,0,20,20,(250,160,130)),(15,20,20,30,(0,0,255)),(19,6,5,5,(255,255,255)),(26,6,5,5,(255,255,255)),)),
("bedrock_f",10000,2,1,1,((0,0,50,50,(150,150,150)),)),
("o",10000,2,0,0,((0,0,50,50,(0,0,20)),)),
("",10000,3,0,0,((0,0,50,50,(130,230,255)),(0,10,50,40,(220,220,130)),(0,10,50,10,(0,100,0)),(8,0,34,10,(0,170,0)),(20,0,10,8,(0,0,1)))),
("",10000,2,1,0,((0,0,50,50,(130,230,255)),(0,10,50,40,(0,0,1)),)),
("",10000,2,1,0,((0,0,50,50,(230,230,230)))),
)

inv=[
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]
]

selectY=0
select=0

def casser(outil=0):
  if not -1<p.y+direction[1]<4:
    return
  block=blocks[map[p.y+direction[1]][(p.x+direction[0])%max_map]]
  outil_destine=block[2]
  temps=0.2*block[1]/10
  if outil!=0:
    if outil_destine==outil%10:
      temps/=2
    else:
      temps*=2
    temps/=(int(outil/10)-3)+1

  if block[1]==10000:
    return
  for h in range(1,5):
    for i in range(0,5):
      for j in range(0,5):
        if h==break_mode[i][j]:
          fill_rect(50*(p.x-cx+direction[0])+10*i,50*(p.y+direction[1])+10*j,10,10,(0,0,0))
    sleep(temps)
  if o==1 :
    map[p.y+direction[1]][(p.x+direction[0])%max_map]=0
  if o==2 :
    map[p.y+direction[1]][(p.x+direction[0])%max_map]=22
  if o==3 :
    map[p.y+direction[1]][(p.x+direction[0])%max_map]=23


class Perso():
  def __init__(self):
    self.x=0
    self.y=0

  def move(self,x,y):
    global direction,cx
    direction=(x,y)
    keydown = pygame.key.get_pressed()
    if keydown[pygame.K_LSHIFT] or self.y + y in (-1, 4):
      return
    if blocks[map[(self.y+y)%4][(self.x+x)%max_map]][3]>0:
      self.x+=x
      self.y+=y
    if cx+4<self.x or self.x<cx+1:
      cx+=x


  def draw(self):
    rx=(self.x-cx)*50
    ry=self.y*50
    fill_rect(rx+15,ry+10,20,40,(0,0,220))
    fill_rect(rx+15,ry,20,20,(250,160,130))

    fill_rect(rx+18,ry+5,5,5,(255,255,255))
    fill_rect(rx+27,ry+5,5,5,(255,255,255))

    fill_rect(rx+19+(direction[0]),ry+6+(direction[1]),3,3,(0,0,1))
    fill_rect(rx+28+(direction[0]),ry+6+(direction[1]),3,3,(0,0,1))
    
    if 0<inv[0][select%6]<20:
      block=blocks[inv[0][select]]
      for k in block[5]:
        fill_rect(int(30+rx+(k[0]*1/5)),int(30+ry+(k[1]*1/5)),int(k[2]*1/5),int(k[3]*1/5),k[4])
    if 30<inv[0][select%6]<80:
      draw_outil(30+rx,30+ry,1/5,inv[0][select%6]-30)

p=Perso()


def draw():
  if open_inv:
    draw_inv()
    bouger_inv()
    return
  else:
    for i in range(0,4):
      for j in range(0,7):
        block=blocks[map[i][(j+(cx))%max_map]]
        for k in block[5]:
          fill_rect(k[0]+(j*50),k[1]+(i*50),k[2],k[3],k[4])

    p.draw()

  if armure!=ex[0] or vie!=ex[1]:
    draw_life()

def draw_life():
  global ex
  ex=(armure,vie)
  fill_rect(0,200,320,22,(255,255,255))
  fill_rect(0,200,int(armure/100*320),22,(120,120,150))
  fill_rect(3,203,int(vie/100*314),16,(255,0,0))

drawed_inv=0

def draw_inv():
  global drawed_inv
  if drawed_inv:
    return

  fill_rect(20,20,280,160,(125,225,250))
  for i in range(0,6):
    for j in range(0,3):

      if i==select and j==selectY:
        fill_rect(27+i*45-5,10*(j!=0)+30+j*45-5,50,50,(220,200,200))

      if 0<=inv[j][i]<20:
        block=blocks[inv[j][i]]
        for k in block[5]:
          fill_rect(int(27+i*45+(k[0]*4/5)),int(10*(j!=0)+30+j*45+(k[1]*4/5)),int(k[2]*4/5),int(k[3]*4/5),k[4])
      elif 30<inv[j][i]<80:
        draw_outil(27+i*45,10*(j!=0)+30+j*45,4/5,inv[j][i]-30)
      else:
        fill_rect(27+i*45,10*(j!=0)+30+j*45,40,40,(0,0,0))
  drawed_inv=1

open_inv=0  

def draw_outil(x,y,scale,id):
  couleur=((200,100,10),(180,180,180),(235,235,235),(0,255,255),(130,50,60),)[int(id/10)]
  if id%10==1:
    fill_rect(x+int(15*scale),y+int(5*scale),int(20*scale),int(30*scale),couleur)
    fill_rect(x+int(20*scale),y+int(35*scale),int(10*scale),int(15*scale),(220,120,30))

  if id%10==2:
    fill_rect(x+int(5*scale),y+int(5*scale),int(40*scale),int(10*scale),couleur)
    fill_rect(x+int(20*scale),y+int(15*scale),int(10*scale),int(30*scale),(220,120,30))

  if id%10==3:
    fill_rect(x+int(20*scale),y,int(25*scale),int(10*scale),couleur)
    fill_rect(x+int(30*scale),y+int(10*scale),int(15*scale),int(10*scale),couleur)
    fill_rect(x+int(20*scale),y+int(10*scale),int(10*scale),int(35*scale),(220,120,30))

  if id%10==4:
    fill_rect(x+int(15*scale),y+int(5*scale),int(20*scale),int(20*scale),couleur)
    fill_rect(x+int(20*scale),y+int(25*scale),int(10*scale),int(25*scale),(220,120,30))


def bouger_inv():
  keydown = pygame.key.get_pressed()
  global select,selectY,drawed_inv
  if not open_inv:
    return
  for i in range(18):
    if keydown[i+30]:
      if keydown[pygame.K_t]:
        inv[int(i/6)][i%6],inv[selectY][select]=inv[selectY][select],inv[int(i/6)][i%6]
      else:
        selectY=int(i/6)
        select=i%6
  for i in range(4):
    if keydown[i]:
      select=(select+(-1,0,0,1)[i])%6
      selectY=(selectY+(0,-1,1,0)[i])%3

  drawed_inv=0
  draw_inv()

while True:
  draw()
  sleep(0.2)
  keydown = pygame.key.get_pressed()
  if keydown[pygame.K_e]:
    drawed_inv=0
    open_inv=1-open_inv
  if open_inv:
    continue

  if p.y<3:
    if blocks[map[(p.y+1)%4][p.x%max_map]][3]==1 and p.y<3:
      p.y+=1
  if map[p.y][p.x%max_map]==14:
    vie-=8-(5*(vie<=armure))
    cdm='steavy est une saussice griller'
  if map[p.y][p.x%max_map]==24:
    cdm='steavy est un zombie'
    vie-=10-(5*(vie<=armure))
  if map[p.y][p.x%max_map]==31:
    cdm='steavy est en feu'
    vie-=20-(5*(vie<=armure))
  if map[p.y][p.x%max_map]==33:   
    if e==1 :
      inv=[
      [0,41,42,3,4,13],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0]
      ]
      e=2
  if map[p.y][p.x%max_map]==41:   
    if e==4 :
      inv=[
      [0,71,72,3,4,13],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0]
      ]
      e=5     
  if map[p.y][p.x%max_map]==36 :
    if e==2 :
      inv=[
      [0,51,52,3,4,13],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0]
      ]
      e=3
  if map[p.y][p.x%max_map]==39 :
    if e==3 :
      inv=[
      [0,61,62,3,4,13],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0]
      ]
      e=4
  if map[p.y][p.x%max_map]==0:
    o=1
  if map[p.y][p.x%max_map]==22:
    o=2
  if map[p.y][p.x%max_map]==23 or map[p.y][p.x%max_map]==50 :
    o=3
  if map[p.y][p.x%max_map]==46:
    s=1
  if s==1 :
    fill_rect(0,0,400,250,(255,255,255))         
  if map[p.y][p.x%max_map]==29 :
    fill_rect(0,0,400,250,(0,0,190))    
    draw_string("gg t as termine",90,60,(0,0,255),(0,0,190))
    bcl=0 
    while bcl==0 :
      a=0
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            bcl=1
            p.move(47,-3)
            direction=(0,0)
            vie=99+1                 
  if vie<=0 :
    fill_rect(0,0,400,250,(150,0,0))
    draw_string("game over",100,100,(255,0,0),(150,0,0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    a=0

  for i in range(6):
    if keydown[12+i]:
      select=i

  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        if 0<inv[0][select%6]<20:
          if map[(p.y+direction[1])%4][(p.x+direction[0])%max_map] in (0,13,14,22,23):
            map[(p.y+direction[1])%4][(p.x+direction[0])%max_map]=inv[0][select]
        else:
          casser(inv[0][select%6])

  if keydown[pygame.K_SPACE] and (map[(p.y+1)%4][p.x%max_map]!=0 or p.y==3) or keydown[pygame.K_z] and (map[(p.y+1)%4][p.x%max_map]!=0 or p.y==3) or keydown[pygame.K_UP] and (map[(p.y+1)%4][p.x%max_map]!=0 or p.y==3) or keydown[pygame.K_w] and (map[(p.y+1)%4][p.x%max_map]!=0 or p.y==3):
    p.move(0,-1)
  if keydown[pygame.K_s] or keydown[pygame.K_DOWN]:
    p.move(0,1)
  if keydown[pygame.K_q] or keydown[pygame.K_LEFT] or keydown[pygame.K_a]:
    p.move(-1,0)
  if keydown[pygame.K_d] or keydown[pygame.K_RIGHT]:
    p.move(1,0)
  if keydown[pygame.K_1]:
    select=0
  if keydown[pygame.K_2]:
    select=1
  if keydown[pygame.K_3]:
    select=2
  if keydown[pygame.K_4]:
    select=3
  if keydown[pygame.K_5]:
    select=5
  if keydown[pygame.K_ESCAPE]:
    pygame.quit()
  if map[p.y][p.x%max_map]==40 :
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if vie < 100 :
            vie=vie+1

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LSHIFT] and keys[pygame.K_l] :
    pygame.quit()
    import launcharles as launcharles

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  pygame.display.flip()