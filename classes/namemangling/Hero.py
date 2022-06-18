class Hero:
    hero_name = None
    real_name = None

    def __init__(self, hero_name, real_name):
        self.hero_name = hero_name
        self.real_name = real_name

    def print_name(self):
        print(f'I\'m {self.hero_name}!')

    # Class privates starts with two underscores
    def __print_real_name(self):
        print(f'PWNED! I\'m {self.real_name} :(')
