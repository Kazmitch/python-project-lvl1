
"""Brain-even main program."""

import prompt
from random import randint


def welcome_user():
    """Greeting."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def question(name):
    """Check for correct answer"""
    counter = 0
    for i in range(0, 3):
        num = randint(0, 100)
        if num % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question: ' + str(num))
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            counter += 1
            print('Correct!')
            if counter == 3:
                print(f'Congratulations, {name}!')
                continue
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{right_answer}"')
            print(f"Let's try again, {name}")
            break


def main():
    """Main program"""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question(name)


if __name__ == '__main__':
    main()
