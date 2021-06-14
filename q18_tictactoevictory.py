# Write a function that will identify if a victory condition exists in a
# tic-tac-toe game.

def victory(board):
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6]:
            return True
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    return False

def main():
    board = ['x','o','','x','x','o','x','o','o']
    board2 = ['','x','x','o','x','o','','o','x']
    print(victory(board))
    print(victory(board2))

if __name__ == '__main__':
    main()
