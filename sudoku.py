#Sudoku Solver
#pre May 9 edit

from graphics import *
import time

win = GraphWin('sudoku',544,570)

#columns: 0,1,2,3,4,5,6,7,8
board = [[0,2,0,0,0,1,5,0,0],#1
         [7,8,4,6,0,0,1,0,0],#2
         [0,0,0,8,7,0,0,0,9],#3
         [0,0,0,0,0,0,2,9,0],#4
         [0,5,0,7,0,8,0,4,0],#5
         [0,6,2,0,0,0,0,0,0],#6
         [6,0,0,0,8,4,0,0,0],#7
         [0,0,8,0,0,6,9,5,4],#8
         [0,0,1,9,0,0,0,8,0]]#9
#0 is for unknowns

#quadrants: 0,1,2
#           3,4,5
#           6,7,8

#blank at 0 so numbers match up with indices
indices = [[],[-20,-20],[0,-20],[20,-20],
           [-20,0],[0,0],[20,0],
           [-20,20],[0,20],[20,20]]

#will be filled with the Text graphics, accurate to graphics[row][col][note], where note is the actual number displayed to the screen
text   =   [[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],
            [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],
            [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],
            [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],
            [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],
            [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],
            [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],
            [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],
            [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]]

def row(r):#takes in a row number
    return board[r]#returns a list of all entries in that row

def col(c):#takes in a col number
    col = []
    for i in range(9):
        col.append(board[i][c])
    return col#returns a list of all entries in that col

def quadIndex(q):#takes in a quadrant number
    r = []
    c = []
    if q==0:
        r = [0,1,2]
        c = [0,1,2]
    if q==1:
        r = [0,1,2]
        c = [3,4,5]
    if q==2:
        r = [0,1,2]
        c = [6,7,8]
    if q==3:
        r = [3,4,5]
        c = [0,1,2]
    if q==4:
        r = [3,4,5]
        c = [3,4,5]
    if q==5:
        r = [3,4,5]
        c = [6,7,8]
    if q==6:
        r = [6,7,8]
        c = [0,1,2]
    if q==7:
        r = [6,7,8]
        c = [3,4,5]
    if q==8:
        r = [6,7,8]
        c = [6,7,8]
    return r,c#returns the range of its rows and cols (as 2 lists)

def quad(q):#takes in a quadrant number
    r,c = quadIndex(q)
    quad = []
    for i in r:
        for j in c:
            quad.append(board[i][j])
    return quad#returns a list of all entries in that quadrant

def findQuad(row,col):#takes in a row&col index, returns the quadrant that box is in
    if row <= 2:
        if col <= 2:
            return 0
        elif col <= 5:
            return 1
        return 2
    elif row <= 5:
        if col <= 2:
            return 3
        elif col <= 5:
            return 4
        return 5
    elif row <= 8:
        if col <= 2:
            return 6
        elif col <= 5:
            return 7
        return 8

def search(lst,num):
    for i in lst:
        if i == num:
            return True#returns True if num is one of the entries
    return False#otherwise, returns False

def remove(lst,num):
    try:
        lst.remove(num)#if num is in list, removes it and returns new list
        return lst
    except ValueError:#otherwise, just returns the initial list
        return lst

def removeNotes(r,c,num):
    #remove num from notes in row and col
    for i in range(9):
        if type(board[r][i])==list:
            board[r][i] = remove(board[r][i],num)
            unNote(r,i,num)
        if type(board[i][c])==list:
            board[i][c] = remove(board[i][c],num)
            unNote(i,c,num)
                                
    #remove num from notes in quad
    quadR,quadC = quadIndex(findQuad(r,c))
    for i in quadR:
        for j in quadC:
            if type(board[i][j])==list:
                board[i][j] = remove(board[i][j],num)
                unNote(i,j,num)

