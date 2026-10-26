#!/usr/bin/env python3
prompt = "What you gotta say? : "
while True:
    text = input(prompt)
    if text == "STOP":
        break
    prompt = "I got that! Anything else? : "
