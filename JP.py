
import numpy as np

print('Hello traveler')

ver_vis_num = 7
hor_vis_num = 7

vision = np.chararray((ver_vis_num,hor_vis_num), unicode = True)

vision[:] = 'O'

print('The zeroes are the unknown.')

print(vision)

player = 'A'

print('The A is you..')

m_ver_vis_num = int(ver_vis_num / 2)
m_hor_vis_num = int(hor_vis_num / 2)


vision[m_ver_vis_num][m_hor_vis_num] = player

print(vision)
