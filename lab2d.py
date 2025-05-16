#!/usr/bin/env python3
'''Description: '''


# Name   : lab2d.py
# Author : Chung Yin Choi
# Date   : May 15, 2025

import sys

scriptname = sys.argv[0]

if len(sys.argv) != 3:
    print('Usage: ' + scriptname + ' name age')
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + str(age) + ' years old.')
