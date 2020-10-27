import random
from queue import PriorityQueue


# bug --> visited 


def mixer(puzzleGrid):
  emptyX = 3
  emptyY = 3
  count = 0
  while count < 10:
    rand = random.randint(0, 3)
    if rand == 0 and emptyX - 1 >= 0 :
      puzzleGrid[emptyX][emptyY] = puzzleGrid[emptyX - 1][emptyY]
      puzzleGrid[emptyX - 1][emptyY] = 0
      emptyX -= 1
      count += 1
    elif rand == 1 and emptyY + 1 < 4 :
      puzzleGrid[emptyX][emptyY] = puzzleGrid[emptyX][emptyY + 1]
      puzzleGrid[emptyX][emptyY + 1] = 0
      emptyY += 1
      count += 1
    elif rand == 2 and emptyX + 1 < 4 :
      puzzleGrid[emptyX][emptyY] = puzzleGrid[emptyX + 1][emptyY]
      puzzleGrid[emptyX + 1][emptyY] = 0 
      emptyX += 1
      count += 1

    elif rand == 3 and emptyY - 1 >= 0 :
      puzzleGrid[emptyX][emptyY] = puzzleGrid[emptyX][emptyY - 1]
      puzzleGrid[emptyX][emptyY - 1] = 0
      emptyY -= 1
      count += 1
    #debug
    #print()  
    #print("decision is " + str(rand))
    #print("count is " + str(count))
    #print()  
    #printer(puzzleGrid)

def printer(Array):
  for r in Array:
      for c in r:
          print(c,end = " ")
      print()

def countMisplacedTiles(Array):
  counter = 0
  length = len(Array)

  for i in range(length):
      for j in range(length):
          if(Array[i][j] != finalGrid[i][j]):
            counter += 1

  return counter

def findEmptyGrid(s):
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          return i,j
      

def checkUp(s):
  x,y = findEmptyGrid(s)
  if(x == 0):
    return False
  return True

def checkDown(s):
  x,y = findEmptyGrid(s)
  if(x == 3):
    return False
  return True

def checkLeft(s):
  x,y = findEmptyGrid(s)
  if(y == 0):
    return False
  return True

def checkRight(s):
  x,y = findEmptyGrid(s)
  if(y == 3):
    return False
  return True

def moveUp(puzzle):
  s = puzzle
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          temp = s[i-1][j]
          s[i-1][j] = 0
          s[i][j] = temp
          return s

def moveDown(puzzle):
  s = puzzle
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          #print (i,j)
          temp = s[i+1][j]
          s[i+1][j] = 0
          s[i][j] = temp
          return s

def moveLeft(puzzle):
  s = puzzle
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          temp = s[1][j-1]
          s[1][j-1] = 0
          s[i][j] = temp
          return s

def moveRight(puzzle):
  s = puzzle
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          temp = s[i][j+1]
          s[i][j+1] = 0
          s[i][j] = temp
          return s

def checkVisited(vis, arr):
  for state in vis:
    if(arr == state):
      return True
  return False
      

def Astar(puzzle):

  #form a queue with root node
  queue = PriorityQueue()
  visited = []
  
  misplacedTiles = countMisplacedTiles(puzzle)

  node = {
    "Puzzle" : puzzle,
    "Cost" : misplacedTiles
  }
  #queue.append(node)
  currentPath = []

  queue.put((misplacedTiles,puzzle,currentPath))

  print("worked fine")

  #check if goal is reached
  while(queue.empty() == False):

    print(queue.queue,"queue end")
    #remove the first path
    fPath = queue.get()
    
    nPuzzle = fPath[1]
    nCost = fPath[0]

    if(nCost == 0):
      return

    #print(queue)
    #print(fPath)
    
    #add new paths 
    if(checkUp(nPuzzle)):
      puz = moveUp(nPuzzle)
      if(checkVisited(visited,puz) != True):
        ncost = countMisplacedTiles(puz)
        visited.append(puz)
        currentPath.append(0)
        queue.put((nCost,puz,currentPath))
      
    if(checkDown(nPuzzle)):
      puz = moveDown(nPuzzle)
      if(checkVisited(visited,puz)):
        ncost = countMisplacedTiles(puz)
        visited.append(puz)
        currentPath.append(1)
        queue.put((nCost,puz,currentPath))
      
    if(checkLeft(nPuzzle)):
      puz = moveLeft(nPuzzle)
      if(checkVisited(visited,puz) != True):
        ncost = countMisplacedTiles(puz)
        visited.append(puz)
        currentPath.append(2)
        queue.put((nCost,puz,currentPath))
      
    if(checkRight(nPuzzle)):
      puz = moveRight(nPuzzle)
      if(checkVisited(visited,puz) != True):
        ncost = countMisplacedTiles(puz)
        visited.append(puz)
        currentPath.append(3)
        queue.put((nCost,puz,currentPath))
    


finalGrid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, 0]]

T = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, 0]]

printer(T)
print()
mixer(T)
printer(T)
print(countMisplacedTiles(T))
print(findEmptyGrid(T))

Astar(T)
