#!/usr/bin/env python3

# None is a null number
# Comparing None to anything other than None will always return False
# None is the only null number
# It has its own datatype (NoneType)
# You can assign None to any variable, but you can not create other NoneType objects

CTE_NONE1 = None
CTE_NONE2 = None

if __name__ == '__main__':
    print("None:")
    print(f"None == False -> {None == False}")  # False
    print(f"None == 0 -> {None == 0}")  # False
    print(f"None == '' -> {None == ''}")  # False
    print(f"None == var_none -> {None == CTE_NONE1}")  # True
    print(f"var_none == var_none2 -> {CTE_NONE1 == CTE_NONE2}")  # True

    # In a boolean context None is False
    if not None:
        print("In a boolean context None is always False")
