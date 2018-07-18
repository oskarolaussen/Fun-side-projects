import random
import numpy as np
from PIL import Image
import time
'''This program creates an image of a square maze using recursive backtracking.
The image has a black border. The path is white and the walls are black.'''

def maze(lab,i,j,neighbours):
	current_cell=(i,j)
	stack=[]
	visited=set()
	visited.add(current_cell)
	number_of_visited_cells=1
	while number_of_visited_cells<(size-2)**2:
		a, b = current_cell
		unvisited_neighbours=neighbours(a,b)- visited
		if unvisited_neighbours:
			chosen_cell=random.choice(tuple(unvisited_neighbours))
			stack.append(current_cell)
			#following if-statements remove the wall (means setting it white) between the current cell and chosen cell.
			if chosen_cell[0]==current_cell[0]:
				if chosen_cell[1]<current_cell[1]:
					lab[2*chosen_cell[0]-1][2*chosen_cell[1]]=255
				else:
					lab[2*chosen_cell[0]-1][2*chosen_cell[1]-2]=255
			else:
				if chosen_cell[0]<current_cell[0]:
					lab[2*chosen_cell[0]][2*chosen_cell[1]-1]=255
				else:
					lab[2*chosen_cell[0]-2][2*chosen_cell[1]-1]=255
			current_cell=chosen_cell
			visited.add(current_cell)
			number_of_visited_cells=number_of_visited_cells+1
		elif stack:
			current_cell=stack.pop()
	return lab;

'''neighbours returns the neighbouring cells of the input excluding the border'''
def neighbours(i,j):
	neighbouring=set()
	k=i
	for s in range(j-1,j+2,2):
		if (k!=0 and k!=size-1) and (s!=0 and s!=size-1):
			neighbouring.add((k,s))
	l=j
	for n in range(i-1,i+2,2):
		if (l!=0 and l!=size-1) and (n!=0 and n!=size-1):
			neighbouring.add((n,l))
	return neighbouring;


size=int(input("How many cells across you wish the maze to be? "))

start_x, start_y=1, 1
#set the whole maze black 
labyrinth=np.zeros([2*(size-2)+1,2*(size-2)+1])
#set upper left corner (entrance) and lower right corner (finish) as white
labyrinth[0][1], labyrinth[2*size-4][2*size-5]= 255, 255
#set cells as white
for i in range(1,2*(size-2),2):
	for j in range(1, 2*(size-2), 2):
		labyrinth[i][j]=255
start_time=time.time()
labyrinth=maze(labyrinth,start_x,start_y, neighbours)
print(time.time()-start_time)
img=Image.fromarray(labyrinth)
img= img.convert("RGB")
img.save("labyrinth.png")