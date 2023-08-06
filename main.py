import pygame
from pygame.locals import *

import json
import os
import sys
import importlib
from inspect import isfunction
import random
import time

def call_func(full_module_name, func_name, *args, **kwargs):
    module = importlib.import_module(full_module_name)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if isfunction(attribute) and attribute_name == func_name:
            attribute(*args, **kwargs)


pygame.init()

global path
path = os.path.dirname(os.path.realpath(__file__))
f = open(f'{path}\\data\\config\\config.json')
configA = json.load(f)
config = configA['config']

debug = config["debug"]

width, height = config["resolution"]["width"], config["resolution"]["height"]

clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))
screen = win
display = win
pygame.display.set_caption("Game Engine", config['version'])



## Static variables

# color
black = (0, 0, 0)
white = (255, 255, 255)
grey = (100,100,100)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
sky_blue = (135, 206, 250)
light_blue = (155, 155, 255)

#Fonts
fontSize = 25
font = pygame.font.Font(None, fontSize)

Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Images


assetList = [["box"]]
assetList2 = [["floor"],["grass"],["hole"],["dirt"]]

allAssets = []
userAssets = []

for i in range(len(assetList)):
    allAssets.append(pygame.image.load(
        f'{path}//data//assets//programImages//{assetList[i][0]}.png'))


for i in range(len(assetList2)):
    userAssets.append(pygame.image.load(f'{path}//data//assets//userPacks//{assetList2[i][0]}.png'))



## END
taskbarPos = [[10,height-70],[80,height-70],[150,height-70],[220,height-70],[290,height-70]]
taskbarPoscopy = [[10,height-70],[80,height-70],[150,height-70],[220,height-70],[290,height-70]]

clicked = [False, 0]

def drawTaskbar():
  global clicked
  taskbarPoscopy = [[10,height-70],[80,height-70],[150,height-70],[220,height-70],[290,height-70]]
  mousePos = pygame.mouse.get_pos()
  index = 0
  for item in taskbarPos:
    if colide(mousePos[0], mousePos[1], item[0], item[1], 60,60):
      if pygame.mouse.get_pressed() == (True, False, False):
        clicked = [True, index]
        
      win.blit(pygame.transform.scale(allAssets[0], (60,60)), (item[0], (item[1]-10)))
      taskbarPoscopy[index] = [item[0], (item[1]-10)]
    else:
      win.blit(pygame.transform.scale(allAssets[0], (60,60)), (item[0], item[1]))
    index += 1
    
  for i in range(len(userAssets)):
    win.blit(pygame.transform.scale(userAssets[i], (50,50)), ((taskbarPoscopy[i][0]+5), (taskbarPoscopy[i][1])+5))
    
def save(data):
  if not os.path.exists(f'{path}//data//save//save.json'):
    with open(f'{path}//data//save//save.json', 'x') as f:
      pass
  with open(f'{path}//data//save//save.json', 'w') as f:
        data2 = json.dumps(data)
        f.write(str(data2))
        
def load():
  try:
    with open(f'{path}//data//save//save.json', 'r') as f:
        data = json.load(f)
        return data
  except FileNotFoundError:
    print("file not found")
    

def colide(x1,y1,x2,y2,sizex,sizey):
  if x1 >= x2 and x1 <= (x2 + sizex):
      if y1 >= y2 and y1 <= (y2 + sizey):
        return True
      else:
        return False
  else:
    return False
  
  
  
spriteCode = """from main import *

def init():
    x = 0
    y = 0
    xvel = 0
    yvel = 0
    print(f"Init {name}")
  
  
def tick(): # Runs every frame
    print(f"ran frame: {name}")
    pass """
    
  
  


tiles = []
sprites = []

def newSprite():
  LoadingText = "Loading..."
  win.blit(font.render("{}".format(LoadingText),True, white), ((width/2)-(len(LoadingText)-fontSize), (height/2)))
  pygame.display.update()
  name = input("Enter Sprite Name (noSpaces): ")
  sprites.append(name)
  with open(f"./data/code/{name}.py","x") as f:
    f.write(f"#Code for Sprite: {name}\n\nname = '{name}'\n\n")
    f.write(spriteCode)
  call_func(f"data.code.{name}","init")
  time.sleep(0.5)
  return 
  
  
  
def tickSprites():
  for spriteName in sprites:
    print(f"Ticked {spriteName[0]}, {sprites}")
    try:
      call_func(f"data.code.{spriteName[0]}","tick")
    except FileNotFoundError:
      print(f"FileNotFoundError: {spriteName[0]}\n")

  




while True:  # game loop
    display.fill(grey)  # clear screen by filling it with blue
    pressed= False
    mousePos = pygame.mouse.get_pos()

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
          pressed = True
          
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
          save(tiles)
          
        if keys[pygame.K_l]:
          tiles = load()
          
        if keys[pygame.K_n]:
          newSprite()
    
    #print(pressed)
    if clicked[0]:
      if pressed:
        tiles.append([clicked[1], mousePos])
        clicked = [False, 0]
      else:
        win.blit(userAssets[clicked[1]], mousePos)
    
    
    for tile in tiles:
      #print(tile)
      try:
        win.blit(userAssets[tile[0]], tile[1])
      except Exception as e:
        print("Error: "+ e)
    
    drawTaskbar()
    tickSprites()  
            
    
    if debug:
      framerate = round(clock.get_fps(), 1)
      win.blit(font.render("FPS: {}".format(framerate),True, white), (10, 10))
    pygame.display.update()
   clock.tick(60)