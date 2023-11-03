#!/usr/bin/env python3

DETECTIVES = ['Marlowe', 'Parker', 'Poirot', 'Carvalho']

if __name__ == '__main__':
    for detective in DETECTIVES:
        print(f"{detective}", end=',')
        # return: Marlowe,Parker,Poirot,Carvalho,

    print()

    for i in range(len(DETECTIVES)):
        print(f"{DETECTIVES[i]}", end=',')
        # return: Marlowe,Parker,Poirot,Carvalho,
