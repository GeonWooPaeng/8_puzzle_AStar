from queue import PriorityQueue
from copy import deepcopy

class E_puzzle:
    def __init__(self,start,parent):
        self.board = start 
        self.parent = parent 
        self.f = 0
        self.g = 0
        self.h = 0

# h(n) ->Check the miss tile
def distance(child,goal): 
    dist = 0
    for i in range(3):
        for j in range(3):
            if child.board[i][j] != goal[i][j]:
                dist += 1
    return dist
            
#Move and find children 
def Move(current): 
    current = current.board
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
    
    for item in openlist:
        if item.f < f:
            f = item.f
            PQ.put((f,item))
            
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
        if current.board == goal:
            return current
                     
        openList.remove(current)
        closedList.append(current)

        children = Move(current)
        for child in children:
            for child_c in closedList:
                if child != child_c:
                    #f(n) = h(n) + g(n) 
                    g = current.g + 1 
                    child.g = g 
                    child.h = distance(child,goal)
                    child.f = child.g + child.h 
                    child.parent = current 
                    openList.append(child)
                else:
                    break 
    return 0


      
# Write start value and goal value here
start = [[1,2,0],[3,4,5],[6,7,8]]
goal = [[0,1,2],[3,4,5],[6,7,8]] 
a = E_puzzle(start, None)
result = Astar(a,goal)

Path = []
if(not result):
    print ("No solution")
else:
    Path.append([y for x in result.board for y in x]) 
    t=result.parent
    while t:
        Path.append([y for x in t.board for y in x])
        t=t.parent
for i in range(len(Path)-1,-1,-1):
    print(' '.join(map(str,Path[i])))



        
