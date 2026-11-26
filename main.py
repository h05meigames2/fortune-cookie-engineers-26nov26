#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one original one-line fortune-cookie message for a software
engineer to /output/entry.txt (gate: UTF-8 text, 1-120 characters,
single line).
"""
import os

FORTUNE = "A stranger will review your code today. It is you, six months from now, and you are furious."

def main():
    assert "\n" not in FORTUNE and 1 <= len(FORTUNE) <= 120, "fortune must be one line, 1-120 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
