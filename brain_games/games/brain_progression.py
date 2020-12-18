
"""Brain-progression main program."""

import prompt
from random import randint


def welcome_user():
    """Greeting."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def question(name):
    """Check for correct answer"""
    counter = 0
    for i in range(0, 3):
        progression = randint(1, 100)
        step = randint(2, 10)
        quantity_of_progression = randint(5, 10)
        i = randint(0, quantity_of_progression - 1)
        c = []
        for n in range(1, quantity_of_progression + 1):
            c.append(progression)
            progression += step

        right_answer = c[i]
        c[i] = '..'

        str_progression = ' '.join(map(str, c))
        print(f'Question: {str_progression}')

        answer = int(prompt.string('Your answer: '))
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
    print('What number is missing in the progression?')
    question(name)


if __name__ == '__main__':
    main()
