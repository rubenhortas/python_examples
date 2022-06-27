from classes.namemangling.Hero import Hero

if __name__ == '__main__':
    batman = Hero('Batman', 'Bruce Wayne')
    batman.print_name()
    # noinspection PyProtectedMember,PyUnresolvedReferences
    batman._Hero__print_real_name()
