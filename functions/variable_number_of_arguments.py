#!/usr/bin/env python3

def _variable_number_of_arguments(arg1, arg2, *args) -> None:
    # Parameters will be a tuple
    print("Variable number of arguments")
    print(f"Mandatory parameters: {arg1}, {arg2}")
    print(f"Variable number of arguments: {args}")
    print()


def _variable_number_of_named_arguments(arg1, arg2, **args) -> None:
    # Parameters will be a dictionary
    print("Variable number of named arguments")
    print(f"Mandatory parameters: {arg1}, {arg2}")
    print(f"Variable number of named arguments: {args}")
    print()


if __name__ == '__main__':
    _variable_number_of_arguments('argument1', 'argument2', 'argument3', 'argument4')
    # return: Variable number of arguments
    #           Mandatory parameters: argument1, argument2
    #           Variable number of arguments: ('argument3', 'argument4')

    _variable_number_of_named_arguments('argument1', 'argument2', arg3='argument3', arg4='argument4')
    # return: Variable number of named arguments
    #           Mandatory parameters: argument1, argument2
    #           Variable number of named arguments: {'arg3': 'argument3', 'arg4': 'argument4'}