def removeAdjRow(row,quad,num):#removes num from notes in row, skipping over quad
    if quad==0 or quad==3 or quad==6:
        index = [3,4,5,6,7,8]
    elif quad==1 or quad==4 or quad==7:
        index = [0,1,2,6,7,8]
    else:#quad 2,5,8
        index = [0,1,2,3,4,5]
    for i in index:
        if type(board[row][i])==list:
            board[row][i]=remove(board[row][i],num)
            unNote(row,i,num)

def removeAdjCol(col,quad,num):#removes num from notes in col, skipping over quad
    if quad==0 or quad==1 or quad==2:
        index = [3,4,5,6,7,8]
    elif quad==3 or quad==4 or quad==5:
        index = [0,1,2,6,7,8]
    else:#quad 6,7,8
        index = [0,1,2,3,4,5]
    for i in index:
        if type(board[i][col])==list:
            board[i][col]=remove(board[i][col],num)
            unNote(i,col,num)

def removeQRows(q,num,row):#remove num from notes in q, skipping over row (0,1,or 2)
    quadR,quadC = quadIndex(q)
    del quadR[row]
    for r in quadR:
        for c in quadC:
            if type(board[r][c])==list:
                remove(board[r][c],num)
                unNote(r,c,num)

def removeQCols(q,num,col):#removes num from notes in q, skipping over col (0,1,or 2)
    quadR,quadC = quadIndex(q)
    del quadC[col]
    for c in quadC:
        for r in quadR:
            if type(board[r][c])==list:
                remove(board[r][c],num)
                unNote(r,c,num)

def rowOccurence(q,num):
    quadR,quadC = quadIndex(q)
    rows = []
    for r in quadR:
        qRowCount = 0
        for c in quadC:
            if type(board[r][c])==list:
                if search(board[r][c],num):
                    qRowCount+=1
        rows.append(qRowCount)
    return rows#returns a list [?,?,?] of the # of times the num appears in each row of quadrant

def colOccurence(q,num):
    quadR,quadC = quadIndex(q)
    cols = []
    for c in quadC:
        qColCount = 0
        for r in quadR:
            if type(board[r][c])==list:
                if search(board[r][c],num):
                    qColCount+=1
        cols.append(qColCount)
    return cols#returns a list [?,?,?] of the # of times the num appears in each col of the quadrant

def notes():#replaces 0s on board with list of possible nums
    for r in range(9):
        for c in range(9):
            if board[r][c]==0:
                q = findQuad(r,c)
                lst = []
                for note in range(1,10):
                    inRow = row(r)
                    inCol = col(c)
                    inQuad = quad(q)                    
                    if(not search(inRow,note) and not search(inCol,note) and not search(inQuad,note)):
                        lst.append(note)
                board[r][c] = lst

def unNote(r,c,num):#removes Text of note from screen, and graphics 3D list
    if type(text[r][c][num])!=int:
        text[r][c][num].undraw()
        text[r][c][num]=num
        time.sleep(0.05)#**CONTROL DELAY**

def textNew(r,c,num):
    for note in range(1,10):#if there are any notes still left, remove them
        unNote(r,c,note)
    message = Text(Point(c*60+32,r*60+32),str(num))#create text for solved num
    message.setSize(36)
    message.setTextColor('blue')
    message.draw(win)#draw to window
    text[r][c]=message

