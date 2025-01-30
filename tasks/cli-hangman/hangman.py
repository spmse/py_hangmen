import argparse
import random
from typing import List

def get_random_word() -> str:
    words = ['python', 'hangman', 'challenge', 'programming']
    return random.choice(words)


def display_word(word: str, guessed_letters: str) -> str:
    """
    Just to showcase this awesome feature

    Returns

        str: a string that follows the pattern '_ _ _ X _ _ Y _ Z'
    """

    result = ""

    for character in word:
        if character in guessed_letters:
            result += character
        else:
            result += "_"
        
    return result


def play_hangman(word):
    """
    This function will handle the hangman game loop and 
    connects all pieces of game logic.
    """
    pass


def main():
    parser = argparse.ArgumentParser(description="Play Hangman game")
    parser.add_argument('--word', type=str, help="Word to guess (optional)")
    args = parser.parse_args()

    pass

if __name__ == "__main__":
    main()