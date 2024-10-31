#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    A prototype that determine UTF-8 validation
    """
    number_bytes = 0

    byte_1 = 1 << 7
    byte_2 = 1 << 6

    for i in data:
        byte_remaining = 1 << 7

        if number_bytes == 0:
            while byte_remaining & i:
                number_bytes += 1
                byte_remaining = byte_remaining >> 1

                if number_bytes == 0:
                    continue

                if number_bytes == 1 or number_bytes > 4:
                    return False
        else:
            if not (i & byte_1 and not (i & byte_2)):
                return False
            number_byte -= 1

    if number_bytes == 0:
        return True

    return False
