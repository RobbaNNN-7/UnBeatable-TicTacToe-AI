import pygame # type: ignore
import sys
import numpy as np # type: ignore
from components.colors import *
from components.size import*
from game_structure.structure import*
from minimax.minimax import*

""" Initializing Screen """
""" Function to Draw 2 lines Vertically and 2 lines Horizontally on the Screen"""
""" Function to Draw Either a Circle Or a Cross """
""" Function to Determine the Player """ 
""" Function to Determine the Player """ 
""" Function to Check if Sqare is Full or Not """
""" Function to Determine if Board is Full (TERMINAL STATE) """
""" Function to Determine if a Player Won """

""" Finds the Best move using the Minimax Algorithm Defined Above and Marks that Position"""

# board is our current game state shown above
# depth starts at 0 and increases with each recursive call
# isMaximizing is True for AI's turn (O), False for Human's turn (X)

""" MAIN FUNCTION """

def play_game():
    screen, board = initialize_game()
    drawLines(screen)
    player = 1
    gameOver = False
    winner = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Handle game restart
            if (event.type == pygame.MOUSEBUTTONDOWN and gameOver) or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                board, player, gameOver = reset_game(screen)
                winner = None
                continue
            
            # Handle game moves
            if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = event.pos[1] // SQUARE_SIZE
                
                if isAvailible(board, mouseY, mouseX):
                    mark_square(board, player, mouseY, mouseX)
                    
                    if isWinState(player, board):
                        gameOver = True
                        winner = player
                    elif not isBoardFull(board):
                        player = 2  # AI's turn
                        
                        if best_move(board):
                            if isWinState(2, board):
                                gameOver = True
                                winner = 2
                            player = 1  # Back to human
                        
                    if not gameOver and isBoardFull(board):
                        gameOver = True
                        winner = 0  # Draw

        # Draw current game state
        screen.fill(BLACK)
        drawLines(screen)
        
        if not gameOver:
            draw_action(screen, board)
        else:
            if winner == 1:   ## THIS IS A USELESS FUNCTION !! YOU CAN NEVER WIN !!
                draw_action(screen, board, GREEN)
                drawLines(screen, GREEN)
            elif winner == 2:  # AI wins
                draw_action(screen, board, RED)
                drawLines(screen, RED)
            else:  # Draw
                draw_action(screen, board, GREY)
                drawLines(screen, GREY)
            
            # Draw restart message
            draw_game_over_text(screen, winner)

        pygame.display.update()

if __name__ == '__main__':
    play_game()