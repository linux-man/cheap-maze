from cheap_maze import *

width = 10
height = 10
t, l = make_maze(width, height)

print(t)
print(l)

for y in range(height):
	for x in range(width):
		if check_grid(t, x, y): print("+-", end="")
		else: print("+ ", end="")
	print("+")
	for x in range(width):
		if check_grid(l, x, y): print("| ", end="")
		else: print("  ", end="")
	print("|")
for x in range(width): print("+-", end="")
print("+")
