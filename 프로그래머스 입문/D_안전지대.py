# 내 코드  
import numpy as np

def solution(board):
    board = np.array(board)
    n = board.shape[0]
    for i in range(n) : 
        for j in range(n) : 
            if board[i,j] == 1 :
                board[i-1:j+2, i-1 :j+2] = 1 
    answer = n*n - sum(sum(board))
    return answer
