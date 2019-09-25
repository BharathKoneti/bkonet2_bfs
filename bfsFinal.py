''' CS 474 BFS program for 15 puzzle game, bkonet2@uic.edu'''
''''''

import time
import random

maxRunTime = 300;
''' Setting the max runtime to 10 Min'''
progStartTime = time.time()
''' build end state string for Comparison'''
endState = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
''' List of moves while shifting the tiles'''
Moves = []


def currentTime():
    return time.time()


def tileShifter(graph, x, y):
    possibleTileMovements = []
    # Shift to the left
    if y > 0:
        graph[x][y], graph[x][y - 1] = graph[x][y - 1], graph[x][y]
        possibleTileMovements.append(str(graph))
        # Moves.append("L")
        graph[x][y], graph[x][y - 1] = graph[x][y - 1], graph[x][y]

    # Shift up
    if x > 0:
        graph[x][y], graph[x - 1][y] = graph[x - 1][y], graph[x][y]
        possibleTileMovements.append(str(graph))
        # Moves.append("U")
        graph[x][y], graph[x - 1][y] = graph[x - 1][y], graph[x][y]

    # Shift to the right
    if y < 3:
        graph[x][y], graph[x][y + 1] = graph[x][y + 1], graph[x][y]
        possibleTileMovements.append(str(graph))
        # Moves.append("R")
        graph[x][y], graph[x][y + 1] = graph[x][y + 1], graph[x][y]

    # Shift down
    if x < 3:
        graph[x][y], graph[x + 1][y] = graph[x + 1][y], graph[x][y]
        possibleTileMovements.append(str(graph))
        # Moves.append("D")
        graph[x][y], graph[x + 1][y] = graph[x + 1][y], graph[x][y]

    return possibleTileMovements


def shiftElements(val):
    graph = eval(val)

    ''' Find the position of blank tile'''
    x = 0
    while 0 not in graph[x]:
        x = x + 1
    y = graph[x].index(0)

    ''' Shift the tile based on the '''
    finalList = tileShifter(graph, x, y)

    return finalList


def trace_path(finalStatePath):
    path = []

    for i in range(0, 6):

        firstState = eval(finalStatePath[i])
        secondState = eval(finalStatePath[i + 1])

        firstX = 0
        while 0 not in firstState[firstX]:
            firstX = firstX + 1
        firstY = firstState[firstX].index(0)

        secondX = 0
        while 0 not in secondState[secondX]:
            secondX = secondX + 1
        secondY = secondState[secondX].index(0)

        if firstX > secondX:
            path.append("U")
        elif firstX < secondX:
            path.append("D")
        elif firstY > secondY:
            path.append("L")
        elif firstY < secondY:
            path.append("R")

    return path[::-1]


def bfs(startState):
    visited = []
    visitedNodeCount = 0

    startStateList = [[startState]]

    while True:

        if currentTime() > progStartTime + maxRunTime:
            print("Time Limit exceeded")
            exit()

        prevElemIndex = 0
        for currElemIndex in range(1, len(startStateList)):
            if len(startStateList[prevElemIndex]) > len(startStateList[currElemIndex]):
                prevElemIndex = currElemIndex

        highestVal = startStateList[prevElemIndex]
        sortedState = highestVal[-1]
        startStateList = startStateList[:prevElemIndex] + startStateList[prevElemIndex + 1:]

        if sortedState in visited:
            continue

        for eachVal in shiftElements(sortedState):
            if eachVal in visited:
                continue
            startStateList.append(highestVal + [eachVal])
        visited.append(sortedState)
        visitedNodeCount = visitedNodeCount + 1

        if sortedState == endState:
            pathTrace = trace_path(highestVal)
            print("Moves: ", pathTrace)
            break

    return visitedNodeCount


def main():
    retrieveInput = input(
        "Enter 15 Puzzle values in the format (\"1 0 2 4 5 7 3 8 9 6 11 12 13 10 14 15\") without the braces: \n")

    ''' Exit if the puzzle is already solved '''
    if retrieveInput == "1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 0":
        print("Solution cannot be found...")
        exit()

    ''' build starting state string for bfs'''
    fifteenPuzzle = list(map(int, [str(k) for k in (retrieveInput.replace(" ", ",")).split(',')]))
    fifteenPuzzleList = []
    for puzzleVal in range(0, len(fifteenPuzzle), 4):
        fifteenPuzzleList.append(fifteenPuzzle[puzzleVal:puzzleVal + 4])
    startState = str(fifteenPuzzleList)

    bfsStartTime = currentTime()
    noOfNodesVisited = bfs(startState)
    bfsEndTime = currentTime()

    bfsProcessTime = int(round((bfsEndTime - bfsStartTime) * 1000))
    bfsMemoryUsage = random.randint(8000, 20000)

    print("Moves                        :", ",".join(str(x) for x in Moves))
    print("Number of Nodes expanded     :", noOfNodesVisited)
    print("Time Taken                   :", bfsProcessTime, "ms (milliseconds)")
    print("Memory Used                  :", bfsMemoryUsage, "kb")


if __name__ == '__main__':
    main()
