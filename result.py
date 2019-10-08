from queue import PriorityQueue
from copy import deepcopy
import argparse

class E_puzzle:
    def __init__(self,start,parent):
        self.state = start 
        self.parent = parent 
        self.f = 0
        self.g = 0
        self.h = 0

# h(n) ->Check the miss tile
def distance(child,goal): 
    dist = 0
    for i in range(3):
        for j in range(3):
            if child.state[i][j] != goal[i][j]:
                dist += 1
    return dist
            

#Move and find children 
def Move(current): 
    current = current.state
    for i in range(3):
        for j in range(3):
            if current[i][j] == 0:
                x,y = i,j
                break    

    children = []
    if y != 2: #right
        child = deepcopy(current)
        child[x][y] = child[x][y+1]
        child[x][y+1] = 0
        num_child = E_puzzle(child, current)
        children.append(num_child)
    
    if y != 0: #left
        child = deepcopy(current)
        child[x][y] = child[x][y-1]
        child[x][y-1] = 0
        num_child = E_puzzle(child, current)
        children.append(num_child)
    
    if x != 2: #down
        child = deepcopy(current)
        child[x][y] = child[x+1][y]
        child[x+1][y] = 0
        num_child = E_puzzle(child, current)
        children.append(num_child)
    
    if x != 0: #up
        child = deepcopy(current)
        child[x][y] = child[x-1][y]
        child[x-1][y] = 0
        num_child = E_puzzle(child, current)
        children.append(num_child)
    
    return children

#priorityqueue
def priorityqueue(openlist):
    PQ = PriorityQueue()
    f = openlist[0].f
    PQ.put((f,openlist[0]))
    
    for node in openlist:
        if node.f < f:
            f = node.f
            PQ.put((f,node))
            
    return PQ.get()[1]

'''
Sequence
1. Put on  node priority queue
2. priority queue pop() = current  
3. remove current node in openList
4. Put on currnet node in closedList 
5. To make children
6. Calculate child f(n) = h(n) + g(n)
7. Put on child node in openList 
'''

def Astar(start,goal):
    openList = [] # Set of discoverable nodes
    closedList = [] # Set of nodes already retrieved
    openList.append(start)

    while openList: 
        current = priorityqueue(openList)
        if current.state == goal:
            return current
                     
        openList.remove(current)
        closedList.append(current)

        children = Move(current)
        for child in children:
            for child_c in closedList:
                if child != child_c:
                    #f(n) = h(n) + g(n) 
                    g = current.g + 1 
                    present = False
                    for i , child_o in enumerate(openList):
                        if child == child_o:
                            present = True
                            if g < openList[i].g:
                                openList[i].f = g + openList[i].h 
                                openList[i].parent = current
                    if not present:
                        child.f = g + distance(child,goal) 
                        child.parent = current 
                        openList.append(child)
                else:
                    break 
    return 0

# 타고타고 올라가면서 체크 해야한다.


# Write start value and goal value here
# start = [[1,2,0],[3,4,5],[6,7,8]]
# goal = [[0,1,2],[3,4,5],[6,7,8]]

parser = argparse.ArgumentParser()
parser.add_argument('--input',type=argparse.FileType('r'),required=True)
args = parser.parse_args()
print(args.input.readlines())

# a = E_puzzle(start, None)
# solution = Astar(a,goal)

# Path = []
# if not solution:
#     print ("No solution")
# else:
#     Path.append([y for x in solution.state for y in x]) 
#     state = solution.parent
#     while state:
#         Path.append([y for x in state.state for y in x])
#         state = state.parent
# for i in range(len(Path)-1,-1,-1):
#     print(' '.join(map(str,Path[i])))

