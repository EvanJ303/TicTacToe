rowone=[0,0,0]
rowtwo=[0,0,0]
rowthree=[0,0,0]
colone=[rowone[0],rowtwo[0],rowthree[0]]
coltwo=[rowone[1],rowtwo[1],rowthree[1]]
colthree=[rowone[2],rowtwo[2],rowthree[2]]
diagone=[rowone[0],rowtwo[1],rowthree[2]]
diagtwo=[rowone[2],rowtwo[1],rowthree[0]]

player=1
playab=1

gameboard=[rowone[0],rowone[1],rowone[2],rowtwo[0],rowtwo[1],rowtwo[2],rowthree[0],rowthree[1],rowthree[2]]

print(rowone)
print(rowtwo)
print(rowthree)

while playab==1:
    if player==1:
        print("P1 TURN")
    else:
        print("P2 TURN")
    punchcount=int(input("SELECT A NUMBER 0-9"))
    if player==1:
        gameboard[punchcount]=1
    else:
        gameboard[punchcount]=2
    rowone=[gameboard[0],gameboard[1],gameboard[2]]
    rowtwo=[gameboard[3],gameboard[4],gameboard[5]]
    rowthree=[gameboard[6],gameboard[7],gameboard[8]]
    colone=[rowone[0],rowtwo[0],rowthree[0]]
    coltwo=[rowone[1],rowtwo[1],rowthree[1]]
    colthree=[rowone[2],rowtwo[2],rowthree[2]]
    diagone=[rowone[0],rowtwo[1],rowthree[2]]
    diagtwo=[rowone[2],rowtwo[1],rowthree[0]]
    print(rowone)
    print(rowtwo)
    print(rowthree)
    if rowone or rowtwo or rowthree or colone or coltwo or colthree or diagone or diagtwo==[1,1,1]or[2,2,2]:
        break
    
playab=2
if player==1:
    print("P1 WINS")
else:
    print("P2 WINS")