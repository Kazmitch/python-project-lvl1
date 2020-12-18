
"""Brain-gcd main program."""

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
        first_num = randint(0, 100)
        second_num = randint(0, 100)
        expression = f'{first_num} {second_num}'
        print(f'Question: {expression}')
        answer = int(prompt.string('Your answer: '))

        while first_num != 0 and second_num != 0:
            if first_num > second_num:
                first_num %= second_num
            else:
                second_num %= first_num
        right_answer = first_num + second_num

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
    print('Find the greatest common divisor of given numbers.')
    question(name)


if __name__ == '__main__':
    main()
