
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

player_2_ver = random.randrange(12,20)
player_2_hor = random.randrange(12,20)
player_3_ver = random.randrange(12,20)
player_3_hor = random.randrange(12,20)
player_4_ver = random.randrange(12,20)
player_4_hor = random.randrange(12,20)
player_5_ver = random.randrange(12,20)
player_5_hor = random.randrange(12,20)
player_6_ver = random.randrange(12,20)
player_6_hor = random.randrange(12,20)
player_7_ver = random.randrange(12,20)
player_7_hor = random.randrange(12,20)


cord_list=[0]*7


map = np.chararray((100,100), unicode = True)

map[:] = 'O'

map[0,:] = 'H'

map[:,0] = 'H'

vision = map[ver_vis_num_l:ver_vis_num_h, hor_vis_num_l:hor_vis_num_h]


print('The zeroes are the unknown.')

print(vision)

player = 'A'



exp = 0
attack_level = 1
player_level = 0
attack_list = ['heal','hit','hit hard']

info = [attack_level,exp,attack_list]*7



print('The A is you..')

m_ver_vis_num = int((ver_vis_num_h + ver_vis_num_l) / 2)
m_hor_vis_num = int((hor_vis_num_h + hor_vis_num_l) / 2)


map[m_ver_vis_num][m_hor_vis_num] = player


print(vision)


def check_neighbors(cords,player_health,attack_list,player_attack,exp):

	ver_cord = cords[0]
	hor_cord = cords[1]
	if map[ver_cord + 1][hor_cord] == 'B' or map[ver_cord][hor_cord + 1] == 'B' or map[ver_cord + 1][hor_cord + 1] == 'B' or map[ver_cord - 1][hor_cord] == 'B' or map[ver_cord][hor_cord - 1] == 'B' or map[ver_cord - 1][hor_cord - 1] == 'B' or map[ver_cord - 1][hor_cord + 1] == 'B' or map[ver_cord + 1][hor_cord - 1] == 'B':
		print("encounter")
		exp = battle(player_health,attack_list,player_attack,exp)



	return exp


def check_neighbors_npc(cords,count,info):

	ver_cord = cords[0]
	hor_cord = cords[1]
	if map[ver_cord + 1][hor_cord] == 'B' or map[ver_cord][hor_cord + 1] == 'B' or map[ver_cord + 1][hor_cord + 1] == 'B' or map[ver_cord - 1][hor_cord] == 'B' or map[ver_cord][hor_cord - 1] == 'B' or map[ver_cord - 1][hor_cord - 1] == 'B' or map[ver_cord - 1][hor_cord + 1] == 'B' or map[ver_cord + 1][hor_cord - 1] == 'B':
		print("encounter")
		player_cord_list = cord_list(count,cords)
		enemy_count = check_positions(cords, player_cord_list)
		enemy_info = info[enemy_count]
		your_info = info[count]
		y_exp, e_exp = npc_battle(info,enemy_info)
		y_player_level = math.floor(y_exp / 2)
		y_attack_level = (y_player_level * .5) + 1
		store_info(y_attack_level,y_exp,info[count][2],count)
		e_player_level = math.floor(e_exp / 2)
		e_attack_level = (e_player_level * .5) + 1
		store_info(e_attack_level,e_exp,info[count][2],enemy_count)
		
	return

def npc_battle(your_info,enemy_info):

	y_attack_list = your_info[2]
	e_attack_list = enemy_info[2]
	y_exp = your_info[1]
	e_exp = enemy_info[1]
	y_attack_level = your_info[0]
	e_attack_level = enemy_info[0]			

	npc_health = 10	
	enemy_health = 10
	
	while npc_health > 0 and enemy_health > 0:
	
		attack_choice = random.randrange(1,4)


		if(attack_choice == 1):
				npc_health += 1
		
		if(attack_choice == 2):
				enemy_health -= y_attack_level
	

		if(attack_choice == 3):
				npc_health -= 2 * y_attack_level
		
	
		if npc_health < 1:
			break
		

		if enemy_health < 1:
			break

		attack_choice = random.randrange(1,4)


		if(attack_choice == 1):
				enemy_health += 1
		
		if(attack_choice == 2):
				npc_health -= e_attack_level
	

		if(attack_choice == 3):
				npc_health -= e_attack_level
		
		
		if npc_health < 1:
			break
		

		if enemy_health < 1:
			break
	

	if player_health < 1:
		e_exp += 1
		print("Challenger Loses")
			
		

	if enemy_health < 1:
		y_exp += 1
		print("Challenger Wins")
		


	return y_exp, e_exp





def battle(player_health,attack_list,player_attack,exp):

	enemy_health = 10
	
	print("""\

         />_________________________________
[########[]_________________________________>
         \>


                    """)


	while player_health > 0 and enemy_health > 0:
		print("Choose an attack from the list")
		attack_input = input(attack_list)
	
		if(attack_input == 'hit'):
			enemy_health -= player_attack
	
		if(attack_input == 'heal'):
			player_health += 1

		if(attack_input == 'hit hard'):
			enemy_health -= player_attack * 2

		print('your enemies health: ')
		print(enemy_health)
		print('your health: ')
		print(player_health)			
	
		if player_health < 1:
			break
		

		if enemy_health < 1:
			break

		attack_choice = random.randrange(1,4)


		if(attack_choice == 1):
				enemy_health += 1
		
		if(attack_choice == 2):
				player_health -= 1
	

		if(attack_choice == 3):
				player_health -= 2
		
		print("enemy used:")
		print(attack_list[attack_choice - 1])
		print('your enemies health: ')
		print(enemy_health)
		print('your health: ')
		print(player_health)	


	if player_health < 1:
		print("You Lose")
			
		

	if enemy_health < 1:
		exp += 1
		print("You Win")
		


	return exp

	

