#!/usr/bin/env python3

"""
Reverse Polish Notation (RPN): https://en.wikipedia.org/wiki/Reverse_Polish_notation
"""

OPERATORS = ['**', '*', '/', '+', '-']


def rpn_to_infix(expression: str) -> str:
    """
    Converts an expression from Reverse Polish Notation (RPN) to infix.
    :param expression: '1 2 3 * + 4 5 6 * + +'
    :return: '((1+(2*3))+(4+(5*6)))'
    """
    output_queue = []

    for token in expression:
        if token == ' ':
            continue
        elif token in OPERATORS:
            b = output_queue.pop()
            a = output_queue.pop()
            output_queue.append(f"({a}{token}{b})")
        else:
            output_queue.append(token)

    return output_queue[0]
