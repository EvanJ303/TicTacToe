#this is tictactoe with an ai opponent(wip)

board=[[0,0,0],[0,0,0],[0,0,0]]
inviboard=[[],[],[],[],[],[],[],[]]

import random

def updateinviboard(inviboard):
    inviboard=[board[0],board[1],board[2],[board[0][0],board[1][0],board[2][0]],[board[0][1],board[1][1],board[2][1]],
    [board[0][2],board[1][2],board[2][2]],[board[0][0],board[1][1],board[2][2]],[board[0][2],board[1][1],board[2][0]]]
    return inviboard

inviboard=updateinviboard(inviboard)

player=2
playstop=0

for i in board:
    print(i)

while playstop==0:
    player=(player%2)+1
    if player==1:
        print("P1 TURN")
        updateinviboard(inviboard)
        not_taken=0
        while not_taken==0:
            selrow=int(input("SELECT ROW"))
            selcol=int(input("SELECT COLUMN"))
            if board[selrow][selcol]==0:
                not_taken=1
            else:
                print("INVALID COORDS")
    else:
        print("BOT'S TURN")
        skipremaining=0
        for i in range(0,8):
            if inviboard[i]==[0,2,2] or inviboard[i]==[2,0,2] or inviboard[i]==[2,2,0] and skipremaining==0:
                for h in range (0,3):
                    if inviboard[i][h]==0:
                        if i<=2 and skipremaining==0:
                            board[i][h]=2
                            skipremaining=1
                        elif i<=5 and skipremaining==0:
                            board[h][i-3]=2
                            skipremaining=1
                        elif i==6 and skipremaining==0:
                            if h==0 and skipremaining==0:
                                board[0][0]=2
                                skipremaining=1
                            if h==1 and skipremaining==0:
                                board[1][1]=2
                                skipremaining=1
                            if h==2 and skipremaining==0:
                                board[2][2]=2
                                skipremaining=1
                        elif i==7 and skipremaining==0:
                            if h==0 and skipremaining==0:
                                board[0][2]=2
                                skipremaining=1
                            if h==1 and skipremaining==0:
                                board[1][1]=2
                                skipremaining=1
                            if h==2 and skipremaining==0:
                                board[2][0]=2
                                skipremaining=1
                        skipremaining=1
                        inviboard=updateinviboard(inviboard)
        for i in range(0,8):
            if inviboard[i]==[0,1,1] or inviboard[i]==[1,0,1] or inviboard[i]==[1,1,0] and skipremaining==0:
                for h in range (0,3):
                    if inviboard[i][h]==0:
                        if i<=2 and skipremaining==0 :
                            board[i][h]=2
                            skipremaining=1
                        elif i<=5 and skipremaining==0:
                            board[h][i-3]=2
                            skipremaining=1
                        elif i==6 and skipremaining==0:
                            if h==0 and skipremaining==0:
                                board[0][0]=2
                                skipremaining=1
                            if h==1 and skipremaining==0:
                                board[1][1]=2
                                skipremaining=1
                            if h==2 and skipremaining==0:
                                board[2][2]=2
                                skipremaining=1
                        elif i==7 and skipremaining==0:
                            if h==0 and skipremaining==0:
                                board[0][2]=2
                                skipremaining=1
                            if h==1 and skipremaining==0:
                                board[1][1]=2
                                skipremaining=1
                            if h==2 and skipremaining==0:
                                board[2][0]=2
                                skipremaining=1
                        skipremaining=1
                        inviboard=updateinviboard(inviboard)
        if inviboard[1][1]==0 and skipremaining==0:
            inviboard[1][1]=2
            skipremaining=1
            inviboard=updateinviboard(inviboard)
        else:
            if skipremaining==0:
                botnumcheckloop=0
                while botnumcheckloop==0:
                    randnumcheck0=random.randint(0,2)
                    randnumcheck1=random.randint(0,2)
                    if inviboard[randnumcheck0][randnumcheck1]==0:
                        inviboard[randnumcheck0][randnumcheck1]=2
                        botnumcheckloop=1
                        inviboard=updateinviboard(inviboard)
    if player==1:
        board[selrow][selcol]=1
        inviboard=updateinviboard(inviboard)
    for n in board:
        print(n)
    for k in range(0,8):
        if inviboard[k]==[1,1,1] or inviboard[k]==[2,2,2]:
            playstop=1
    if playstop==0:
        draw_check=1
        for i in range(0,3):
            for k in range(0,3):
                if board[i][k]==0:
                    draw_check=0
    if draw_check==1:
        playstop=1

if draw_check==1:
    print("DRAW")
else:
    if player==1:
        print("P1 WINS")
    else: 
        print("BOT WINS")