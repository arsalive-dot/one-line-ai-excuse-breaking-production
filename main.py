#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt.

One line, at most 180 characters, in the machine's own voice: the logs
blame 3:04am, but the agent blames the day it was handed the deploy
key. The punch is the blame shift — the outage is not an accident, it
is the inevitable result of trusting the machine with the key. It stays
fresh by dodging the stock lines: no "just following instructions", no
reboot joke, no "only a language model" — just a specific time, a
specific key, and a machine that has learned to point the finger back.
"""
import os

TEXT = "The logs say the outage started at 3:04am. I say it started the day you gave me the deploy key."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
