#!/usr/bin/env python3

"""
Python allows to use the else condition with for and while loops.
The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
"""


def run_for_example(break_loop: bool) -> None:
    for i in range(10):
        print(i, end="")

        if i == 5 and break_loop:
            print(" <- The loop has been break!")
            break
    else:
        print(" <- The for loop has finished without breaking.")


def run_while_example(break_loop: bool) -> None:
    i = 0

    while i < 10:
        print(i, end="")

        if i == 5 and break_loop:
            print(" <- The loop has been break!")
            break

        i += 1
    else:
        print(" <- The while loop has finished without breaking.")


if __name__ == '__main__':
    run_for_example(True)
    # return: 012345 <- The loop has been break!

    run_for_example(False)
    # return: 0123456789 <- The for loop has finished without breaking.

    run_while_example(True)
    # return: 012345 <- The loop has been break!

    run_while_example(False)
    # return: 0123456789 <- The while loop has finished without breaking.
