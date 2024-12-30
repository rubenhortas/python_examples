"""
Shunting yard algorithm: https://en.wikipedia.org/wiki/Shunting_yard_algorithm
"""

PRECEDENCES = {  # PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.
    '**': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}


def shunting_yard(expression: str) -> str:
    """
    Converts an expression from infix notation to Reverse Polish Notation (RPN).
    :param expression: '1 + 2 * 3 + (4 + 5 * 6)'
    :return: '1 2 3 * + 4 5 6 * + +'
    """
    expression = expression.strip().replace('(', '( ').replace(')', ' )').split()
    output_queue = []
    operator_stack = []

    for token in expression:
        if token == ' ':
            continue
        elif token in PRECEDENCES:
            while (operator_stack and operator_stack[-1] in PRECEDENCES and
                   PRECEDENCES[token] <= PRECEDENCES[operator_stack[-1]]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()
        else:
            output_queue.append(token)

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return ' '.join(output_queue)
