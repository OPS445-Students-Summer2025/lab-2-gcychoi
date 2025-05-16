#!/usr/bin/env python3
'''Description: '''


# Name: lab2g.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/05/16

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')



