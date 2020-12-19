
"""Brain-prime main program."""

import prompt
from random import randint
# from math import sqrt


def welcome_user():
    """Greeting."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def question(name):
    """Check for correct answer"""
    counter = 0
    for i in range(0, 3):
        n = randint(0, 2)
        print(f'Question: {n}')
        answer = prompt.string('Your answer: ')

        if n == 1:
            right_answer = 'no'
        else:
            d = 2
            while n % d != 0:
                d += 1
            if d == n:
                right_answer = 'yes'
            else:
                right_answer = 'no'

        if answer == right_answer:
            counter += 1
            print('Correct!')
            if counter == 3:
                print(f'Congratulations, {name}!')
                continue
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break


def main():
    """Main program"""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question(name)


if __name__ == '__main__':
    main()
