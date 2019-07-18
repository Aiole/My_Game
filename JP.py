
#whatever monster kills you takes your gear and exp just like a player would xp gain for kills is a % of opponents xp not 100% if you return and kill them you will get everything back but xp will be lost in transfer

#Nothing will ever despawn if you die you respawn with nothing lvl 1 so do the mobs when they die they will spawn as well they can move and will fight and gain xp/items just like you. 

#there will be scrap mobs just like the spawning blobs in agar.io that will be easily farmable and wont move/update the game

import numpy as np
import random
import math


print('Hello traveler')

ver_vis_num_h = 7
hor_vis_num_h = 7
ver_vis_num_l = 0
hor_vis_num_l = 0




map = np.chararray((100,100), unicode = True)

map[:] = 'O'

map[0,:] = 'H'

map[:,0] = 'H'


exp = 0
attack_level = 1
player_level = 0
attack_list = ['heal','hit','hit hard']
cords = [10,10]
start_spawn = [10,10]


vision = map[cords[0]-3:cords[0]+4, cords[1]-3:cords[1]+4]


print('The zeroes are the unknown.')

print(vision)

player = 'A'




def check_positions(your_cords, info):
	
	count = 0;

	for s in info:
			
		x = s[3]			
		
		if your_cords != x and (x[0] - your_cords[0]) <= 1 and (x[0] - your_cords[0]) >=  -1 and (x[1] - your_cords[1]) <= 1 and (x[1] - your_cords[1]) >=  -1:
			return count

		count+=1	 	
	
	return False


def initialize(a, info):

	ver = random.randrange(1,98)
	hor = random.randrange(1,98)
	cords = [ver,hor]
	if not check_positions(cords,info):
		map[cords[0]][cords[1]] = 'B'
		start_spawn = cords
		info[a] = [attack_level,exp,attack_list,cords,start_spawn]
		return info
	else:
		return initialize(a,info)




a = input('Enter the number of players: ')
a = int(a)


info = [[attack_level,exp,attack_list,cords,start_spawn]]*a

a -= 1
dup_a = a

while a > 0:

	info = initialize(a,info)
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
		enemy_info = info[enemy_count]
		your_info = info[count]

		p_exp, e_exp = battle(your_info,enemy_info)

		if(p_exp == 0):
			map[cords[0]][cords[1]] = 'O'
			info.pop(count)
			e_player_level = math.floor(e_exp / 2)
			e_attack_level = (e_player_level * .5) + 1
			info[enemy_count][0] = e_attack_level
			info[enemy_count][1] = e_exp
			info.pop(count)

			#info[count][3] = info[count][4]

		if(e_exp == 0):
			enemy_cords = info[enemy_count][3]
			map[enemy_cords[0]][enemy_cords[1]] = 'O'
			p_player_level = math.floor(p_exp / 2)
			p_attack_level = (p_player_level * .5) + 1
			info[count][0] = p_attack_level
			info[count][1] = p_exp
			info.pop(enemy_count)
			#info[enemy_count][3] = info[enemy_count][4]



	return info


def check_neighbors_npc(cords,count,info):

	ver_cord = cords[0]
	hor_cord = cords[1]

	if check_positions(cords,info):

		print("npc_encounter")
		enemy_count = check_positions(cords, info)
		enemy_info = info[enemy_count]
		your_info = info[count]

		y_exp, e_exp = npc_battle(your_info,enemy_info)
		
		print(math.floor(y_exp / 2))
		print(math.floor(e_exp / 2))

		if y_exp == 0:
			map[cords[0]][cords[1]] = 'O'
			e_player_level = math.floor(e_exp / 2)
			e_attack_level = (e_player_level * .5) + 1
			info[enemy_count][0] = e_attack_level
			info[enemy_count][1] = e_exp
			info.pop(count)
			#info[count][3] = info[count][4]


		if e_exp == 0:
			enemy_cords = info[enemy_count][3]
			map[enemy_cords[0]][enemy_cords[1]] = 'O'
			y_player_level = math.floor(y_exp / 2)
			y_attack_level = (y_player_level * .5) + 1
			info[count][0] = y_attack_level
			info[count][1] = y_exp
			info.pop(enemy_count)
			#info[enemy_count][3] = info[enemy_count][4]

		
		print('PLayers remaining: ' + str(len(info)))
		
	return info

