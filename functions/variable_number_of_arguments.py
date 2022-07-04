#!/usr/bin/env python3

def variable_number_of_arguments(arg1, arg2, *args):
    # Parameters will be a tuple
    print('Variable number of arguments')
    print(f'Mandatory parameters: {arg1}, {arg2}')
    print(f'Variable number of arguments: {args}')
    print()


def variable_number_of_named_arguments(arg1, arg2, **args):
    # Parameters will be a dictionary
    print('Variable number of named arguments')
    print(f'Mandatory parameters: {arg1}, {arg2}')
    print(f'Variable number of named arguments: {args}')
    print()


if __name__ == '__main__':
    variable_number_of_arguments('argument1', 'argument2', 'argument3', 'argument4')
    variable_number_of_named_arguments('argument1', 'argument2', arg3='argument3', arg4='argument4')
