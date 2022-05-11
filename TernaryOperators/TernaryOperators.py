#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

if __name__ == "__main__":
    condition = True
    condition_true = "Condition is true"
    condition_false = "Condition is false"

    # First way
    result = condition_true if condition else condition_false
    print(result)

    # Second way (Less intuitive, inmo)
    # (if_condition_is_false, if_condition_is_true)[condition]
    result = (condition_false, condition_true)[condition]
    print(result)
