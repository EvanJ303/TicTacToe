player=1
playab=1

gameboard=[0,0,0,0,0,0,0,0,0]

print("[0,0,0]")
print("[0,0,0]")
print("[0,0,0]")

while playab==1:
    if player==1:
        print("P1 TURN")
    else:
        print("P2 TURN")
    punchcount=int(input("SELECT A NUMBER 0-8"))
    if player==1:
        gameboard[punchcount]=1
    else:
        gameboard[punchcount]=2
    rowone=[gameboard[0],gameboard[1],gameboard[2]]
    rowtwo=[gameboard[3],gameboard[4],gameboard[5]]
    rowthree=[gameboard[6],gameboard[7],gameboard[8]]
    colone=[gameboard[0],gameboard[3],gameboard[6]]
    coltwo=[gameboard[1],gameboard[4],gameboard[7]]
    colthree=[gameboard[2],gameboard[5],gameboard[8]]
    diagone=[gameboard[0],gameboard[4],gameboard[8]]
    diagtwo=[gameboard[2],gameboard[4],gameboard[6]]
    print(rowone)
    print(rowtwo)
    print(rowthree)
    if rowone==[1,1,1]:
        break
    if rowtwo==[1,1,1]:
        break
    if rowthree==[1,1,1]:
        break
    if colone==[1,1,1]:
        break
    if coltwo==[1,1,1]:
        break
    if colthree==[1,1,1]:
        break
    if diagone==[1,1,1]:
        break
    if diagtwo==[1,1,1]:
        break
    if rowone==[2,2,2]:
        break
    if rowtwo==[2,2,2]:
        break
    if rowthree==[2,2,2]:
        break
    if colone==[2,2,2]:
        break
    if coltwo==[2,2,2]:
        break
    if colthree==[2,2,2]:
        break
    if diagone==[2,2,2]:
        break
    if diagtwo==[2,2,2]:
        break
    player=(player%2)+1
   
playab=2
if player==1:
    print("P1 WINS")
else:
    print("P2 WINS")