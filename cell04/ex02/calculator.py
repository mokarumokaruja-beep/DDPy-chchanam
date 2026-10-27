#!/usr/bin/env python3
first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
division = first / second
if division == int(division):
    division = int(division)
print(f"{first} / {second} = {division}")
print(f"{first} * {second} = {first * second}")
