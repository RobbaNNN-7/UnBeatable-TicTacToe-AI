Unbeatable Tic-Tac-Toe Using Minimax
Overview
This project is an implementation of the classic Tic-Tac-Toe game, featuring an unbeatable AI opponent using the Minimax algorithm. The AI ensures that the player can never win, resulting in either a draw or a loss for the player.

Features
Unbeatable AI: The AI utilizes the Minimax algorithm to guarantee the best possible move, making it impossible for the player to win.
Draw or Lose: The player can only draw or lose, with the AI always making the optimal moves.
Simple GUI: The game features a user-friendly interface built with Pygame, allowing easy interaction with the Tic-Tac-Toe board.

git clone https://github.com/yourusername/unbeatable-tictactoe.git
cd unbeatable-tictactoe

pip install -r requirements.txt

python tic_tac_toe.py

Minimax Algorithm
The Minimax algorithm is used to determine the optimal move for the AI. Here's a high-level explanation of how it works:

The algorithm recursively explores all possible moves for both the player and the AI.
It assigns a score to each possible board state:
+1 for an AI win,
-1 for a player win,
0 for a draw.
The AI always chooses the move that maximizes its chances of winning while minimizing the player's chances

Future Enhancements
Multiplayer Mode: Add an option to allow two players to compete against each other.
Difficulty Levels: Add different AI difficulties (e.g., easy, medium, hard) by tweaking the Minimax algorithm or using random moves.

License
This project is licensed under the MIT License. Feel free to modify and use it as needed.

