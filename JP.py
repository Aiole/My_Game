import numpy as np
import random


print('Hello traveler')

ver_vis_num_h = 7
hor_vis_num_h = 7
ver_vis_num_l = 0
hor_vis_num_l = 0

player_2_ver = random.randrange(7,100)
player_2_hor = random.randrange(7,100)
player_3_ver = random.randrange(7,100)
player_3_hor = random.randrange(7,100)
player_4_ver = random.randrange(7,100)
player_4_hor = random.randrange(7,100)
player_5_ver = random.randrange(7,100)
player_5_hor = random.randrange(7,100)
player_6_ver = random.randrange(7,100)
player_6_hor = random.randrange(7,100)
player_7_ver = random.randrange(7,100)
player_7_hor = random.randrange(7,100)


map = np.chararray((100,100), unicode = True)

map[:] = 'O'

vision = map[ver_vis_num_l:ver_vis_num_h, hor_vis_num_l:hor_vis_num_h]


print('The zeroes are the unknown.')

print(vision)

player = 'A'

print('The A is you..')

m_ver_vis_num = int((ver_vis_num_h + ver_vis_num_l) / 2)
m_hor_vis_num = int((hor_vis_num_h + hor_vis_num_l) / 2)


map[m_ver_vis_num][m_hor_vis_num] = player


print(vision)



def move_player_2(player_2_ver, player_2_hor):

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
	return player_2_ver, player_2_hor



player_2_ver, player_2_hor = move_player_2(player_2_ver, player_2_hor)
player_3_ver, player_3_hor = move_player_2(player_3_ver, player_3_hor)
player_4_ver, player_4_hor = move_player_2(player_4_ver, player_4_hor)
player_5_ver, player_5_hor = move_player_2(player_5_ver, player_5_hor)
player_6_ver, player_6_hor = move_player_2(player_6_ver, player_6_hor)
player_7_ver, player_7_hor = move_player_2(player_7_ver, player_7_hor)


while 1:

	player_input = input("Enter up, down, right, left to move or enter look to recenter screen: ")


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


	map[m_ver_vis_num][m_hor_vis_num] = player
	

	player_2_ver, player_2_hor = move_player_2(player_2_ver, player_2_hor)
	player_3_ver, player_3_hor = move_player_2(player_3_ver, player_3_hor)
	player_4_ver, player_4_hor = move_player_2(player_4_ver, player_4_hor)
	player_5_ver, player_5_hor = move_player_2(player_5_ver, player_5_hor)
	player_6_ver, player_6_hor = move_player_2(player_6_ver, player_6_hor)
	player_7_ver, player_7_hor = move_player_2(player_7_ver, player_7_hor)

	print(m_ver_vis_num)
	print(m_hor_vis_num)

	print(vision)






