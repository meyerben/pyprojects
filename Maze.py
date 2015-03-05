import keyword
#LEARN HOW TO MOVE AN OBJECT IN STRINGS

Win = '''




You Win!

'''
map = [
[ "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "8", "O", "O", "O", "8" ],
[ "8", " ", " ", " ", "8", " ", " ", " ", "8", " ", " ", " ", "8", " ", " ", " ", " ", " ", " ", " ", "8" ],
[ "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", " ", " ", " ", "8", "a", "a", "a", "8" ],
[ "8", " ", " ", " ", "8", " ", " ", " ", "8", " ", " ", " ", " ", " ", " ", " ", "8", " ", " ", " ", "8" ],
[ "a", "a", "a", "a", "a", "a", "a", "a", "a", " ", " ", " ", "a", "a", "a", "a", "8", "a", "a", "a", "8" ],
[ "8", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "8", " ", " ", " ", "8", " ", " ", " ", "8" ],
[ "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "8", "a", "a", "a", "8" ]
]

Win = '''




You Win!

'''

def ShowMaze(walls):
    print("".join(walls[0]))
    print("".join(walls[1]))
    print("".join(walls[2]))
    print("".join(walls[3]))
    print("".join(walls[4]))
    print("".join(walls[5]))
    print("".join(walls[6]))


def FindPickle(maze,object):
    '''takes in a nested list (in the form of a maze) and returns the position
    of the object given as the second object'''
    row = 0
    col = 0
    for i in range(len(maze)): #Runs through each row in the map
        if object in map[i]:   #If the runner is in this row
            row = i            #set row equal to this index
            col = map[i].index(object) #set column equal to this index
        else: 
            row +=0            #added both of these for
            col +=0            #clarity!
    return [row, col]

#print FindPickle(map,"X") #This works!


def MoveDown(maze):
    row = (FindPickle(maze,"X"))[0]
    col = (FindPickle(maze,"X"))[1]
    maze[row].remove("X")               #Removes the X from the first row
    maze[row].insert(col," ")   #inserts the " " into the second row to replace the old x
    del (maze[row+1])[col]        #must use delete because remove can only take 1 argument
    maze[row+1].insert(col,"X")   #Inserts the X into the second list.

def MoveUp(maze):
    row = (FindPickle(maze,"X"))[0]
    col = (FindPickle(maze,"X"))[1]
    maze[row].remove("X")               
    maze[row].insert(col," ")   
    del (maze[row-1])[col]        
    maze[row-1].insert(col,"X")   


def MoveRight(maze):
    row = (FindPickle(maze,"X"))[0]
    col = (FindPickle(maze,"X"))[1]
    maze[row].remove("X")               
    maze[row].insert(col," ")   
    del (maze[row])[col+1]        
    maze[row].insert(col+1,"X")   

def MoveLeft(maze):
    row = (FindPickle(maze,"X"))[0]
    col = (FindPickle(maze,"X"))[1]
    maze[row].remove("X")               
    maze[row].insert(col," ")   
    del (maze[row])[col-1]        
    maze[row].insert(col-1,"X")


        
def getMove(row,col):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('wasd')
        move = raw_input()
        move = move.lower()
        if (move == "w") and (((map[row-1])[col] == "a") or ((map[row-1])[col] == "8")):
            ShowMaze(map)
        elif (move == "s") and (((map[row+1])[col] == "a") or ((map[row+1])[col] == "8")):
            ShowMaze(map)
        elif (move == "d") and (((map[row])[col+1] == "a") or ((map[row])[col+1] == "8")):
            ShowMaze(map)
        elif (move == "a") and (((map[row])[col-1] == "a") or ((map[row])[col-1] == "8")):
            ShowMaze(map)
        elif (move == "w") and ((map[row-1])[col] == "O"):
            print Win
            break
        else: 
            return move

row = (FindPickle(map,"X"))[0]
col = (FindPickle(map,"X"))[1]
GameisDone = False
while True:
    row = (FindPickle(map,"X"))[0]
    col = (FindPickle(map,"X"))[1]
    ShowMaze(map)
    Move = getMove(row,col)
    if Move == "w":
        MoveUp(map)
    elif Move == "s":
        MoveDown(map)
    elif Move == "d":
        MoveRight(map)
    elif Move == "a":
        MoveLeft(map)
    else:
        break
