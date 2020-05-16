
#whatever monster kills you takes your gear and exp just like a player would xp gain for kills is a % of opponents xp not 100% if you return and kill them you will get everything back but xp will be lost in transfer

#Nothing will ever despawn if you die you respawn with nothing lvl 1 so do the mobs when they die they will spawn as well they can move and will fight and gain xp/items just like you. 

#there will be scrap mobs just like the spawning blobs in agar.io that will be easily farmable and wont move/update the game

#Ai adventures who are on the same mission as you and will also be rogue like and you can interact with them

#Weapons/Armor are cards and skills are static. A turn is a combination of a weapon and a skill. There will be many different skills but you can only bring a limited number of skills (3?) into each battle which you can equip in inventory.

#What does fusion add besides more cards to your hand? What does it do that other card games cant? defusion and fusion skills can only be used once per turn cycle (your turn + enemies) they are infinite like hero powers. Defusion is when you use one of your skills after an opponent plays something (the possible things that can be played on your turn are: nothing which can not be defused, one card, 2 cards playing 2 cards is known as a combination/combo, 1 card 1 skill known as a fusion) you can not play a skill by itself.

import time
import numpy as np
import random
import math
import csv
import msvcrt
from Map import road
from random import shuffle
from graphics import *

win = GraphWin('Face', 800, 600) # give title and dimensions
enemies = []

class CreateEnemy:
	
	def __init__(self,cords,health,size,color):
		self.c = cords
		self.h = health
		self.s = size
		self.clr = color

	def draw_enemy(self):
		self.n = Circle(Point(self.c[0],self.c[1]), self.s)
		self.n.setFill(self.clr)
		self.n.draw(win)
	
	def enemy_hit(self,x,y):
		if(self.c[0] + self.s >= x >= self.c[0] - self.s and self.c[1] + self.s >= y >= self.c[1] - self.s):
			print(self.n)
			self.n.undraw()

i = 0		
while i < 10:		
	cords = [0,0]	
	cords[0] = random.randrange(1,799)
	cords[1] = random.randrange(1,599)
	size = random.randrange(10,50)
	enemies.append(CreateEnemy(cords,20,size,"red",))
	enemies[i].draw_enemy()
	i+=1


dx, dy = 10, 0
key = 0


head = Circle(Point(400,500), 25) # set center and radius
head.setFill("yellow")
head.draw(win)
dx, dy = 10, 0
mcx, mcy = 400,500
p = None
line = None
count_1 = 0

while(1):
	
	k = win.checkKey()


	if k == 'a':
		head.move(-dx, dy)
		mcx -= dx
	elif k == 'd':
		head.move(dx, dy)
		mcx += dx
	elif k == 'w':
		head.move(dy,-dx)
		mcy -= dx
	elif k == 's':
		head.move(dy,dx)
		mcy += dx
	p = win.checkMouse()

	if(p != None):
		if (line):
			line.undraw()
		x = p.x
		y = p.y
		line = Line(Point(mcx,mcy), Point(x,y))
		line.draw(win)
		for enemy in enemies:			
			enemy.enemy_hit(x,y)
		count_1 = 0

	count_1+=1
	






