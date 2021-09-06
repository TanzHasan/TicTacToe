def check(board):
    Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in Wins:
        if board[i[0]] != " ":
            if board[i[0]] == board[i[1]] == board[i[2]]:
                return True
    return False

def pmove (board):
    pos = int(input("choose your position: "))
    if board[pos-1] == " ":
        return pos
    else:
        print ("choose again")
        return pmove (board)

def emove(board, sign, pos):
    #print (board)
    if check (board):
        #If sign is X then O must have won on the previous round
        if sign == "X":
            #print ("working")
            return [pos, 10] #position, value
        else:
            return [pos, 0]
    else:
        #checks draws
        if not " " in board:
            return [pos, 9]
    choices = []
    for i in range(len(board)):
        if board[i] == " ":
            #position, value
            change = [" "]*9
            for j in range(len(board)):
                change[j] = board[j]
            change[i] = sign
            if sign == "X":
                branch = emove (change, "O", i)
            else:
                branch = emove (change, "X", i)
            choices.append(branch)
    nvalue = 0
    if sign == "X":
        #Max
        current = choices[0]
        for k in choices:
            nvalue +=k[1]
            if k[1] < current[1]:
                current = k
    else:
        current =choices[0]
        for k in choices:
            nvalue +=k[1]
            if k[1] > current[1]:
                current = k #Min
    if pos != -1:
        current[0] = pos
    current[1] = nvalue
    return current

def displayboard(board):
    print ("-----")
    print (board[0] +"|" + board [1] + "|" + board[2])
    print ("-----")
    print (board[3] +"|" + board [4] + "|" + board[5])
    print ("-----")
    print (board[6] +"|" + board [7] + "|" + board[8])
    print ("-----")

def main ():
    print ("You will be playing against an AI, these are the positions")
    displayboard (["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    play = True
    while (play):
        turn = 0
        board = [" "]*9
        mode = input("choose whether you wish to go first: X or second: O ")
        if mode.capitalize() == "X":
            emode = "O"
            mode = "X"
        else:
            mode = "O"
            emode = "X"
        while (turn<9):
            if (turn %2) == 0:
                if mode == "X":
                    print ("Your Move")
                    change = pmove(board)
                    board[change-1] = "X"
                else:
                    print ("AI Move")
                    change = emove(board, "X", -1)
                    board[change[0]] = "X"
            else:
                if mode == "O":
                    print ("Your Move")
                    change = pmove(board)
                    board[change-1] = "O"
                else:
                    print ("AI Move")
                    change = emove(board, "O", -1)
                    board[change[0]] = "O"
            displayboard(board)
            turn +=1
            if check (board):
                turn = 9
            if " " not in board:
                turn = 9
        rewind =input("Game Over! Type anything other than n to play again\n")
        if rewind == "n":
            play = False
if __name__ == "__main__":
    main ()
