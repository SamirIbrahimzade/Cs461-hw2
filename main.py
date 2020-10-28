import random
from queue import PriorityQueue
import copy
import matplotlib.pyplot as plt


# second part ==> Ayberk
# collect visited state and cost
# get rid of same state with more cost
# counter 
# current path

# final part
# create 12 puzzles
# solve all 12 puzzles
# polishing(var names)
# add comments

def mixer(puzzleGrid):
    emptyX = 3
    emptyY = 3
    count = 0
    while count < 10:
        rand = random.randint(0, 3)
        if rand == 0 and emptyX - 1 >= 0:
            puzzleGrid[emptyX][emptyY] = puzzleGrid[emptyX - 1][emptyY]
            puzzleGrid[emptyX - 1][emptyY] = 0
            emptyX -= 1
            count += 1
        elif rand == 1 and emptyY + 1 < 4:
            puzzleGrid[emptyX][emptyY] = puzzleGrid[emptyX][emptyY + 1]
            puzzleGrid[emptyX][emptyY + 1] = 0
            emptyY += 1
            count += 1
        elif rand == 2 and emptyX + 1 < 4:
            puzzleGrid[emptyX][emptyY] = puzzleGrid[emptyX + 1][emptyY]
            puzzleGrid[emptyX + 1][emptyY] = 0
            emptyX += 1
            count += 1

        elif rand == 3 and emptyY - 1 >= 0:
            puzzleGrid[emptyX][emptyY] = puzzleGrid[emptyX][emptyY - 1]
            puzzleGrid[emptyX][emptyY - 1] = 0
            emptyY -= 1
            count += 1
        # debug
        # print()
        # print("decision is " + str(rand))
        # print("count is " + str(count))
        # print()
        # printer(puzzleGrid)


def printer(Array):
    for r in Array:
        for c in r:
            print(c, end=" ")
        print()


def countMisplacedTiles(Array):
    counter = 0
    length = len(Array)

    for i in range(length):
        for j in range(length):
            if (Array[i][j] != finalGrid[i][j]):
                counter += 1

    return counter


def findEmptyGrid(s):
    length = len(s)

    for i in range(length):
        for j in range(length):
            if (s[i][j] == 0):
                return i, j


def checkUp(s):
    x, y = findEmptyGrid(s)
    if (x == 0):
        return False
    return True


def checkDown(s):
    x, y = findEmptyGrid(s)
    if (x == 3):
        return False
    return True


def checkLeft(s):
    x, y = findEmptyGrid(s)
    if (y == 0):
        return False
    return True


def checkRight(s):
    x, y = findEmptyGrid(s)
    if (y == 3):
        return False
    return True


def moveUp(puzzle):
    s = copy.deepcopy(puzzle)
    length = len(s)

    for i in range(length):
        for j in range(length):
            if (s[i][j] == 0):
                temp = copy.deepcopy(s[i - 1][j])
                s[i - 1][j] = 0
                s[i][j] = copy.deepcopy(temp)
                return s


def moveDown(puzzle):
    s = copy.deepcopy(puzzle)
    length = len(s)

    for i in range(length):
        for j in range(length):
            if (s[i][j] == 0):
                temp = copy.deepcopy(s[i + 1][j])
                s[i + 1][j] = 0
                s[i][j] = copy.deepcopy(temp)
                return s


def moveLeft(puzzle):
    s = copy.deepcopy(puzzle)
    length = len(s)

    for i in range(length):
        for j in range(length):
            if (s[i][j] == 0):
                temp = copy.deepcopy(s[i][j - 1])
                s[i][j - 1] = 0
                s[i][j] = copy.deepcopy(temp)
                return s


def moveRight(puzzle):
    s = copy.deepcopy(puzzle)
    length = len(s)

    for i in range(length):
        for j in range(length):
            if (s[i][j] == 0):
                temp = copy.deepcopy(s[i][j + 1])
                s[i][j + 1] = 0
                s[i][j] = copy.deepcopy(temp)
                return s


def checkVisited(vis, arr):
    #print("in checkVisited")
    for state in vis:
        #print("state is ", state)
        #print("state[0] is ", state[0])
        if (arr == state[0]):  # state(puzzle, cost, path)   state[0] = puzzle
            global everVisited
            everVisited += 1
            return True
    return False


