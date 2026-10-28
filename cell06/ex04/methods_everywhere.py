#!/usr/bin/env python3
import sys


def shrink(text):
    print(text[:8])


def enlarge(text):
    while len(text) < 8:
        text = text + "Z"
    print(text)


params = sys.argv[1:]
if len(params) < 1:
    print("none")
else:
    for param in params:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)
