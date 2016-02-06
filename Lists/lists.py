#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        Lists.py
@interpreter: python3
"""

if __name__ == '__main__':
    l = []

    # Adding items
    l = l + ['a']
    l.append(1)  # In a list items don't need to be the same type
    l.extend(['b', 2])
    l.insert(0, True)

    print("List: ", l)

    # Searching for values
    print("Searching for values")
    if 'a' in l:
        print("\tThe value is in the list")

    l.append('a')
    print("\tList: ", list)
    position = l.index('a')  # Returns the position of the first occurrence
    print("\tposition: %d" % position)

    try:
        # Negative index are valid, so raises an exception if the item is not
        # found
        print("\tItem in -1 position: %s" % l[-1])
        position = l.index(False)
    except:
        print("\tItem not found")

    # Popping
    print("Popping")
    print("\t", l)
    l.pop()
    print("\t", l)
