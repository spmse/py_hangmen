# HANGMANPY

This folder contains the task definition for the hangman game as a practice task.
The task involves:

- a python program that allows for playing hangman
  - after a game is configured and started the user gets N tries to make character guesses - the goal of the game is to find the secret word

## Requirements

- word list is static in the beginning (-> fixed list of words that are guessable)
- program needs to be able to receive an argument/option to configure/overwrite the max retries for guessing
  - defaults to: 6
- requires a game loop that consists of the following steps:
  - retrieve a guess input from user
  - user input evaluation
  - while game != finished display current game state
    - game == finished: 
      - correct guess
      - max retries with wrong guesses exceeded
    - current game state:
      - amount of remaining guesses
      - result of last guess (correct/incorrect)
      - current findings/solution state
- launch a game => execute python script will lead to automatic word picking and start of the game loop

### Technical Details

- the program is written in Python 3.X
- the program uses the argparse module
- the max-retries config option should be named `--max-retries`
- the cli program is able to receive a word list from a file with the option `--wordlist`

### Challenge Details

- The project contains a README that can be followed to interact with the repo contents
- The documentation includes an example that illustrates how the static word list can be exchanged with dynamically generated word-lists.