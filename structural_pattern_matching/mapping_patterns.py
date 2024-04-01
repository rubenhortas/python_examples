#!/usr/bin/env python3

# Mapping pattern is a generalization of iterable unpacking to mappings.
# Its syntax is similar to dictionary display but each key and value are patterns "{" (pattern ":" pattern)+ "}".
# A **rest pattern is also allowed, to extract the remaining items.
# Only literal and constant value patterns are allowed in key positions.
# The subject must be an instance of collections.abc.Mapping.
# Extra keys in the subject are ignored even if **rest is not present.
# **_ is invalid in mapping patterns

def _pwn(user_info):
    match user_info:
        case {'SUDO': has_sudo, **rest}:
            print(f"PWN! sudo {has_sudo}: {rest}")
        case {'user_name': user_name}:
            print(f"Normal user: {user_name}")


if __name__ == '__main__':
    _pwn({'user_name': 'user', 'password': '12345'})
    # return: Normal user: user

    _pwn({'SUDO': True, 'user_name': 'sudouser', 'password': 'qwerty123', 'sudo_capabilities': 'ALL:ALL'})
    # return: PWN! sudo True: {'user_name': 'sudouser', 'password': 'qwerty123', 'sudo_capabilities': 'ALL:ALL'}
