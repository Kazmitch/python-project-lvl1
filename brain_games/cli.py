#!/usr/bin/env python3.8


"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """Greeting."""
    name = prompt.string('May I have your name? ')
    #print('Hello, {0}!'.format(name))
    
