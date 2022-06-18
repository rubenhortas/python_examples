from modules import module

if __name__ == '__main__':
    module.public_method()
    # In python nothing is really private
    # noinspection PyProtectedMember
    module._private_method()
