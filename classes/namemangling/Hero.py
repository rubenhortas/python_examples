class Hero:
    __hero_name = None
    __real_name = None

    def __init__(self, hero_name, real_name):
        self.__hero_name = hero_name
        self.__real_name = real_name

    def print_name(self):
        print(f'I\'m {self.__hero_name}!')

    # Class private methods starts with two underscores
    def __print_real_name(self):
        print(f'PWNED! I\'m {self.__real_name} :(')
