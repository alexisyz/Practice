#Tetris in matrix 10*10
def Left(m):
    n = 10
    for i in range(n):
        for j in range(n):
            if m[i][j] != 0 and n != 0:
                if j != 0:
                    if (i > 0 and m[i-1][0] != 0) or (i < 9 and m[i+1][0] != 0): #Verify limits (Piece Extra Case).
                        n = 0

                    m[i][j-1] = m[i][j]
                    m[i][j] = 0
                else:
                    n = 0
    
    return m

def Right(m):
    n = 10
    for i in range(n):
        for j in range(n):
            if m[i][9-j] != 0 and n != 0:
                if j != 0:
                    if (i > 0 and m[i-1][9] != 0) or (i < 9 and m[i+1][9] != 0): #Verify limits (Piece Extra Case).
                        n = 0

                    m[i][9-j+1] = m[i][9-j]
                    m[i][9-j] = 0
                else:
                    n = 0
    
    return m

def Down(m):
    n = 10
    for i in range(n):
        for j in range(n):
            if m[9-i][j] != 0 and n != 0:
                if i != 0:
                    m[9-i+1][j] = m[9-i][j]
                    m[9-i][j] = 0
                else:
                    n = 0
    
    return m

def Rotate(m):
    global c
    n = 10
    f1 = False
    f2 = False
    for i in range(n):
        for j in range(n):
            if (f1 and f2) or (m[i][j] == 1 and (i == 0 or i == 9 or j == 0 or j == 9)):
                n = 0
            
            if n != 0:
                if m[i][j] == 1 and f1 == False: #Base Piece.
                    if m[i][j+1] == 1: #Horizontal.
                        m[i][j] = 0
                        m[i][j+2] = 0
                        m[i+1][j+1] = 1
                        m[i-1][j+1] = 1
                    else: #Vertical.
                        m[i][j] = 0
                        m[i+2][j] = 0
                        m[i+1][j-1] = 1
                        m[i+1][j+1] = 1
                    f1 = True
                elif m[i][j] == 2 and f2 == False: #Extra Piece.
                    m[i][j] = 0
                    m[i+v[c]][j+v[c+4]] = 2 #Move to Corner.
                    c = c + 1 #Next Position of Part 2 to Piece
                    f2 = True
    return m



m = [[0 for _ in range(10)]for _ in range(10)] #Game.
v = [0,2,0,-2,2,0,-2,0] #Part Piece Position.
c = 0 #Count.
u = "" #Option.

#Make Piece
m[0][0] = 2
for j in range(3):
    m[1][j] = 1

while u != "S":
    print("Choose some Action: I: Left, D: Right, A: Down, R: Rotate (NO ROTATE IN THE LIMITS)")
    u = input()
    if u == "I": #Left.
        m = Left(m)
    elif u == "D": #Right.
        m = Right(m)
    elif u == "A": #Down.
        m = Down(m)
    elif u == "R": #Rotate
        m = Rotate(m)
    
    if c == 4: #Reset
        c = 0

    for i in range(10):
        s = "" #Reset String
        for j in range(10):
            s = s + str(m[i][j]) + " "
        print(s) #Print Matrix
