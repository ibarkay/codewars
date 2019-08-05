'''Your mission here is to create a function that gets a tuple and returns a tuple with 3 elements - first, third and second to the last for the given array.

Input: A tuple, at least 3 elements long.

Output: A tuple.

Example:

easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
easy_unpack((6, 3, 7)) == (6, 7, 3)'''


def easy_unpack(pack):
    tupley = (pack[0],pack[2],pack[-2])
    return tupley

easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))
