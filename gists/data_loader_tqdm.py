#!/usr/bin/env python3

from tqdm import tqdm
from time import sleep

if __name__ == '__main__':

    data = list(range(100))

    for i in tqdm(data):
        sleep(0.1)
