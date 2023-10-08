from random import randrange, random
from math import sin, cos, asin, pi

def set_bit(value, bit):
	return value | (1<<bit)

def clear_bit(value, bit):
	if check_bit(value, bit):
		return value & ~(1 << bit)
	return value

def check_bit(value, bit):
	return value & 1 << bit != 0

def set_grid(g, x, y):
	g[y] = set_bit(g[y], x)

def clear_grid(g, x, y):
	g[y] = clear_bit(g[y], x)

def check_grid(g, x, y):
	return check_bit(g[y], x)

def make_maze(w = 4, h = 4):
	count = 0
	visited = [0]*h
	top_wall = [2**w - 1] * h
	left_wall = [2**w - 1] * h
	x = randrange(w - 1)
	y = randrange(h - 1)

	def check_cell(n_x, n_y):
		if not(n_x < 0 or n_y < 0 or n_x > w - 1 or n_y > h - 1 or check_grid(visited, n_x, n_y)):
			d = [(n_x - 1, n_y), (n_x, n_y + 1), (n_x + 1, n_y), (n_x, n_y - 1)]
			for (xx, yy) in d:
				if not(xx < 0 or yy < 0 or xx > w - 1 or yy > h - 1) and check_grid(visited, xx, yy):
					new_cells.append([n_x, n_y])
					break
		
	while count < w * h:
		set_grid(visited, x, y)
		count += 1
		d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		d = sorted(d, key = lambda k: random()) #shuffle(d)
		dead_end = True
		for (xx, yy) in d:
			if not(xx < 0 or yy < 0 or xx > w - 1 or yy > h - 1 or check_grid(visited, xx, yy)):
				if xx == x: clear_grid(top_wall, x, max(y, yy))
				else: clear_grid(left_wall, max(x, xx), y)
				x = xx
				y = yy
				dead_end = False
				break
		if dead_end:
			new_cells = []
			for dist in range(1, max(w, h)):
				for da in range(-dist, dist + 1, dist * 2):
					for db in range(-dist, dist + 1):
						n_x = x + da
						n_y = y + db
						check_cell(n_x, n_y)
						n_x = x + db
						n_y = y + da
						check_cell(n_x, n_y)
						if len(new_cells) > 0: break
					if len(new_cells) > 0: break
				if len(new_cells) > 0: break
			new_cells = sorted(new_cells, key = lambda k: random()) #shuffle(d)
			new_cells = sorted(new_cells, key = lambda k: (k[0] - x)**2 + (k[1] - y)**2)
			new_cell = False
			for (n_x, n_y) in new_cells:
				d = [(n_x - 1, n_y),(n_x, n_y + 1),(n_x + 1, n_y),(n_x, n_y - 1)]
				d = sorted(d, key = lambda k: random()) #shuffle(d)
				for (xx, yy) in d:
					if not(xx < 0 or yy < 0 or xx > w - 1 or yy > h - 1) and check_grid(visited, xx, yy):
						if xx == n_x: clear_grid(top_wall, n_x, max(n_y, yy))
						else: clear_grid(left_wall, max(n_x, xx), n_y)
						x = n_x
						y = n_y
						new_cell = True
						break
				if new_cell: break
			
	return top_wall, left_wall