# def Astar(puzzle):
#   # form a queue with root node
#   queue = PriorityQueue()
#   visited = []
#
#   misplacedTiles = countMisplacedTiles(puzzle)
#
#   node = {
#     "Puzzle": puzzle,
#     "Cost": misplacedTiles
#   }
#   # queue.append(node)
#   currentPath = []
#
#   queue.put((misplacedTiles, puzzle))
#
#   print("worked fine")
#
#   # check if goal is reached
#   while (queue.empty() == False):
#
#     print(queue.queue, "queue end")
#     print()
#     # remove the first path
#     fPath = queue.get()
#
#     nPuzzle = fPath[1]
#     newCost = fPath[0]
#
#     if (newCost == 0):
#       printer(nPuzzle)
#       return
#
#     # print(queue)
#     # print(fPath)
#
#     # add new paths
#     if (checkUp(nPuzzle)):
#       puz = moveUp(nPuzzle)
#       # printer(puz)
#       if (checkVisited(visited, puz) != True):
#         ncost = countMisplacedTiles(puz)
#         visited.append(puz)
#         # currentPath.append(0)
#
#         queue.put((ncost, puz))
#         # print("flag1")
#         # print(queue.queue)
#
#     if (checkDown(nPuzzle)):
#       # printer(nPuzzle)
#       puz = moveDown(nPuzzle)
#
#       # print("flag22")
#       # printer(puz)
#       # print()
#       if (checkVisited(visited, puz) != True):
#         ncost = countMisplacedTiles(puz)
#         visited.append(puz)
#         # currentPath.append(1)
#         # print("flag2")
#         queue.put((ncost, puz))
#
#     if (checkLeft(nPuzzle)):
#       puz = moveLeft(nPuzzle)
#       if (checkVisited(visited, puz) != True):
#         ncost = countMisplacedTiles(puz)
#         visited.append(puz)
#         # currentPath.append(2)
#         queue.put((ncost, puz))
#
#     if (checkRight(nPuzzle)):
#       puz = moveRight(nPuzzle)
#       if (checkVisited(visited, puz) != True):
#         ncost = countMisplacedTiles(puz)
#         visited.append(puz)
#         # currentPath.append(3)
#         queue.put((ncost, puz))


