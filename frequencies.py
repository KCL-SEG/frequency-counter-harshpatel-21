"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter

def frequencies(items):
    frequencies = {}
    for item in map(str,items):
        frequencies.setdefault(item,0)
        frequencies[item] += 1
    return frequencies