def solve():
    for r in range(9):
        for c in range(9):
            #for each list in board, if only one note, set it to be that
            if type(board[r][c])==list:
                    if len(board[r][c])==1:
                        num = board[r][c][0]
                        board[r][c] = num#set the place to be that number
                        removeNotes(r,c,num)#remove from notes
                        textNew(r,c,num)        
            #for each num, sum instances in row, col, quad (seperately)
            for num in range(1,10):
                rowCount = 0
                colCount = 0
                quadCount = 0
                #board coordinate stored of the instance of the num
                onlyR = ()
                onlyC = ()
                onlyQ = ()
                for i in range(9):
                    if type(board[r][i])==list:
                        if search(board[r][i],num):
                            rowCount += 1
                            onlyR = (r,i)
                    if type(board[i][c])==list:
                        if search(board[i][c],num):
                            colCount += 1
                            onlyC = (i,c)
                quadR,quadC = quadIndex(findQuad(r,c))
                for i in quadR:
                    for j in quadC:
                        if type(board[i][j])==list:
                            if search(board[i][j],num):
                                quadCount += 1
                                onlyQ = (i,j)
                #if the num only occurs once, it must be the correct num
                if rowCount==1:
                    board[onlyR[0]][onlyR[1]]=num#set number in place
                    removeNotes(onlyR[0],onlyR[1],num)#remove from notes
                    textNew(onlyR[0],onlyR[1],num)
                elif colCount==1:
                    board[onlyC[0]][onlyC[1]]=num#set number in place
                    removeNotes(onlyC[0],onlyC[1],num)#remove from notes
                    textNew(onlyC[0],onlyC[1],num)
                elif quadCount==1:
                    board[onlyQ[0]][onlyQ[1]]=num#set number in place
                    removeNotes(onlyQ[0],onlyQ[1],num)#remove from notes
                    textNew(onlyQ[0],onlyQ[1],num)

    for q in range(9):
            quadR, quadC = quadIndex(q)
            for num in range(1,10):
                #if num only appears in one row of a quadrant, it mustn't be in that row of the parallel quadrants
                rowInstances = rowOccurence(q,num)
                if rowInstances[0]!=0 and rowInstances[1]==0 and rowInstances[2]==0:#[?,0,0]
                    removeAdjRow(quadR[0],q,num)#remove notes from 1st row of adjacent quad
                elif rowInstances[0]==0 and rowInstances[1]!=0 and rowInstances[2]==0:#[0,?,0]
                    removeAdjRow(quadR[1],q,num)#remove notes from 2nd row of adjacent quad
                elif rowInstances[0]==0 and rowInstances[1]==0 and rowInstances[2]!=0:#[0,0,?]
                    removeAdjRow(quadR[2],q,num)#remove notes from 3rd row of adjacent quad
                #if num only appears in one col of a quadrant, it mustn't be in that col of the parallel quadrants
                colInstances = colOccurence(q,num)
                if colInstances[0]!=0 and colInstances[1]==0 and colInstances[2]==0:#[?,0,0]
                    removeAdjCol(quadC[0],q,num)#remove notes from 1st col of adjacent quad
                elif colInstances[0]==0 and colInstances[1]!=0 and colInstances[2]==0:#[0,?,0]
                    removeAdjCol(quadC[1],q,num)#remove notes from 2nd col of adjacent quad
                elif colInstances[0]==0 and colInstances[1]==0 and colInstances[2]!=0:#[0,0,?]
                    removeAdjCol(quadC[2],q,num)#remove notes from 3rd row of adjacent quad

    #for each pair of horizontally aligned quadrants:
    for quadPair in [[0,1,2],[1,2,0],[0,2,1],[3,4,5],[4,5,3],[3,5,4],[6,7,8],[7,8,6],[6,8,7]]:
        #if num appears in 2 rows of 2 quadrants, it must be in 3rd row of 3rd quadrant
        for num in range(1,10):
            rows1 = rowOccurence(quadPair[0],num)
            rows2 = rowOccurence(quadPair[1],num)
            if rows1[0] and rows1[1] and not rows1[2] and rows2[0] and rows2[1] and not rows2[2]:
                removeQRows(quadPair[2],num,2)#[0,0,?]
            if not rows1[0] and rows1[1] and rows1[2] and not rows2[0] and rows2[1] and rows2[2]:
                removeQRows(quadPair[2],num,0)#[?,0,0]
            if rows1[0] and not rows1[1] and rows1[2] and rows2[0] and not rows2[1] and rows2[2]:
                removeQRows(quadPair[2],num,1)#[0,?,0]
    #for each pair of vertically aligned quadrants:
    for quadPair in [[0,3,6],[3,6,0],[0,6,3],[1,4,7],[4,7,1],[1,7,4],[2,5,8],[5,8,2],[2,8,5]]:
        #if num appears in 2 cols of 2 quadrants, it must be in 3rd col of 3rd quadrant
        for num in range(1,10):
            cols1 = colOccurence(quadPair[0],num)
            cols2 = colOccurence(quadPair[1],num)
            if cols1[0] and cols1[1] and not cols1[2] and cols2[0] and cols2[1] and not cols2[2]:
                removeQCols(quadPair[2],num,2)#[0,0,?]
            if not cols1[0] and cols1[1] and cols1[2] and not cols2[0] and cols2[1] and cols2[2]:
                removeQCols(quadPair[2],num,0)#[?,0,0]
            if cols1[0] and not cols1[1] and cols1[2] and cols2[0] and not cols2[1] and cols2[2]:
                removeQCols(quadPair[2],num,1)#[0,?,0]

    #hidden pairs
    #for each pair of boxes in a row or col:
    #if the only occurences of 2 nums are in 2 boxes, they mustn't be anything else
    for r in range(9):
        nums = [[]]#initializes with an empty list so that num=1 will be at nums[1]
        for num in range(1,10):
            numPlaces = []
            for c in range(9):
                if type(board[r][c])==list:
                    if search(board[r][c],num):
                        numPlaces.append(c)
            nums.append(numPlaces)
        for i in range(1,10):
            for j in range(i+1,10):
                if nums[i]==nums[j]:
                    if len(nums[i])==2:
                        col1 = nums[i][0]
                        col2 = nums[i][1]
                        board[r][col1]=[i,j]#box should only have notes for the pair
                        board[r][col2]=[i,j]#box should only have notes for the pair
                        for note in range(9):
                            if note!=i and note!=j:
                                unNote(r,col1,note)
                            if note!=i and note!=j:
                                unNote(r,col2,note)                        
    for c in range(9):
        nums = [[]]
        for num in range(1,10):
            numPlaces = []
            for r in range(9):
                if type(board[r][c])==list:
                    if search(board[r][c],num):
                        numPlaces.append(r)
            nums.append(numPlaces)
        for i in range(1,10):
            for j in range(i+1,10):
                if nums[i]==nums[j]:
                    if len(nums[i])==2:
                        row1 = nums[i][0]
                        row2 = nums[i][1]
                        board[row1][c]=[i,j]
                        board[row2][c]=[i,j]
                        for note in range(9):
                            if note!=i and note!=j:
                                unNote(row1,c,note)
                            if note!=i and note!=j:
                                unNote(row2,c,note)

    #if theres a pair of boxes with the same pair of numbers in it
    #they must be in one of those spots only    
    for i in range(9):
        for j in range(i+1,9):#for each possible pair of numbers
            for r in range(9):#for each row:
                    if board[r][i]==board[r][j]:
                        if type(board[r][i])==list:
                            if len(board[r][i])==2:
                                num1 = board[r][i][0]
                                num2 = board[r][i][1]
                                cols = [0,1,2,3,4,5,6,7,8]
                                cols = remove(cols,i)
                                cols = remove(cols,j)
                                #remove num1&num2 from row r except for from col i and j
                                for c in cols:
                                    if type(board[r][c])==list:
                                        remove(board[r][c],num1)
                                        remove(board[r][c],num2)
                                        unNote(r,c,num1)
                                        unNote(r,c,num2)
            for c in range(9):#for each col:
                    if board[i][c]==board[j][c]:
                        if type(board[i][c])==list:
                            if len(board[i][c])==2:
                                num1 = board[i][c][0]
                                num2 = board[i][c][1]
                                rows = [0,1,2,3,4,5,6,7,8]
                                rows = remove(rows,i)
                                rows = remove(rows,j)
                                #remove num1&num2 from col c except for row i and row j
                                for r in rows:
                                    if type(board[r][c])==list:
                                        remove(board[r][c],num1)
                                        remove(board[r][c],num2)
                                        unNote(r,c,num1)
                                        unNote(r,c,num2)

