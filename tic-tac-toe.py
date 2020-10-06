#tic tac toe game
import random

def display_board(board):
    #using string formatting to use placeholders
    print(f'''
    {board[7]}|{board[8]}|{board[9]}                            7 | 8 | 9
    ---+---+---                           ---+---+---
    {board[4]}|{board[5]}|{board[6]}            Positions -->   4 | 5 | 6
    ---+---+---                           ---+---+---
    {board[1]}|{board[2]}|{board[3]}                            1 | 2 | 3

    ''')

#method to take input of position
def valid_input():
    while True:
        pos = input("Enter position: ")
        #check if position in valid range
        if pos != " ":
            try: 
                if int(pos) in range (1,10):
                    pos = int(pos)      #typecast to integer
                    break
                else:
                    print("Number is out of range.")
            except:
                print("Invalid entry.")
        else:
            #" " means exit from game
            print("Thank you for playing Tic Tac Toe !")
            exit()
    return(pos)

#method to check if the position is valid
def valid_pos(turn,board):
    print(f"{turn} chance to play.")
    while True: 
        pos = valid_input()
        #if position is vacant
        if board[pos] == "   ":
            board[pos] = turn     #mark the position
            break
        else:
            print("Cannot overwrite, please enter new position.")

def check(board):
    check = False

    #check rows
    if board[1]==board[2]==board[3] != "   " or board[4]==board[5]==board[6] != "   " or board[7]==board[8]==board[9] != "   ":
        check = True
    #check columns
    elif board[1]==board[4]==board[7] != "   " or board[2]==board[5]==board[8] != "   " or board[3]==board[6]==board[9] != "   ":
        check = True
    #check diagonals
    elif board[1]==board[5]==board[9] != "   " or board[3]==board[5]==board[7] != "   " :
        check = True
    return check


def user_input(board, symbol):
    sym1, sym2 = symbol[random.randint(0,1)]
    #sym1 will be going 1st always
    print(f"{sym1} is going first")
    display_board(board)

    #the game has 9 chances
    for i in range (9):
        if i%2 == 0 :
            #turn of sym1
            turn = " "+sym1+" "
            valid_pos(turn,board)
        else:
            #turn of sym2
            turn = " "+sym2+" "
            valid_pos(turn,board)
        display_board(board)

        #one of the symbols has been placed 3 or more times
        if i >= 4 :
            #check = check(board)
            if check(board):
                if i%2 == 0:
                    print(f"{sym1} has won!!")
                else:
                    print(f"{sym2} has won!!")
                break

        #if i is 8 it means tie
        if i == 8:
            print("Its a TIE! No onw won :(")




def game():

    print("\nLet's play Tic Tac Toe !!")
    #list containing contents of board
    board = ["0th index for adjustment :)","   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ","   "]
    #markers
    symbol = [("X", "O"), ("O", "X")]

    while True:
        marker = input("\nEnter your marker: ").upper()
        if marker == "X" or marker == "O" :
            user_input(board,symbol)
            break
        else:
            print("The marker should be X or O only.")


def main():
    game()
    while input("\nDo you want to play again Y/N : ").upper() == "Y":
        game()
    print("\nThank you for playing.")


if __name__ == "__main__":
        main()