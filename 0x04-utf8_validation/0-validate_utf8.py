#!/usr/bin/python3
"""UTF-8 Validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """function to check validation"""
    try:
        count = 0
        for val in data:
            if count == 0:
                if val >> 5 == 0b110:
                    count = 1
                elif val >> 4 == 0b1110:
                    count = 2
                elif val >> 3 == 0b11110:
                    count = 3
                elif val >> 7 == 0b0:
                    count = 0
                else:
                    return False
            else:
                if val >> 6 != 0b10:
                    return False
                count -= 1

        return count == 0

    except UnicodeDecodeError:
        return False
