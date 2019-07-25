import numpy as np
import random

b=15


map = np.chararray((b,b), unicode = True)

map[:] = '0'

map[0,:] = 'X'

map[:,0] = 'X'

map[b-1,:] = 'X'

map[:,b-1] = 'X'

def road(map,b):
	r1 = random.randrange(1,4)
	r2 = random.randrange(1,4)
	a = 0
	while a < b:
		r1 = random.randrange(1,4)
		r2 = random.randrange(1,4)
		if r1 > 1:
			map[int(b/2)+1,a] = 'X'
		if r2 > 1:
			map[int(b/2)-1,a] = 'X'
		
		a+=1

	return map