def player_cord_list(count,cords):
	
	cord_list[count] = cords
	return cord_list



def check_positions(your_cords, player_cord_list):
	
	count = 0;

	for x in player_cord_list:

		if your_cords != x and (x[0] - your_cords[0]) <= 1 and (x[0] - your_cords[0]) >=  -1 and (x[1] - your_cords[1]) <= 1 and (x[1] - your_cords[1]) >=  -1:
			return count

		count+=1	 	
	
	

def store_info(attack_level,exp,attack_list,count):
	info[count]= [attack_level,exp,attack_list]
	return info
	



def move_player_2(player_2_ver, player_2_hor,count,info):

	player_2 = 'B'


	choice = random.randrange(1,5)
	
	player_2_ver_l = player_2_ver - 7
	player_2_hor_l = player_2_hor - 7
		
	m_ver_vis_num_2 = int((player_2_ver + player_2_ver_l) / 2)
	m_hor_vis_num_2 = int((player_2_hor + player_2_hor_l) / 2)
	
	

	if choice == 1:
		
		if m_ver_vis_num_2 > 0:
			map[m_ver_vis_num_2][m_hor_vis_num_2] = 'O'
			player_2_ver -= 1
			player_2_ver_l -= 1


	if choice == 2:

		if m_ver_vis_num_2 < 99:
			map[m_ver_vis_num_2][m_hor_vis_num_2] = 'O'
			player_2_ver += 1
			player_2_ver_l += 1

	if choice == 3:

		if m_hor_vis_num_2 > 0:
			map[m_ver_vis_num_2][m_hor_vis_num_2] = 'O'
			player_2_hor -= 1
			player_2_hor_l -= 1

	if choice == 4:

		if m_hor_vis_num_2 < 99:
			map[m_ver_vis_num_2][m_hor_vis_num_2] = 'O'
			player_2_hor += 1
			player_2_hor_l += 1

	

	m_ver_vis_num_2 = int((player_2_ver + player_2_ver_l) / 2)
	m_hor_vis_num_2 = int((player_2_hor + player_2_hor_l) / 2)


	map[m_ver_vis_num_2][m_hor_vis_num_2] = 'B'
	
	check_neighbors_npc()

	store_info(attack_level,exp,count,player_level)
	
	return player_2_ver, player_2_hor


'''
count = 0
player_2_ver, player_2_hor = move_player_2(player_2_ver, player_2_hor,count,info)
count += 1
player_3_ver, player_3_hor = move_player_2(player_3_ver, player_3_hor,count)
count += 1
player_4_ver, player_4_hor = move_player_2(player_4_ver, player_4_hor,count)
count += 1
player_5_ver, player_5_hor = move_player_2(player_5_ver, player_5_hor,count)
count += 1
player_6_ver, player_6_hor = move_player_2(player_6_ver, player_6_hor,count)
count += 1
player_7_ver, player_7_hor = move_player_2(player_7_ver, player_7_hor,count)
count += 1
'''


while 1:

	

	player_input = input("Enter up, down, right, left to move or enter look to recenter screen: ")

	player_health = 10
	attack_list = ['heal','hit','hit hard']
	
		


	if player_input == "up":
		if m_ver_vis_num > 0:
			map[m_ver_vis_num][m_hor_vis_num] = 'O'
			ver_vis_num_h -= 1
			ver_vis_num_l -= 1

	if player_input == "down":
		if m_ver_vis_num < 99:
			map[m_ver_vis_num][m_hor_vis_num] = 'O'
			ver_vis_num_h += 1
			ver_vis_num_l += 1

	if player_input == "left":
		if m_hor_vis_num > 0:
			map[m_ver_vis_num][m_hor_vis_num] = 'O'
			hor_vis_num_h -= 1
			hor_vis_num_l -= 1

	if player_input == "right":
		if m_hor_vis_num < 99:
			map[m_ver_vis_num][m_hor_vis_num] = 'O'
			hor_vis_num_h += 1
			hor_vis_num_l += 1

	if player_input == "look":
		vision = map[ver_vis_num_l:ver_vis_num_h, hor_vis_num_l:hor_vis_num_h]

	if player_input == "map":
		print(map[40:70, 40:70])


	m_ver_vis_num = int((ver_vis_num_h + ver_vis_num_l) / 2)
	m_hor_vis_num = int((hor_vis_num_h + hor_vis_num_l) / 2)
	player_cords = [m_ver_vis_num,m_hor_vis_num]

	player_2_ver, player_2_hor = move_player_2(player_2_ver, player_2_hor,0,info)
	player_3_ver, player_3_hor = move_player_2(player_3_ver, player_3_hor,1,info)
	player_4_ver, player_4_hor = move_player_2(player_4_ver, player_4_hor,2,info)
	player_5_ver, player_5_hor = move_player_2(player_5_ver, player_5_hor,3,info)
	player_6_ver, player_6_hor = move_player_2(player_6_ver, player_6_hor,4,info)
	player_7_ver, player_7_hor = move_player_2(player_7_ver, player_7_hor,5,info)

	prev_lvl = player_level

	exp = check_neighbors(player_cords,player_health,attack_list,player_attack,exp)

	player_level = math.floor(exp / 2)
	
	print(player_level)
	print(player_attack)

	player_attack = (player_level * .5) + 1
	attack_level = (player_level * .5) + 1

	if(player_level > prev_lvl):
		print("Congratulations you leveled up to",math.floor(player_level))
	

	map[m_ver_vis_num][m_hor_vis_num] = player
	
	store_info(attack_level,exp,6,player_level)	
	
	print(player_cords)

	print(vision)












