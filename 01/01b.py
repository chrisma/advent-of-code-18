#!/usr/bin/env python3

# https://adventofcode.com/2018/day/1#part2

import os

def chronal_calibration(iterable):
    seen = []
    total = 0
    lst = list(iterable)
    i = 0
    while True:
        if total in seen:
            return total
        else:
            seen.append(total)
        total += int(lst[i%len(lst)])
        i += 1
        # print(total)

if __name__ == "__main__":
    assert chronal_calibration([+1, -1]) == 0
    assert chronal_calibration([+3, +3, +4, -2, -4]) == 10
    assert chronal_calibration([-6, +3, +8, +5, -6]) == 5
    assert chronal_calibration([+7, +7, -2, -7, -4]) == 14
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        print(chronal_calibration(f))
