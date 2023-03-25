#!/usr/bin/env python3

# Python allows us to use the else condition with for and while loops.
# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

def run_for_example():
    for i in range(9):
        print(i)
        # break
    else:
        print("The for loop has finished without breaking")


def run_while_example():
    i = 0

    while i < 10:
        print(i)
        i += 1
        # break
    else:
        print("The while loop has finished without breaking")


if __name__ == '__main__':
    # run_for_example()
    run_while_example()
