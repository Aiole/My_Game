
#whatever monster kills you takes your gear and exp just like a player would xp gain for kills is a % of opponents xp not 100% if you return and kill them you will get everything back but xp will be lost in transfer

#Nothing will ever despawn if you die you respawn with nothing lvl 1 so do the mobs when they die they will spawn as well they can move and will fight and gain xp/items just like you. 

#there will be scrap mobs just like the spawning blobs in agar.io that will be easily farmable and wont move/update the game

#Ai adventures who are on the same mission as you and will also be rogue like and you can interact with them

#Weapons/Armor are cards and skills are static. A turn is a combination of a weapon and a skill. There will be many different skills but you can only bring a limited number of skills (3?) into each battle which you can equip in inventory.

#What does fusion add besides more cards to your hand? What does it do that other card games cant? defusion and fusion skills can only be used once per turn cycle (your turn + enemies) they are infinite like hero powers. Defusion is when you use one of your skills after an opponent plays something (the possible things that can be played on your turn are: nothing which can not be defused, one card, 2 cards playing 2 cards is known as a combination/combo, 1 card 1 skill known as a fusion) you can not play a skill by itself.

import numpy as np
import random
import math
import csv
from Map import road


print('Hello traveler')

ver_vis_num_h = 7
hor_vis_num_h = 7
ver_vis_num_l = 0
hor_vis_num_l = 0

b = input('Enter the Map Size: ')
b = int(b)


map = np.chararray((b,b), unicode = True)

map[:] = '0'

map[0,:] = 'X'

map[:,0] = 'X'

map[b-1,:] = 'X'

map[:,b-1] = 'X'

map = road(map,b)

exp = 0
attack_level = 1
player_level = 0
attack_list = ['heal','hit','hit hard']
cords = [5,5]
start_spawn = [5,5]
axe = ['axe',random.randrange(1,20)]
sword = ['sword',random.randrange(1,20)]
chainbody = ['chainbody',random.randrange(1,20)]
platemale = ['platemale',random.randrange(1,20)]
weapons = [axe,sword]
armor = [chainbody,platemale]
items = [weapons,armor]
max_cord = b


vision = map[cords[0]-3:cords[0]+4, cords[1]-3:cords[1]+4]


print('The zeroes are the unknown.')

print(vision)

player = 'A'



