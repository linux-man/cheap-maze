# cheap-maze
## Maze Generator for low resources systems
It all started when I decided to make a maze game for the NumWorks calculator (MicroPython).

Starting with the depth-first search algorithm of maze generation implemented using backtracking, I found that the system couldn't handle the level of recursion for mazes above 8x8 cells - "pystack exhausted".

Tried the Iterative implementation with stack. Better, but at around 30x30, the generator began to crash - "Memory allocation failed".

Then I tried to build a maze with smaller mazes. It's feaseble, but the result is ugly - you can see the "blocks".

After all this experiments, my solution is a "mutated" depth-first search algorithm without memory.
### Routine:
1. Given a current cell as a parameter
2. Mark the current cell as visited
3. If the current cell has any unvisited neighbour cells

    3.1. Choose one of the unvisited neighbours
   
    3.2. Remove the wall between the current cell and the chosen cell
   
    3.3. Choose the chosen cell as the current cell
   
    3.4. Goto 2

5. If the current cell don't have unvisited neighbour cells

    4.1. Search for the closest unvisited cell with any visited neighbours

    4.2. Remove the wall between the closest unvisited cell and one of its visited neighbours

    4.3. Choose the unvisited cell as the current cell

    4.4. Goto 2

And with that, one can generate a maze of over 100x100 cells (I tried up to 160x111, half of NumWorks resolution).

Although I didn't find closed paths and other issues, I can't guarantee the correctness of the generated mazes.
### Other memory optimizations:
Cells only have Top and Left walls. Every wall is "bit stored". Every maze row is stored in 2 integers - Top walls and Left walls - so a maze is made of 2 (one dimensional) arrays: top_wall and left_wall. There are no walls to close the right and bottom of the maze.

### Objective:
[NumWorks Maze Script](https://my.numworks.com/python/joao-caldas-lopes/maze)
### How to Create a Maze
```python
from cheap_maze import *

width=10
height=10
t, l = make_maze(width, height)
```
#### There are helper function to read and change the data:
`check_grid(array, x, y)`

`set_grid(array, x, y)`

`clear_grid(array, x, y)`
