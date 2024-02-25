# Battleship Game


## Introduction
 - Battleship is a classic game where players try to sink each other's ships on a grid. This Python implementation allows you to play agains the computer, trying to sink its hidden ships before runing out of turns.


## Futures 
 - Random placement of ships on the hidden board.
 - Players guesses coordinates to try and hit the ships.
 - Visual representation of both hidden board(with ships) and the guess board(tracking hits and misses).
 - Limited number of turns to guess all ships.

 ### Future futures
  - I will like to add more ships on the game.
  - Extend the board.
  - Missed location to be marked as '-'.


 ## How to play:
 1. Run the battleship.py file in a Python enviroment.
 2. Follow thee prompts to input your guesses in the format "(row column)". For exemple, to guess row 1, column 2, you would input "1 2".
 3. Continue guessing until you either sink all the ships or run out of turns.

 ## Rules:
 - The hidden board is a 3x3 grid, and there are 3 ships placed randomly on it.
 - Each turn, you input your guesses for a coordinate on the board.
 - If you guess hits a ship, it will be marked with an 'X' on you're guesse board.
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
 <img src="readmeimg\bugpython.png">

 ## Technology
  - Python to create the code.
  - Heroku to test the code.


 ## Deployment 


  ### GitHub
   
   - We have deployd the Battleship to GitHub.
      

   ### Heroku


   - This project was deployed using Code Institute mock terminal for Heroku.
   <ul><li>Steps for deployment:</li>
      <ul><li>Fork or clone this repository</li>
      <li>Create a new Heroku app</li>
      <li>Set the buildbacks to Python and NodeJS in that order</li>
      <li>Link the Heroku app to the repository</li>
      <li>Click on Deploy</li></ul>

   


### Flow Chart

 - We have also created a flow chart for this code.
 <img src=readmeimg\flowchart.png>

 

 ### Visual Studio Code
 - In Visual Studio Code we have write the code for the game.

 ### Overview of the game 
 <img src=readmeimg\overview.png>


### Credits
- Code Institute for the deployment terminal

