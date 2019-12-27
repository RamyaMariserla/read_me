import random

def d_board(board):
    
    print("* * * * * * * ")
    print("*",end=" ")
    print(board[7],"|",board[8],"|",board[9],"*")
    print("*",end=" ")
    print("-","-","-","-","-","* ")
    print("*",end=" ")
    print(board[4],"|",board[5],"|",board[6],"*")
    print("*",end=" ")
    print("-","-","-","-","-","*")
    print("*",end=" ")
    print(board[1],"|",board[2],"|",board[3],"*")
    print("*",end=" ")
    print("* * * * * * ")





def position_checker(board):

    kk=[]
    for i in range(1,10):
        if(board[i]==" "):
            kk.append(i)
    return kk
            

def space_check(board,pos):

    if(board[pos]==" "):
        return True
    else:
        return False       
def full_board(board):

    for i in range(1,10):
        if(space_check(board,i)):
            return False
    return True



def choose_player():

    if random.randint(0,1)==0:
        return"Player2"
    return"Player1"
def replay():

    return(input("do u want to play again enter yes or no").lower()[0]=='y')
def win(board,mark):

    return((board[7]==mark and board[8]==mark and board[9]==mark)or
           (board[4]==mark and board[5]==mark and board[6]==mark)or
           (board[1]==mark and board[2]==mark and board[3]==mark)or
           (board[1]==mark and board[5]==mark and board[9]==mark)or
           (board[3]==mark and board[5]==mark and board[7]==mark)or
           (board[7]==mark and board[4]==mark and board[1]==mark)or
           (board[8]==mark and board[5]==mark and board[2]==mark)or
           (board[9]==mark and board[6]==mark and board[3]==mark))

print("lets play tic toc toe")

print("PLAYER1 is X and PLAYER2 is O")


while(1):

    board=[" "]*10
    turn=choose_player()
    print(turn,"will go first")
    while(1):
        if(turn=="Player1"):
            d_board(board)
            v=int(input("player1 enter the position u want to place X"))
            kk=position_checker(board)
            if( v in kk):
               board[v]="X"
            else:
               print("its already filled ,Please enter any of these positions")
               for i in kk:
                  print(i,end=" ")
               print()        
            if(win(board,"X")):
                d_board(board)
                print("Congrats Player1 won the game")
                break
            else:
                if(full_board(board)):
                    d_board(board)
                    print("game is draw")
                    break
                else:
                    turn="Player2"
            
        
        else:
            d_board(board)
            s=int(input("player2 enter the position u want to place O"))
            kk=position_checker(board)
            if(s in kk):
               board[s]="O"
            else:
               print("its already filled ,Please enter any of these positions")
               for i in kk:
                  print(i,end=" ")
               print()
        
            
            if(win(board,"O")):
                d_board(board)
                print("Congrats Player2 won the game")
                break
            else:
                if(full_board(board)):
                    d_board(board)
                    print("game is draw")
                    break
                else:
                    turn="Player1"
    if not replay():
        break
