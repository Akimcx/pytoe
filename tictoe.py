from random import randrange as rand
computer_pawn = "X"
user_pawn = "O"
board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def check_valid_move(move,board):
   pass 
    
def display_board(board):
    for i in range(len(board)):
        print("+-------+-------+-------+")
        print("|                       |")
        for j in range(len(board[i])):
            print("|   ", end="")
            print(board[i][j], end="   ")
        print("|")
        print("|                       |")
    print("+-------+-------+-------+")

def enter_move(board):
    cont = True
    while cont:
        try:
            user_move = int(input("Enter your move: "))
            if(user_move > 0 and user_move < 10):
                possible_moves = make_list_of_free_fields(board)
                for m in possible_moves:
                    move = m[0]
                    if(move == user_move):
                        board[m[1]][m[2]] = 'O'
                        cont = False
                        break
                else:
                    print("You cannot make a move to the square %d" % user_move)
            else:
                print("You must enter a number >0 and <10\n")
        except:
            print("You must enter a number")
            

def make_list_of_free_fields(board):
    moves = []
    for i in range(len(board)):
       for j in range(len(board)):
           el = board[i][j] 
           if(isinstance(el,int)):
               col = (el - 1) % 3
               row = (el - 1) // 3
               if col > 3:
                   col -= 3
               moves.append((el, row, col))
    return moves

def victory_for(board, sign):
    pass

def draw_move(board):
    cont = True
    while cont:
        computer_move = rand(1,9)
        possible_moves = make_list_of_free_fields(board)
        for m in possible_moves:
            move = m[0]
            if(move == computer_move):
                board[m[1]][m[2]] = 'X'
                cont = False
                break
            
board[1][1] = 'X'
while True:
    display_board(board)
    enter_move(board)
    display_board(board)
    draw_move(board)
#print(board, len(board))
#print(board[1], len(board[1]))
