#!/usr/bin/env python3

import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    print(sum((int(line) for line in f)))
