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
    usernames = defaultdict(list)
    usernames['root'].append('trazi')
    usernames['admin'].append('trazi')
    usernames['admin'].append('ctrl')
    usernames['admin'].append('demonsito')
    usernames['admin'].append('kaian')
    usernames['users'].append('alice')
    usernames['users'].append('bob')

    print(f"Roots: {usernames['root']}")
    # return: Roots: ['trazi']

    print(f"Admins: {usernames['admin']}")
    # return: Admins: ['trazi', 'ctrl', 'demonsito', 'kaian']

    print(f"Users: {usernames['users']}")
    # return: Users: ['alice', 'bob']

    print(f"Users: {usernames['ftp']}")
    # return: Users: []
