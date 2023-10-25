#!/usr/bin/env python3
from collections import defaultdict

if __name__ == '__main__':
    user_count = defaultdict(int)
    user_count['root'] = 1
    user_count['admin'] = 4
    user_count['users'] = 2

    print(f"Number of roots: {user_count['root']}")  # 1
    print(f"Number of guests: {user_count['guests']}")  # 0

    # defaultdicts are very useful when we are using a table collection (e.g. a list) as value.
    # This way we don't need to initialize the keys before first use, and we will not get a KeyError.
    user_names = defaultdict(list)
    user_names['root'].append('ruben')
    user_names['admin'].append('ruben')
    user_names['admin'].append('ctrl')
    user_names['admin'].append('demonsito')
    user_names['admin'].append('kaian')
    user_names['users'].append('alice')
    user_names['users'].append('bob')

    print(f"Roots: {user_names['root']}")
    # return: ['ruben']

    print(f"Admins: {user_names['admin']}")
    # return: ['ruben', 'ctrl', 'demonsito', 'kaian']

    print(f"Users: {user_names['users']}")
    # return: ['alice', 'bob']
