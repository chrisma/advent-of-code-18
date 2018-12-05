#!/usr/bin/env python3

# https://adventofcode.com/2018/day/1

import os

def chronal_calibration(iterable):
    return sum((int(line) for line in f))

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        print(chronal_calibration(f))
