import pygame # type: ignore
import sys
import numpy as np # type: ignore
from components.colors import *
from components.size import*

pygame.init()  # This initializes Pygame itself
pygame.font.init()

""" Initializing Screen """
def initialize_game():
    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption("TIC TAC TOE WITH AI - Press R to restart")
    screen.fill(BLACK)
    board = np.zeros((ROWS, COLS))
    return screen, board

def reset_game(screen):
    """Reset all game states to initial values"""
    screen.fill(BLACK)
    board = np.zeros((ROWS, COLS))
    drawLines(screen)
    return board, 1, False  # Returns new board, player 1's turn, game not over

def draw_game_over_text(screen, winner):
    """Draw game over message and restart instructions"""
    font = pygame.font.Font(None, 36)
    
    if winner == 1:
        text = font.render("Player Wins! Click or press R to restart", True, GREEN)
    elif winner == 2:
        text = font.render("AI Wins! Click or press R to restart", True, RED)
    else:
        text = font.render("Draw! Click or press R to restart", True, GREY)
    
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 30))
    screen.blit(text, text_rect)

def drawLines(screen, color=WHITE):
    for i in range(1, COLS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE*i), (WIDTH, SQUARE_SIZE*i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE*i, 0), (SQUARE_SIZE*i, HEIGHT), LINE_WIDTH)

def draw_action(screen, board, color=WHITE):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, 
                    (int(col*SQUARE_SIZE + SQUARE_SIZE//2), int(row*SQUARE_SIZE + SQUARE_SIZE//2)), 
                    CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, 
                    (col*SQUARE_SIZE + SQUARE_SIZE//4, row*SQUARE_SIZE + SQUARE_SIZE//4),
                    (col*SQUARE_SIZE + 3*SQUARE_SIZE//4, row*SQUARE_SIZE + 3*SQUARE_SIZE//4),
                    CROSS_WIDTH)
                pygame.draw.line(screen, color,
                    (col*SQUARE_SIZE + SQUARE_SIZE//4, row*SQUARE_SIZE + 3*SQUARE_SIZE//4),
                    (col*SQUARE_SIZE + 3*SQUARE_SIZE//4, row*SQUARE_SIZE + SQUARE_SIZE//4),
                    CROSS_WIDTH)

def mark_square(board, player, row, col):
    board[row][col] = player

def isAvailible(board, row, col):
    return board[row][col] == 0

def isBoardFull(checkBoard):
    return not any(checkBoard[row][col] == 0 for row in range(ROWS) for col in range(COLS))

def isWinState(player, checkBoard):
    # Check rows and columns
    for i in range(ROWS):
        if all(checkBoard[i][j] == player for j in range(COLS)) or \
           all(checkBoard[j][i] == player for j in range(ROWS)):
            return True
    
    # Check diagonals
    if all(checkBoard[i][i] == player for i in range(ROWS)) or \
       all(checkBoard[i][ROWS-1-i] == player for i in range(ROWS)):
        return True
    
    return False