def show():#prints the board to the console
    print('=========================')
    for r in range(len(board)):
        print(end='| ')
        for c in range(len(board[r])):
            if c==2 or c==5 or c==8:
                print(board[r][c], end=' | ')
            else:
                print(board[r][c], end=' ')
        if r==2 or r==5 or r==8:
            print('\n=========================')
        else:
            print('\n-------------------------')
    print('\n')

def unknown():#counts up how many blanks there are
    numUnknown = 0
    for r in range(9):
        for c in range(9):
            if type(board[r][c])==list:
                numUnknown+=1
    return numUnknown

def graphics():#draws original board to window, modifications made later in textNew and unNote
    for i in range(10):#prints lines
        line1 = Line(Point(2,i*60+2),Point(542,i*60+2))
        line2 = Line(Point(i*60+2,2),Point(i*60+2,542))
        if i%3==0:
            line1.setWidth(4)
            line2.setWidth(4)
        line1.draw(win)
        line2.draw(win)
    for r in range(9):
        for c in range(9):
            if not type(board[r][c])==list and board[r][c]!=0:#draws the starting numbers to the window
                message = Text(Point(c*60+32,r*60+32),str(board[r][c]))
                message.setSize(36)
                message.draw(win)
                text[r][c]=message
            elif type(board[r][c])==list:
                for note in board[r][c]:#draws all notes to the window
                    message = Text(Point(c*60+32+indices[note][0],r*60+32+indices[note][1]),str(note))
                    message.setSize(12)
                    message.draw(win)
                    text[r][c][note]=message
     
