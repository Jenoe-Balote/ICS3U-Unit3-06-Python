#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program is the better "Number Guessing Game"

import random
import string
random_number = random.randint(0, 9)


def main():
    # this function runs the better "Number Guessing Game"

    # input
    number_guessed = str(input("Enter a number between 0 - 9: "))
    print("")

    # process and output
    try:
        number_guessed = int(number_guessed)
        if number_guessed == random_number:
            print("You guessed correctly!")
        else:
            print("Incorrect, the number was {}.".format(random_number))
    except Exception:
        print("That is not a number at all!")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
