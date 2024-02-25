# Battleship Game


## Introduction
 - Battleship is a classic game where players try to sink each other's ships on a grid. This Python implementation allows you to play agains the computer, trying to sink its hidden ships before runing out of turns.


## Futures 
 - Random placement of ships on the hidden board.
 - Players guesses coordinates to try and hit the ships.
 - Visual representation of both hidden board(with ships) and the guess board(tracking hits and misses).
 - Limited number of turns to guess all ships.


 ## How to play:
 1. Run the battleship.py file in a Python enviroment.
 2. Follow thee prompts to input your guesses in the format "(row column)". For exemple, to guess row 1, column 2, you would input "1 2".
 3. Continue guessing until you either sink all the ships or run out of turns.

 ## Rules:
 - The hidden board is a 3x3 grid, and there are 3 ships placed randomly on it.
 - Each turn, you input your guesses for a coordinate on the board.
 - If you guess hits a ship, it will be marked with an 'X' on you're guesse board.
 - If your guess misses, it will be marked with a '-' on your guess board.
 - You have a limited number of turns to sink all the ships.