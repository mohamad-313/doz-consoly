from colored import fg,bg,attr
#---------------Initialize Var---------------
board = {key: "?" for key in range(1, 10)}
nobat = "X"

#---------------methods---------------
def isInputValid(input : str) -> bool:
    if input != "" and input.isdigit():
        return 0 < int(input) < 10

def setMoveInBoard(move, nobat) -> bool:
    if board[move] == "?":
        board[move] = nobat
        return True

    return False

def showBoard(Board) -> str:
    board = list(Board.values())
    editedBoard = [ "  ".join(board[ 0 : 3 ]) , "  ".join(board[ 3 : 6 ]) , "  ".join(board[ 6 : 9 ])]
    return "\n".join(editedBoard)

def color(text,color):
    reset = attr(0)
    return "%s%s%s" % (fg(color),text,reset)

def getWinner(board,nobat):

    allWinnerPosition = [[1,2,3], [4,5,6], [7,8,9], [1,4,7],
                        [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    for pos in allWinnerPosition:
        if board[pos[0]] == nobat and board[pos[1]] == nobat and board[pos[2]] == nobat:
            return True

#---------------main while---------------
while True:
    move = input(f"Please enter {nobat} Move:\n")

    if not isInputValid(move):
        print("Please enter a valid move,",end=" ")
        continue

    move = int(move)

    if not setMoveInBoard(move,nobat):
        print("This position is filled,Please enter a move that is not filled")
        continue

    print(showBoard(board))

    winner = "X" if getWinner(board,"X") else ("O" if getWinner(board,"O") else None)

    if winner != None:
        print("Player " + color(winner,("light_red" if winner == "X" else "light_yellow")) + " Winner")
        break

    nobat = "O" if nobat == "X" else "X"

input()
