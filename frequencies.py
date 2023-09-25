"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter

def frequencies(items):
    frequencies = {}
    for item in items:
        frequencies.setdefault(str(item),0)
        frequencies[str(item)] += 1
    return frequencies
