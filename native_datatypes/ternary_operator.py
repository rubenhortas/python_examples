#!/usr/bin/env python3

CONDITION = True
MESSAGE_TRUE = 'Condition is true'
MESSAGE_FALSE = 'Condition is false'

if __name__ == '__main__':
    # First way
    # if_condition_is_true if condition else if_condition_is_false
    result = MESSAGE_TRUE if CONDITION else MESSAGE_FALSE
    print(result)

    # Second way (Less intuitive, inmo)
    # (if_condition_is_false, if_condition_is_true)[condition]
    result = (MESSAGE_FALSE, MESSAGE_TRUE)[CONDITION]
    print(result)