def Astar(puzzle):
    # form a queue with root node
    pqueue = PriorityQueue()  # queue(heuristicValue, tuple)    tuple(puzzleState, cost, path)
    visited = []  # (puzzle state, cost, path)
    costSoFar = 0  # move counter
    currentPath = []  # 0=up 1=down 2=left 3=right

    heuristicValue = countMisplacedTiles(puzzle)  # getting heuristic value (number of misplaced tiles)

    pqueue.put( (heuristicValue, [puzzle, costSoFar, currentPath]) )  #
    visited.append((puzzle, costSoFar, currentPath))

    #print("worked fine")

    maxQueueSize = 0

    # check if goal is reached
    while (pqueue.empty() == False):

        #print("queue begin", pqueue.queue, "queue end")
        if(pqueue.qsize() > maxQueueSize):
            maxQueueSize = pqueue.qsize()
        #print(pqueue.qsize())
        #print()
        # remove the first path
        fPath = pqueue.get()

        currentHeuristic = fPath[0]
        currentTuple = fPath[1]

        currentPuzzle = currentTuple[0]
        currentCostSoFar = currentTuple[1]
        print("currentcostsofar ", currentCostSoFar)
        currentPath = currentTuple[2]
        global printerCount
        if(printerCount > 0):
            if(printerCount == 2):
                print("first puzzle is being solved")
            if(printerCount == 1):
                print("second puzzle is being solved")
            printer(currentPuzzle)
        #print()

        # print("visited")
        # for v in visited:
        #     print(v)


        if (currentHeuristic == 0):
            #print(currentPath)
            if(printerCount > 0):
                print("puzzle is solved, final state is ")
                printer(currentPuzzle)
                printerCount -= 1

            tempValue = pqueue.get()
            maxList.append(pqueue.qsize())



            # solveFollow(currentPath)

            return

        #########################################################################
        # find new possible paths
        heuristic0 = maxInt
        heuristic1 = maxInt
        heuristic2 = maxInt
        heuristic3 = maxInt

        if (checkUp(currentPuzzle)):  # if we can move empty-tile up
            #print("can go up")
            puz0 = moveUp(currentPuzzle)  # puz0 = state when empty-tile is moved up
            heuristic0 = countMisplacedTiles(puz0)  # heuristic value of that state is number of misplaced tiles

        if (checkDown(currentPuzzle)):  # if we can move empty-tile down
            #print("can go down")
            puz1 = moveDown(currentPuzzle)  # puz1 = state when empty-tile is moved down
            heuristic1 = countMisplacedTiles(puz1)  # heuristic value of that state is number of misplaced tiles

        if (checkLeft(currentPuzzle)):  # if we can move empty-tile left
            #print("can go left")
            puz2 = moveLeft(currentPuzzle)  # puz2 = state when empty-tile is moved left
            heuristic2 = countMisplacedTiles(puz2)  # heuristic value of that state is number of misplaced tiles

        if (checkRight(currentPuzzle)):  # if we can move empty-tile right
            #print("can go right")
            puz3 = moveRight(currentPuzzle)  # puz3 = state when empty-tile is moved right
            heuristic3 = countMisplacedTiles(puz3)  # heuristic value of that state is number of misplaced tiles

        heuristics = [(heuristic0 * 10), (heuristic1 * 10 + 1), (heuristic2 * 10 + 2), (heuristic3 * 10 + 3)]
        #print("new", heuristics)
        heuristics.sort()
        #print("hhsorted", heuristics)

        # pqueue.put (heuristic0 + currentCostSoFar) --> heuristic0   (so on for 1-2-3)
        for i in range(len(currentPuzzle)):  # starting to use paths from the best heuristic value to the worst
            if (heuristics[i] % 10 == 0 and heuristic0 < maxInt):
                if (checkVisited(visited, puz0) == False):  # this state is never visited
                    currentPath.append(0)  # moving up is added to new path
                    newCostSoFar = copy.deepcopy(currentCostSoFar)
                    newCostSoFar += 1  # step cost so far increased
                    visited.append((puz0, newCostSoFar, currentPath))  # adding this state to visited with values
                    pqueue.put( ( (heuristic0 + currentCostSoFar) , [puz0, newCostSoFar, currentPath]) )  # queue the visited state with heuristic value
                else:  # if state is already visited
                    newVisited = []  # new visited after possible change
                    for i in range(len(visited)):
                        oneState = visited.pop()
                        if (oneState[0] != puz0):  # if this is a different state, put it back in
                            newVisited.append(oneState)
                        else:  # if relevant state is found
                            if (newCostSoFar < oneState[1]):  # if new state has lower cost
                                newVisited.append((puz0, newCostSoFar, currentPath))
                                # pqueue.put( (heuristic0, [puz0, newCostSoFar, currentPath]) )
                            else:  # if old state has still least cost
                                newVisited.append(oneState)
                                # pqueue.put(fPath)
                    for i in range(len(newVisited)):
                        item = newVisited.pop()
                        visited.append(item) # to-do global

            elif (heuristics[i] % 10 == 1 and heuristic1 < maxInt):
                if (checkVisited(visited, puz1) == False):  # this state is never visited
                    currentPath.append(1)  # moving up is added to new path
                    newCostSoFar = copy.deepcopy(currentCostSoFar)
                    newCostSoFar += 1  # step cost so far increased
                    visited.append((puz1, newCostSoFar, currentPath))  # adding this state to visited with values
                    pqueue.put(((heuristic1 + currentCostSoFar), [puz1, newCostSoFar, currentPath]))  # queue the visited state with heuristic value
                else:  # if state is already visited
                    newVisited = []  # new visited after possible change
                    for i in range(len(visited)):
                        oneState = visited.pop()
                        if (oneState[0] != puz1):  # if this is a different state, put it back in
                            newVisited.append(oneState)
                        else:  # if relevant state is found
                            if (newCostSoFar < oneState[1]):  # if new state has lower cost
                                newVisited.append((puz1, newCostSoFar, currentPath))
                                # pqueue.put((heuristic1, [puz1, newCostSoFar, currentPath]))
                            else:  # if old state has still least cost
                                newVisited.append(oneState)
                                # pqueue.put(fPath)
                    for i in range(len(newVisited)):
                        item = newVisited.pop()
                        visited.append(item)

            elif (heuristics[i] % 10 == 2 and heuristic2 < maxInt):
                if (checkVisited(visited, puz2) == False):  # this state is never visited
                    currentPath.append(2)  # moving up is added to new path
                    newCostSoFar = copy.deepcopy(currentCostSoFar)
                    newCostSoFar += 1  # step cost so far increased
                    visited.append((puz2, newCostSoFar, currentPath))  # adding this state to visited with values
                    pqueue.put(((heuristic2 + currentCostSoFar), [puz2, newCostSoFar, currentPath]))  # queue the visited state with heuristic value
                else:  # if state is already visited
                    newVisited = []  # new visited after possible change
                    for i in range(len(visited)):
                        oneState = visited.pop()
                        if (oneState[0] != puz2):  # if this is a different state, put it back in
                            newVisited.append(oneState)
                        else:  # if relevant state is found
                            if (newCostSoFar < oneState[1]):  # if new state has lower cost
                                newVisited.append((puz2, newCostSoFar, currentPath))
                                # pqueue.put((heuristic2, [puz2, newCostSoFar, currentPath]))
                            else:  # if old state has still least cost
                                newVisited.append(oneState)
                                # pqueue.put(fPath)
                    for i in range(len(newVisited)):
                        item = newVisited.pop()
                        visited.append(item)

            elif (heuristics[i] % 10 == 3 and heuristic3 < maxInt):
                if (checkVisited(visited, puz3) == False):  # this state is never visited
                    currentPath.append(3)  # moving up is added to new path
                    newCostSoFar = copy.deepcopy(currentCostSoFar)
                    newCostSoFar += 1  # step cost so far increased
                    visited.append((puz3, newCostSoFar, currentPath))  # adding this state to visited with values
                    pqueue.put( ((heuristic3 + currentCostSoFar), [puz3, newCostSoFar, currentPath]))  # queue the visited state with heuristic value
                else:  # if state is already visited
                    newVisited = []  # new visited after possible change
                    for i in range(len(visited)):
                        oneState = visited.pop()
                        if (oneState[0] != puz3):  # if this is a different state, put it back in
                            newVisited.append(oneState)
                        else:  # if relevant state is found
                            if (newCostSoFar < oneState[1]):  # if new state has lower cost
                                newVisited.append((puz3, newCostSoFar, currentPath))
                                # pqueue.put((heuristic3, [puz3, newCostSoFar, currentPath]))
                            else:  # if old state has still least cost
                                newVisited.append(oneState)
                                # pqueue.put(fPath)
                    for i in range(len(newVisited)):
                        item = newVisited.pop()
                        visited.append(item)


