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


 ## Validator Testing 
  <ul>
   <li>Python</li>
    <ul><li>Using PEP8 no issues have been found</li></ul></ul>

    
 ## Bugs 
 - The code dosen't have any unsolved bugs.
 ### Solved Bugs
 - On the function that check the input from the player i had one bug with the max numbers for input.
 - On the 3x3 board i started the row and colum numbers from 1 to 3 but in the code i check if the input form the player is >= 3.
 <img src="readmeimg\Bug Python.png">

 ## Technology
  - Python to create the code.


 ## Deployment 


  ### GitHub
   
   <ul><li>We have deployd the Battleship to GuiHub.</li>
      <li>On the GitHub page head to settings.</li>
      <li>From drop-down menu head to Master Branch.</li>
      <li>After Master Branch was selected it will provide the link to game.</ul>