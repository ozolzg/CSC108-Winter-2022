"""
Q3: Writing a Function
3 marks

Write the code for the following function.
"""


def no_dups(s: str) -> str:
    '''
    Return a new version of s, but with each sequence of repeated characters
    replaced by a single character.

    >>> no_dups('aaaddc')
    'adc'
    >>> no_dups('aaaabbcaa')
    'abca'
    >>> no_dups('abc')
    'abc'
    '''

    result = list()
    s_list = list(s)

    while s_list:
        character = s_list.pop(0)
        if not result or result[-1] != character:
            result.append(character)

    return "".join(result)






