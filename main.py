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
T = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, 0]]

printer(T)
print()
mixer(T)

printer(T)
