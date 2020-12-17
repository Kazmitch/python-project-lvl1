
"""Brain-even main program."""

import prompt
from random import randint
from random import choice


def welcome_user():
    """Greeting."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def question(name):
    """Check for correct answer"""
    counter = 0
    for i in range(0, 3):
        first_num = randint(0, 100)
        second_num = randint(0, 100)
        operator = choice(['+', '-', '*'])
        expression = f'{first_num} {operator} {second_num}'
        right_answer = eval(expression)
        print('Question: ' + expression)
        answer = int(prompt.string('Your answer: '))
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
    print('What is the result of the expression?')
    question(name)


if __name__ == '__main__':
    main()