def swap_pos(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list


def check_positions(your_cords, info):
	
	count = 0;

	for s in info:
			
		x = s[3]			
		
		if your_cords != x and (x[0] - your_cords[0]) <= 1 and (x[0] - your_cords[0]) >=  -1 and (x[1] - your_cords[1]) <= 1 and (x[1] - your_cords[1]) >=  -1:
			return count

		count+=1	 	
	
	return False




lines = open('adjectives.csv').read().splitlines()

def rand_adj(lines):
	r = random.randrange(1,28475)
	return lines[r]


def initialize(a, b, info, lines):
	ver = random.randrange(1,b-2)
	hor = random.randrange(1,b-2)
	cords = [ver,hor]
	axe = [rand_adj(lines) + ' axe', random.randrange(1,20)]
	sword = [rand_adj(lines) + ' sword', random.randrange(1,20)]
	chainbody = [rand_adj(lines) + ' chainbody', random.randrange(1,20)]
	platemale = [rand_adj(lines) + ' platemale', random.randrange(1,20)]
	weapons = [axe,sword]
	armor = [chainbody,platemale]
	items = [weapons,armor]
	max_cord = b

	if not check_positions(cords,info):
		map[cords[0]][cords[1]] = 'B'
		start_spawn = cords
		info[a] = [attack_level,exp,attack_list,cords,start_spawn,items,max_cord]
		return info
	else:
		return initialize(a,b,info,lines)




a = input('Enter the number of players: ')
a = int(a)


info = [[attack_level,exp,attack_list,cords,start_spawn,items,max_cord]]*a

a -= 1
dup_a = a

while a > 0:

	info = initialize(a,b,info,lines)
	a -= 1



print('The A is you..')

cords = info[0][3]

vision = map[cords[0]-3:cords[0]+4, cords[1]-3:cords[1]+4]


map[cords[0]][cords[1]] = player


print(vision)


def check_neighbors(info,count):

	
	cords = info[count][3]
	ver_cord = cords[0]
	hor_cord = cords[1]

	if check_positions(cords,info):

		print("encounter")
		enemy_count = check_positions(cords, info)

		info = battle(info,enemy_count)


	return info


def check_neighbors_npc(cords,count,info):

	ver_cord = cords[0]
	hor_cord = cords[1]

	if check_positions(cords,info):

		print("npc_encounter")
		enemy_count = check_positions(cords, info)
		info = npc_battle(info,count,enemy_count)
		
		print('Players remaining: ' + str(len(info)))
		
	return info

	


def npc_battle(info,count,enemy_count):

	y_attack_list = info[count][2]
	e_attack_list = info[enemy_count][2]
	y_exp = info[count][1]
	e_exp = info[enemy_count][1]
	y_attack_level = check_dmg(info,count)
	y_def = check_def(info,count)
	e_attack_level = check_dmg(info,enemy_count)
	e_def = check_def(info,enemy_count)
		

	npc_health = 20	
	enemy_health = 20

	
	while 1:
	
		attack_choice = random.randrange(1,4)


		if attack_choice == 1:
				enemy_health -= y_attack_level / e_def
		
		if attack_choice == 2:
				enemy_health -= y_attack_level / e_def
	

		if attack_choice == 3:
				enemy_health -= 2 * y_attack_level / e_def
		
	
		if npc_health <= 0:
			e_exp += (y_exp / 2) + 1
			y_exp = 0
			print("Challenger Loses")
			break
		

		if enemy_health <= 0:
			y_exp += (e_exp / 2) + 1
			e_exp = 0
			print("Challenger Wins")
			break

		attack_choice = random.randrange(1,4)


		if attack_choice == 1:
				npc_health -= e_attack_level / y_def
		
		if attack_choice == 2:
				npc_health -= e_attack_level / y_def
	

		if attack_choice == 3:
				npc_health -= 2 * e_attack_level / y_def
		
		
		if npc_health <= 0:
			e_exp += (y_exp / 2) + 1
			y_exp = 0
			print("Challenger Loses")
			break
		

		if enemy_health <= 0:
			y_exp += (e_exp / 2) + 1
			e_exp = 0
			print("Challenger Wins")
			break
	
		
		

	if(y_exp == 0):
		map[cords[0]][cords[1]] = 'O'
		e_player_level = math.floor(e_exp / 2)
		e_attack_level = (e_player_level * .5) + 1
		info[enemy_count][0] = e_attack_level
		info[enemy_count][1] = e_exp
		info[enemy_count][5][0].extend(info[count][5][0])
		info[enemy_count][5][1].extend(info[count][5][1])
		info.pop(count)


	if(e_exp == 0):
		enemy_cords = info[enemy_count][3]
		map[enemy_cords[0]][enemy_cords[1]] = 'O'
		y_player_level = math.floor(y_exp / 2)
		y_attack_level = (y_player_level * .5) + 1
		info[count][0] = y_attack_level
		info[count][1] = y_exp
		info[count][5][0].extend(info[enemy_count][5][0])
		info[count][5][1].extend(info[enemy_count][5][1])
		info.pop(enemy_count)
		


	return info






def battle(info,enemy_count):

	
	print("""\

         />_________________________________
[########[]_________________________________>
         \>


                    """)
		

	
	y_attack_list = info[0][2]
	e_attack_list = info[enemy_count][2]
	y_exp = info[0][1]
	e_exp = info[enemy_count][1]
	y_attack_level = check_dmg(info,0)
	e_attack_level = check_dmg(info,enemy_count)			
	y_def = check_def(info,0)
	e_def = check_def(info,enemy_count)

	player_health = 20	
	enemy_health = 20
	
	while player_health > 0 and enemy_health > 0:

		print("Choose an attack from the list")
		attack_input = input(attack_list)
	
		if attack_input == 'hit':
			enemy_health -= y_attack_level / e_def
	
		if attack_input == 'heal':
			player_health += 1

		if attack_input == 'hit hard':
			enemy_health -= (y_attack_level * 2) / e_def

		print('your enemies health: ')
		print(enemy_health)
		print('your health: ')
		print(player_health)			
	
		if player_health <= 0:
			break
		

		if enemy_health <= 0:
			break


		attack_choice = random.randrange(1,4)


		if attack_choice == 1:
				player_health -= e_attack_level / y_def
		
		if attack_choice == 2:
				player_health -= e_attack_level / y_def
	

		if attack_choice == 3:
				player_health -= (e_attack_level*2) / y_def 
	

		print("enemy used:")
		print(attack_list[attack_choice - 1])
		print('your enemies health: ')
		print(enemy_health)
		print('your health: ')
		print(player_health)
		
		
		if player_health <= 0:
			break
		

		if enemy_health <= 0:
			break
	

	if player_health <= 0:
		e_exp += (y_exp / 2) + 1
		y_exp = 0
		print("Player Loses")
			
		

	if enemy_health <= 0:
		y_exp += (e_exp / 2) + 1
		e_exp = 0
		print("Player Wins")
		
		

	if(y_exp == 0):
		map[cords[0]][cords[1]] = 'O'
		e_player_level = math.floor(e_exp / 2)
		e_attack_level = (e_player_level * .5) + 1
		info[enemy_count][0] = e_attack_level
		info[enemy_count][1] = e_exp
		info[enemy_count][5][0].extend(info[0][5][0])
		info[enemy_count][5][1].extend(info[0][5][1])
		info.pop(0)


	if(e_exp == 0):
		enemy_cords = info[enemy_count][3]
		map[enemy_cords[0]][enemy_cords[1]] = 'O'
		y_player_level = math.floor(y_exp / 2)
		y_attack_level = (y_player_level * .5) + 1
		info[0][0] = y_attack_level
		info[0][1] = y_exp
		info[0][5][0].extend(info[enemy_count][5][0])
		info[0][5][1].extend(info[enemy_count][5][1])
		info.pop(enemy_count)
		



	return info



def check_dmg(info,count):
	
	exp = info[count][1]		
	level = math.floor(exp / 2)
	weapon = info[count][5][0][0][1]	
	
	dmg = (level * .35) + (weapon * .1)
	return dmg


def check_def(info,count):
	
	armor = info[count][5][1][0][1]	
	defe = (armor / 20) + 1
	return defe


def equip(items,num):

	player_input = input('Enter which weapon you would like to equip ' + str(items[num]) + ': ')


	if player_input == 'back':
		return items,0


	if player_input == 'quit':
		return items,1

	a = 0
	for weapon in items[num]:

		if (str(player_input) in weapon):			
			items[num][a] = items[num][0]
			items[num][0] = weapon
			if(a == 0):
				print(str(player_input) + ' already equipped')
				return equip(items,num)						
	
			else:		
				print(str(player_input) + ' equipped')
				return equip(items,num)

		a+=1
			

					

	return equip(items,num)


def discard(items,num):

	
	try:				
		player_input = input("Enter the weapon's number you would like to discard starting from one " + str(items[num]) + ': ')
		
		if player_input == 'quit':
			return items,1
	
		if player_input == 'back':
			return items,0

		player_input = int(player_input)				
					
	except ValueError:
		player_input = input('Please enter a number: ' + str(items[num]) + ': ')
		player_input = int(player_input)

	if len(items[num]) == 1:
		print('You can not discard any more items please enter back or quit')
		return discard(items,num)

	if player_input - 1 < len(items[num]):
		print(str(items[num][player_input - 1]) + ' discarded')
		items[num].pop(player_input - 1)
		return discard(items,num)

def dis_or_equ(items,num):

	quit = 0

	player_input = input('Do you want to discard or equip? ')

	if player_input == "equip":
				
		items, quit = equip(items,num)
				
	if player_input == "discard":		

		items, quit = discard(items,num)
		
	if player_input == "back":
		return items, quit

	if player_input == "quit":
		return items, 1
		

	if quit:
		return items, quit					

	if not quit:
		return dis_or_equ(items,num)


		

def open_inv(info):

	items = info[0][5]
	quit = 0
	
	while 1:

		player_input = input('Welcome to your inventory please enter one of the following weapons or armor: ')

		if player_input == "weapons":
			
			num = 0

			items, quit = dis_or_equ(items,num)
			
			if quit:
				break
				
		


		if player_input == "armor":

			num = 1

			items, quit = dis_or_equ(items,num)
			
			if quit:
				break


		if player_input == "quit":
			break
			

		if player_input == "back":
			break

	
	return info


def move_other_player(count,info):

	player_2 = 'B'


	choice = random.randrange(1,5)
	
	cords = info[count][3]

	max_cord = info[count][6]

	if choice == 1:
		
		if cords[0] > 1:
			if map[cords[0]-1][cords[1]] != 'X':
				map[cords[0]][cords[1]] = 'O'
				cords[0] -= 1


	if choice == 2:

		if cords[0] < (max_cord - 2):
			if map[cords[0]+1][cords[1]] != 'X':
				map[cords[0]][cords[1]] = 'O'
				cords[0] += 1

	if choice == 3:

		if cords[1] > 1:
			if map[cords[0]][cords[1]-1] != 'X':
				map[cords[0]][cords[1]] = 'O'
				cords[1] -= 1

	if choice == 4:

		if cords[1] < (max_cord - 2):
			if map[cords[0]][cords[1]+1] != 'X':
				map[cords[0]][cords[1]] = 'O'
				cords[1] += 1

	
	
	map[cords[0]][cords[1]] = 'B'

	info[count][3] = cords
	
	info = check_neighbors_npc(cords,count,info)

		
	
	return info



while 1:


	player_input = input("Enter up, down, right, left to move or enter look to recenter screen: ")

	player_health = 20
	attack_list = ['heal','hit','hit hard']
	
	cords = info[0][3]
	max_cord = info[0][6]
	
	if player_input == "up":
		if cords[0] > 1:
			if map[cords[0]-1][cords[1]] != 'X':
				map[cords[0]][cords[1]] = 'O'
				cords[0] -= 1

	if player_input == "down":
		if cords[0] < (max_cord - 2):
			if map[cords[0]+1][cords[1]] != 'X':
				map[cords[0]][cords[1]] = 'O'
				cords[0] += 1

	if player_input == "left":
		if cords[1] > 1:
			if map[cords[0]][cords[1]-1] != 'X':
				map[cords[0]][cords[1]] = 'O'
				cords[1] -= 1

	if player_input == "right":
		if cords[1] < (max_cord - 2):
			if map[cords[0]][cords[1]+1] != 'X':
				map[cords[0]][cords[1]] = 'O'
				cords[1] += 1

	if player_input == "look":
		vision = map[cords[0]-3:cords[0]+4, cords[1]-3:cords[1]+4]

	if player_input == "map":
		print(map[40:70, 40:70])


	if player_input == "inv":
		info = open_inv(info)

	info[0][3] = cords	
	
	a = 1
	for x in info:
		info = move_other_player(a,info)
		a+=1
		if a >= len(info):
			break

	map[cords[0]][cords[1]] = 'A'

	prev_lvl = player_level

	info = check_neighbors(info,0)

	map[cords[0]][cords[1]] = 'O'
	
	cords = info[0][3]
	print(cords)

	map[cords[0]][cords[1]] = 'A'
	
	exp = info[0][1]
	
	player_level = math.floor(exp / 2)
	
	print('Your current level is ' + str(player_level))

	attack_level = (player_level * .5) + 1

	info[0][0] = attack_level

	if player_level > prev_lvl:
		print("Congratulations you leveled up to",math.floor(player_level))
	

	
	
	

	print(vision)