def getVisitedState(visitedStates, newState):  # returns the visited state with is (puzzle, costSoFar, path)
    print("inGET")
    for state in visitedStates:
        if (state[0] == newState):
            print("state is ", state)
            print("state[0] is ", state[0])
            return state


def solveFollow(path):
    tempGrid = firstGrid

    print("puzzle was like this in the beginning")
    printer(tempGrid)

    for i in range(len(path)):
        if (path[i] == 0):
            print("empty to up in step ", i + 1)
            tempGrid = moveUp(tempGrid)
            printer(tempGrid)
        elif (path[i] == 1):
            print("empty to down in step ", i + 1)
            tempGrid = moveDown(tempGrid)
            printer(tempGrid)
        elif (path[i] == 2):
            print("empty to left in step ", i + 1)
            tempGrid = moveLeft(tempGrid)
            printer(tempGrid)
        elif (path[i] == 3):
            print("empty to right in step ", i + 1)
            tempGrid = moveRight(tempGrid)
            printer(tempGrid)

    return

printerCount = 2
maxList = []
stateCount = 12
maxInt = 9000000
maxMisplaced = 16

everVisited = 0

finalGrid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, 0]]
T = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, 0]]
S = []
StateNames = []
for i in range(stateCount):
    S.append(copy.deepcopy(T))
    while(S[i] == finalGrid):
        mixer(S[i])
    printer(S[i])
    print()
    print()

for i in range(stateCount):
    Astar(S[i])

print()
print(maxList)

for i in range(stateCount):
    name = "S" + str(i+1)
    StateNames.append(name)

#print(StateNames)

# plotting graph with results
plt.rcParams.update({'font.size': 24})

plt.xlabel("State Names")
plt.ylabel("Max Queue Size")
plt.plot(StateNames, maxList)
plt.show()
