class Hero:
    """
    Name mangling is used for class attributes that one does not want subclasses to use which are designated as such
    by giving them a name with two or more leading underscores and no more than one trailing underscore

    Python"s runtime does not restrict access to such attributes, the mangling only prevents name collisions
    if a derived class defines an attribute with the same name.
    """
    __hero_name: str = None
    __real_name: str = None

    def __init__(self, hero_name: str, real_name: str):
        self.__hero_name = hero_name
        self.__real_name = real_name

    def print_name(self):
        print(f"I'm {self.__hero_name}!")

    def _print_real_name(self):
        print(f"PWNED! I'm {self.__real_name} :(")
