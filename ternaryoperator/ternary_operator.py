#!/usr/bin/python3

if __name__ == '__main__':
    condition = True
    message_condition_true = "Condition is true"
    message_condition_false = "Condition is false"

    # First way
    result = message_condition_true if condition else message_condition_false
    print(result)

    # Second way (Less intuitive, inmo)
    # (if_condition_is_false, if_condition_is_true)[condition]
    result = (message_condition_false, message_condition_true)[condition]
    print(result)
