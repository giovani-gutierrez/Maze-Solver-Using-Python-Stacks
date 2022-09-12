# Maze.py

from Stack import Stack

def solveMaze(maze, startX, startY):
    ''' The maze parameter is a 2D List
    maze. Parameters startX and startY
    are the starting coordinates used.
    Returns True if a path exists and
    the goal was reached, and returns
    False if no path to the goal exists.
    '''
    
    m = Stack()
    m.push([startX, startY])
    count = 1
    maze[startX][startY] = count

    while m.isEmpty() == False:
        
        if maze[startX - 1][startY] == ' ' or \
           maze[startX - 1][startY] == 'G': # check North of current position
            if maze[startX - 1][startY] == 'G':
                return True
            else:
                m.push([startX - 1, startY])
                count += 1
                maze[startX - 1][startY] = count
                startX -= 1

        elif maze[startX][startY - 1] == ' ' or \
             maze[startX][startY - 1] == 'G': # checks West of current position
            if maze[startX][startY - 1] == 'G':
                return True
            else:
                m.push([startX, startY - 1])
                count += 1
                maze[startX][startY - 1] = count
                startY -= 1

        elif maze[startX + 1][startY] == ' ' or \
             maze[startX + 1][startY] == 'G': # checks South of curent position
            if maze[startX + 1][startY] == 'G':
                return True
            else:
                m.push([startX + 1, startY])
                count += 1
                maze[startX + 1][startY] = count
                startX += 1

        elif maze[startX][startY + 1] == ' ' or \
             maze[startX][startY + 1] == 'G': # checks East of current position
            if maze[startX][startY + 1] == 'G':
                return True
            else:
                m.push([startX, startY + 1])
                count += 1
                maze[startX][startY + 1] = count
                startY += 1
                
        else: # goes back to previous position and tries again
            m.pop()
            if m.size() > 0:
                startX = m.peek()[0]
                startY = m.peek()[1]
            else:
                return False
            
    return False
