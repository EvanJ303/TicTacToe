board=[[0,0,0],[0,0,0],[0,0,0]]

C1=[board[0][0],board[1][0],board[2][0]]
C2=[board[0][1],board[1][1],board[2][1]]
C3=[board[0][2],board[1][2],board[2][2]]
D1=[board[0][0],board[1][1],board[2][2]]
D2=[board[0][2],board[1][1],board[2][0]]

inviboard=[board[0],board[1],board[2],C1,C2,C3,D1,D2]
player=2
playstop=0

# Print Board
for i in board:
    print(i)

while playstop==0:
    player=(player%2)+1
    if player==1:
        print("P1 TURN")
    else:
        print("P2 TURN")
    selrow=int(input("SELECT ROW"))
    selcol=int(input("SELECT COLUMN"))
    if player==1:
        board[selrow][selcol]=1
    else:
        board[selrow][selcol]=2
    C1=[board[0][0],board[1][0],board[2][0]]
    C2=[board[0][1],board[1][1],board[2][1]]
    C3=[board[0][2],board[1][2],board[2][2]]
    D1=[board[0][0],board[1][1],board[2][2]]
    D2=[board[0][2],board[1][1],board[2][0]]
    for n in board:
        print(n)
    for k in range(0,8):
        if inviboard[k]==[1,1,1] or inviboard[k]==[2,2,2]:
            playstop=1

if player==1:
    print("P1 WINS")
else:
    print("P2 WINS")