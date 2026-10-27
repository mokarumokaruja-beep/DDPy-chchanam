#!/usr/bin/env python3
age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
for years in range(10, 31, 10):
    print(f"In {years} years, you'll be {age + years} years old.")
