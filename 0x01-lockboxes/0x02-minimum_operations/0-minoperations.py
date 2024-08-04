#!/usr/bin/python3
"""
This module contains a function that calculates the fewest number of operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n
    H characters in the file, given a number n.
    """
    no_of_operations = 0
    no_of_characters = 0
    operation = "COPY"

    if no_of_characters == n:
        return no_of_operations
    elif  no_of_characters > n:
        return 0
    # else:
    #     if step == "COPY":
            
    #     if step == "PASTE":
        
    #     op += 1
    #     minOperations(n)
