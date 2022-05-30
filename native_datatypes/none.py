# None is a null value
# Comparing None to anything other than None will always return False
# None is the only null value
# It has its own datatype (NoneType)
# You can assign None to any variable, but you can not create other NoneType objects

if __name__ == '__main__':
    var_none = None
    var_none2 = None

    print("None:")
    print(f"None == False -> {None == False}")  # False
    print(f"None == 0 -> {None == 0}")  # False
    print(f"None == '' -> {None == ''}")  # False
    print(f"None == var_none -> {None == var_none}")  # True
    print(f"var_none == var_none2 -> {var_none == var_none2}")  # True

    # In a boolean context None is False
    if not None:
        print("In a boolean context None is always False")
