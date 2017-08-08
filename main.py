import sys
import numpy as np

def character_to_index(c: str) -> int:
    index = ord(c) - 97
    if -1 < index < 26:
        index = index
    else:
        index = 26
    return index


def parse_file(filename: str) -> list:
    results = [[0 for i in range(27)] for j in range(27)]
    with open(filename) as f:
        for line in f:
            line = line.lower()
            prev = -1
            for letter in line:
                index = character_to_index(letter)
                if prev > -1:
                    results[prev][index] += 1
                prev = index
    return results

if len(sys.argv) < 2:
    print("Usage: main.py filename")
else:
    print(np.matrix(parse_file(sys.argv[1])))