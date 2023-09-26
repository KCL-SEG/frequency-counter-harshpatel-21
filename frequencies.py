"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter

def frequencies(items):
    return Counter(map(str,items))
