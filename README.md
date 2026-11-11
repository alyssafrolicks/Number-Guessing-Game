# Number-Guessing-Game
project page url: https://roadmap.sh/projects/number-guessing-game 
The project was done using VScode. Python code is done in the file guess_cli.py.

# Requirements
* When the game starts, it should display a welcome message along with the rules of the game.
* The computer should randomly select a number between 1 and 100.
* User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
* The user should be able to enter their guess.
* If the user's guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
* If the user's guess is incorrect, the game should display a message indicating whether the number is greater or less than the user's guess.
* The game should end when the user guesses the correct number or runs out of chances.
* Allows the user to play multiple rounds of the game until the user decides to quit.

# Sample Output of game
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
   
Enter your choice:
3

You have selected Hard difficulty level. You have 3 chances to guess the number.
Let's start the game!

Enter your guess: 
4

Incorrect! The number is greater than 4.

Enter your guess: 
5

Incorrect! The number is greater than 5.

Enter your guess: 
6

Incorrect! The number is greater than 6.

Game Over! You are out of guesses. The correct number was: 12

Do you want to play again? (yes/no)
