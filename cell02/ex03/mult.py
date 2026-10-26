#!/usr/bin/env python3
print("Enter the first number:")
first = int(input())
print("Enter the second number:")
second = int(input())
result = first * second
print(first, "x", second, "=", result)
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
