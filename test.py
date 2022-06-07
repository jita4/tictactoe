from random import randrange
def evaluate(board):
    a=board.find('xxx')
    b=board.find('ooo')
    if a>=0:
        print('Player won!')
          
    if b>=0:
        print('PC won!')        
    else:
        board_find=''
        for i in range(20):
            if board[i]=='x' or board[i]=='o':
                board_find=board[i]+board_find
        if len(board_find)==20:
            print('Nobody won')            
        else:
            return board

def move(board, mark, position):
    if position==0:
        board_move=mark+board[1:]
    if position==19:
        board_move=board[:-2]+mark
    if position>0 and position<19:
        board_move=board[:position]+mark+board[position+1:]
    return board_move

def player_move(board):
    while True:
        pos_player=int(input('Choose your position 0-19  '))
        if pos_player>=0 and pos_player<=19:
            if board[pos_player]=='-':
                 board_player=move(board, 'x', pos_player)
                 break
        else:
             print('Your number is wrong') 
    return board_player     

def pc_move(board):
    while True:
        pos_pc=randrange(0,19)
        if board[pos_pc]=='-':
                 board_pc=move(board, 'o', pos_pc)
                 break
    return  board_pc

def tictactoe(board):
    board_start=board
    while True:
        player_input=player_move(board_start)
        c=player_input.find('xxx')
        if c>=0:
            evaluate_input=(evaluate(player_input))
            print(evaluate_input)
            break
        pc_input=pc_move(player_input)   
        evaluate_input=(evaluate(pc_input))
        d=pc_input.find('ooo')
        if d>=0:
            print(pc_input)
            break  
        board_start=evaluate_input
        print(board_start)
    
     
board_input='---------------------'
tictactoe(board_input)

      





