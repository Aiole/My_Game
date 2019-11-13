
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
from random import shuffle

print('Hello traveler')

ver_vis_num_h = 7
hor_vis_num_h = 7
ver_vis_num_l = 0
hor_vis_num_l = 0

b = input('Enter the Map Size: ')
b = int(b)


map = np.chararray((b,b), unicode = True)

map[:] = 'O'

map[0,:] = 'X'

map[:,0] = 'X'

map[b-1,:] = 'X'

map[:,b-1] = 'X'

map = road(map,b)

exp = 0
attack_level = 1
player_level = 0
attack_list = ['hone','enlighten','entrench']
cords = [5,5]
start_spawn = [5,5]
axe = ['axe',random.randrange(1,25)]
sword = ['sword',random.randrange(1,20)]
chainbody = ['chainbody',random.randrange(1,25)]
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




lines = open('adjectives.txt').read().splitlines() #txt or csv depending on version

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
		

	y_deck = shuffle_deck(info,0)
	e_deck = shuffle_deck(info,enemy_count)
	y_hand = []
	e_hand = []
	y_skills = info[0][2]
	e_skills = info[enemy_count][2]
	y_exp = info[0][1]
	e_exp = info[enemy_count][1]
	y_attack_level = check_dmg(info,0)
	e_attack_level = check_dmg(info,enemy_count)			
	y_def = check_def(info,0)
	e_def = check_def(info,enemy_count)
	player_health = 20	
	enemy_health = 20
	y_speed = 0
	e_speed = 0

	a = 0

	battle_info = []
	ori_hand = []
	y_discard = []

	while len(y_deck) > 0 and a < 5:
		y_hand.append(y_deck.pop(0))
		a+=1
	

	while player_health > 0 and enemy_health > 0:
		
	
		battle_info, y_hand, y_discard = first_selection(ori_hand,y_hand,y_skills,y_discard)
		y_deck += y_discard
		y_speed += battle_info[5]
		e_speed += 100	
		print("this is my speed ", y_speed, "this is the enemy speed ", e_speed)


		while(1):
			y_speed -= 1
			e_speed -= 1
			
			if(y_speed <= 0):
				turnflag = 1
				break

			if(e_speed <= 0):
				turnflag = 0
				break


		if(turnflag):
			enemy_health -= battle_info[0] 
			player_health += battle_info[2]
			y_hand.append(y_deck.pop(0))
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
					player_health -= 1 / battle_info[1]
		
			if attack_choice == 2:
					player_health -= 1 / battle_info[1]
	

			if attack_choice == 3:
					player_health -= 1 / battle_info[1] 
	
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

		else:
			attack_choice = random.randrange(1,4)
			if attack_choice == 1:
					player_health -= 1 / battle_info[1]
		
			if attack_choice == 2:
					player_health -= 1 / battle_info[1]
	

			if attack_choice == 3:
					player_health -= 1 / battle_info[1] 
	
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



			enemy_health -= battle_info[0] 
			player_health += battle_info[2]
			y_hand.append(y_deck.pop(0))
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


def first_selection(ori_hand,hand,skills,y_discard):

	ori_hand = hand[:]
	print ('This is your hand: ',hand)

	player_input = input('Please enter the name of the item you would like to select: ')


	a = 0

	for item in hand:

		if (str(player_input) in item):			
			
			print('you have selected ', item)
			item_choice = item 
			y_discard.append(hand.pop(a))
			
			return sec_selection(ori_hand,hand,skills,item_choice,y_discard)			

		a+=1

					

	return first_selection(ori_hand,hand,skills,y_discard)


def sec_selection(ori_hand,hand,skills,item_choice,y_discard):

	print ('This is your hand: ', hand)
	print('These are your skills: ', skills)
	player_input = input('Please enter a secondary selection you will have a chance to confirm your choice if you would like to use the item by itself type done: ')



	if (str(player_input) == 'done'):

		return confirm_attack(ori_hand,hand,skills,item_choice,'None',y_discard)
	

	a = 0
	for item in hand:

		if (str(player_input) in item):			
			
			print('you have selected ', item)
			print(type(item))
			return confirm_attack(ori_hand,hand,skills,item_choice,item,a,y_discard)			

		a+=1

	a = 0
	for skill in skills:

		if (str(player_input) in skill):			
		
			print('you have selected ', skill)
			print(type(skill))
			return confirm_attack(ori_hand,hand,skills,item_choice,skill,None,y_discard)			

		a+=1

	
			
		

	return sec_selection(ori_hand,hand,skills,item_choice,y_discard)



