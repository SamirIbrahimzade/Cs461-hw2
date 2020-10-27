import random


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
          if(i + j == 0 and Array[i][j] != 1):
            counter = counter + 1
          if(i + j == 1 and Array[i][j] != 2):
            counter = counter + 1
          if(i + j == 2 and Array[i][j] != 3):
            counter = counter + 1
          if(i + j == 3 and Array[i][j] != 4):
            counter = counter + 1
          if((i + j == 4 or i + j == 5) and Array[i][j] != 5):
            counter = counter + 1
          if(i + j == 6 and Array[i][j] != 0):
            counter = counter + 1
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

def moveUp(s):
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          temp = s[i-1][j]
          s[i-1][j] = 0
          s[i][j] = temp
          return

def moveDown(s):
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          print (i,j)
          temp = s[i+1][j]
          s[i+1][j] = 0
          s[i][j] = temp
          return

def moveLeft(s):
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          temp = s[1][j-1]
          s[1][j-1] = 0
          s[i][j] = temp
          return

def moveRight(s):
  length = len(s)

  for i in range(length):
      for j in range(length):
        if(s[i][j]==0):
          temp = s[i][j+1]
          s[i][j+1] = 0
          s[i][j] = temp
          return
          
      

def Astar(puzzle):

  #form a queue with root node
  queue = []




T = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, 0]]

printer(T)
print()
mixer(T)
printer(T)
print(countMisplacedTiles(T))

