#!/usr/bin/env python3
original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for number in original:
    if number > 5:
        new.append(number + 2)
print(original)
print(set(new))
