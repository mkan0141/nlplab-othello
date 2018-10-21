NONE  = 0
BLACK = 1
WHITE = 2

def decision(board):
    x = 0
    y = 0
    w = 0
    b = 0

    while y < 8:
        while x < 8:
            if board[x][y] == WHITE:
                w += 1
            elif board[x][y] == BLACK:
                b += 1              
            x += 1
        x = 0
        y += 1
    
    if w > b:
        return WHITE
    elif w < b:
        return BLACK
    elif w == b:
        return NONE