def sudoku():
    while(unknown()!=0):
        blanksLeft = unknown()
        solve()
        if unknown()==blanksLeft:
            break
    if unknown():
        show()










#returns row or col based on the y or x of the pixel
def locate(i):
    if i < 62:
        return 0
    elif i < 122:
        return 1
    elif i < 182:
        return 2
    elif i < 242:
        return 3
    elif i < 302:
        return 4
    elif i < 362:
        return 5
    elif i < 422:
        return 6
    elif i < 482:
        return 7
    else:
        return 8

def startText(r,c,num):
    message = Text(Point(c*60+32,r*60+32),str(num))#create text for solved num
    message.setSize(36)
    message.setTextColor('black')
    message.draw(win)#draw to window
    text[r][c]=message

def readNum(x,y):
    row = locate(y)#find based on y
    col = locate(x)#find based on x
    num = int(input('num:'))
    if board[row][col]==0:
        startText(row,col,num)
    else:
        text[row][col].undraw()
        startText(row,col,num)
    board[row][col]=num

def start():
    solveButton = Rectangle(Point(244,550),Point(300,570))
    solveButton.setFill('green')
    solveButton.draw(win)
    solve = Text(Point(272,560),str('Solve'))
    solve.setTextColor('white')
    solve.setSize(16)
    solve.draw(win)
    noteButton = Rectangle(Point(64,550),Point(120,570))
    noteButton.setFill('blue')
    noteButton.draw(win)
    note = Text(Point(92,560),str('Notes'))
    note.setTextColor('white')
    note.setSize(16)
    note.draw(win)
        
    graphics()
    doneNotes = False
    while(True):
        p = win.getMouse()#stalls until click occurs
        x = p.x
        y = p.y
        if 64<x and x<120 and y > 550:
            noteButton.undraw()
            note.undraw()
            notes()
            graphics()
            doneNotes = True
        elif 244<x and x<300 and y > 550:
            solveButton.undraw()
            solve.undraw()
            noteButton.undraw()
            note.undraw()
            if doneNotes==False:
                notes()
                graphics()
            sudoku()
        else:
            readNum(x,y)
start()