def npc_battle(your_info,enemy_info):

	y_attack_list = your_info[2]
	e_attack_list = enemy_info[2]
	y_exp = your_info[1]
	e_exp = enemy_info[1]
	y_attack_level = your_info[0]
	e_attack_level = enemy_info[0]			

	npc_health = 10	
	enemy_health = 10

	
	while 1:
	
		attack_choice = random.randrange(1,4)


		if attack_choice == 1:
				npc_health += 1
		
		if attack_choice == 2:
				enemy_health -= y_attack_level
	

		if attack_choice == 3:
				enemy_health -= 2 * y_attack_level
		
	
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
				enemy_health += 1
		
		if attack_choice == 2:
				npc_health -= e_attack_level
	

		if attack_choice == 3:
				npc_health -= 2 * e_attack_level
		
		
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
	
		
		


	return y_exp, e_exp





def battle(your_info,enemy_info):

	enemy_health = 10
	
	print("""\

         />_________________________________
[########[]_________________________________>
         \>


                    """)
		

	p_attack_list = your_info[2]
	e_attack_list = enemy_info[2]
	p_exp = your_info[1]
	e_exp = enemy_info[1]
	p_attack_level = your_info[0]
	e_attack_level = enemy_info[0]			

	player_health = 10	
	enemy_health = 10
	
	while player_health > 0 and enemy_health > 0:

		print("Choose an attack from the list")
		attack_input = input(attack_list)
	
		if attack_input == 'hit':
			enemy_health -= p_attack_level
	
		if attack_input == 'heal':
			player_health += 1

		if attack_input == 'hit hard':
			enemy_health -= p_attack_level * 2

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
				enemy_health += 1
		
		if attack_choice == 2:
				player_health -= e_attack_level
	

		if attack_choice == 3:
				player_health -= e_attack_level*2
	

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
		e_exp += (p_exp / 2) + 1
		p_exp = 0
		print("Player Loses")
			
		

	if enemy_health <= 0:
		p_exp += (e_exp / 2) + 1
		e_exp = 0
		print("Player Wins")
		
		


	return p_exp, e_exp






def move_other_player(count,info):

	player_2 = 'B'


	choice = random.randrange(1,5)
	
	cords = info[count][3]

	

	if choice == 1:
		
		if cords[0] > 1:
			map[cords[0]][cords[1]] = 'O'
			cords[0] -= 1


	if choice == 2:

		if cords[0] < 98:
			map[cords[0]][cords[1]] = 'O'
			cords[0] += 1

	if choice == 3:

		if cords[1] > 1:
			map[cords[0]][cords[1]] = 'O'
			cords[1] -= 1

	if choice == 4:

		if cords[1] < 98:
			map[cords[0]][cords[1]] = 'O'
			cords[1] += 1

	
	
	map[cords[0]][cords[1]] = 'B'

	info[count][3] = cords
	
	info = check_neighbors_npc(cords,count,info)

		
	
	return info



while 1:


	player_input = input("Enter up, down, right, left to move or enter look to recenter screen: ")

	player_health = 10
	attack_list = ['heal','hit','hit hard']
	
	cords = info[0][3]

	if player_input == "up":
		if cords[0] > 1:
			map[cords[0]][cords[1]] = 'O'
			cords[0] -= 1

	if player_input == "down":
		if cords[0] < 98:
			map[cords[0]][cords[1]] = 'O'
			cords[0] += 1

	if player_input == "left":
		if cords[1] > 1:
			map[cords[0]][cords[1]] = 'O'
			cords[1] -= 1

	if player_input == "right":
		if cords[1] < 98:
			map[cords[0]][cords[1]] = 'O'
			cords[1] += 1

	if player_input == "look":
		vision = map[cords[0]-3:cords[0]+4, cords[1]-3:cords[1]+4]

	if player_input == "map":
		print(map[40:70, 40:70])

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












