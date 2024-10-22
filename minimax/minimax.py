import pygame # type: ignore
import sys
import numpy as np # type: ignore
from components.colors import *
from components.size import*
from game_structure.structure import*

def minimax(minimax_board, depth, isMaximizing):
    if isWinState(2, minimax_board):
        return 1
    elif isWinState(1, minimax_board):
        return -1
    elif isBoardFull(minimax_board):
        return 0
    
    if isMaximizing:
        best_score = float('-inf')
        for row in range(ROWS):
            for col in range(COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth+1, False)
                    minimax_board[row][col] = 0
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(ROWS):
            for col in range(COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth+1, True)
                    minimax_board[row][col] = 0
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = float('-inf')
    position = (-1, -1)
    
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    position = (row, col)
    
    if position != (-1, -1):
        mark_square(board, 2, position[0], position[1])
        return True
    return False