def confirm_attack(ori_hand,hand,skills,item_choice,sec_choice,a,y_discard):

	battle_info = []

	#item only
	if(sec_choice == 'None'):
		power = item_choice[1] / 10
		if(card_type(item_choice) == 'weapon'):
			print('The selected ability will attack for: ', power)
			
		
		if(card_type(item_choice) == 'armor'):
			print('The selected ability will increase defence by: ', power)
		
		while(1):
			player_input = input('type either confirm, restart to rechoose an initial item or back to rechoose a secondary item or skill: ')
			
			if(str(player_input) == 'confirm'):
				return [item_choice, sec_choice]

			if(str(player_input) == 'back'):
				return sec_selection(ori_hand,hand,skills,item_choice,y_discard)
			
			if(str(player_input) == 'restart'):
				return first_selection(ori_hand,ori_hand,skills,[])
				
		
	while(1):


		battle_info = check_ability(item_choice,sec_choice)

		player_input = input('type either confirm, restart to rechoose an initial item or back to rechoose a secondary item or skill: ')				

		if(str(player_input) == 'confirm'):

			if(a != None):

				y_discard.append(hand.pop(a))

			return battle_info, hand, y_discard

		if(str(player_input) == 'back'):
			return sec_selection(ori_hand,hand,skills,item_choice,y_discard)
		
		if(str(player_input) == 'restart'):
			return first_selection(ori_hand,ori_hand,skills,[])
	


	return sec_selection(ori_hand,hand,skills,item_choice,y_discard)



def check_ability(item,sec_choice):

	attack = 0
	defence = 1
	healing = 0
	buff = [] # [attack buff, defence buff, etc...]
	debuff = []
	power1 = item[1] / 10
	skill_info = []
	speed = 100
	battle_info = [attack,defence,healing,buff,debuff,speed]

	if 'sword' in item:
		battle_info[0] = power1
		speed = 100

	if 'axe' in item:
		battle_info[0] = power1
		speed = 125
	
	if 'chainbody' in item:
		battle_info[1] = power1
		speed = 100
	
	if 'platemale' in item:
		battle_info[1] += power1
		speed = 125

	if card_type(item) == 'weapon':
		battle_info[0] += power1

	if card_type(item) == 'armor':
		battle_info[1] += power1

	if card_type(sec_choice) == 'armor':
		power2 = sec_choice[1] / 10
		battle_info[0] += power2

		if 'chainbody' in sec_choice:
			speed = (speed + 100) / 2
	
		if 'platemale' in sec_choice:
			speed = (speed + 125) / 2
		

	if card_type(sec_choice) == 'weapon':
		power2 = sec_choice[1] / 10
		battle_info[1] += power2

		if 'sword' in sec_choice:
			speed = (speed + 100) / 2
	
		if 'axe' in sec_choice:
			speed = (speed + 125) / 2
		

	if card_type(sec_choice) == 'NA':
		skill_info = skills(sec_choice)

		if (skill_info[0] == "buff"):
			battle_info[skill_info[1]] *= skill_info[2] 

		if (skill_info[0] == "healing"):
			battle_info[2] += skill_info[2]


	print(speed)
	battle_info[5] = speed
		

	return battle_info



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


def card_type(item):

	if 'sword' in str(item) or 'axe' in str(item):
			return 'weapon'

	if 'chainbody' in str(item) or 'platemale' in str(item):
			return 'armor'


	return 'NA'


def skills(skill):
	
	skill_info = []

	if 'hone' in str(skill):
		return ['buff', 0, 1.5] #[type, number in type array, power]
		
	if 'enlighten' in str(skill):
		return ['healing', 0, .5]
	
	if 'entrench' in str(skill):
		return ['buff', 1, 1.5]
	


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



def shuffle_deck(info,count):
	
	deck = info[count][5][0] + info[count][5][1]	
	deck = random.sample(deck, len(deck))
	return deck
	
	



while 1:


	player_input = input("Enter up, down, right, left to move or enter look to recenter screen: ")

	player_health = 20
	attack_list = ['hone','enlighten','entrench']
	
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












