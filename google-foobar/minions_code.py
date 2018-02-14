__author__ = 'Ali Hajimirza'
__email__ = 'ali@alihm.net'
__license__ = 'MIT'

ascii_a = ord('a')
ascii_z = ord('z')


def transform(c):
    """
    Transforms letters [a...z] to [z...a], return the same char if is not in [a...z]
    ----------
    c : char
        Ciphered text

    Returns
    -------
    res : char
        Transformed char

    Doc Test
    ----------
    >>> transform('a')
    'z'

    >>> transform('b')
    'y'

    >>> transform('z')
    'a'

    >>> transform('4')
    '4'

    >>> transform('?')
    '?'

    >>> transform('.')
    '.'

    >>> transform("'")
    "'"

    """
    ascii_val = ord(c)
    if ascii_val < ascii_a or ascii_val > ascii_z:
        return c

    return chr(ascii_a + ascii_z - ascii_val)


def answer(s):
    """
    Deciphers minions code
    ----------
    s : string
        Ciphered text

    Returns
    -------
    res : string
        Deciphered text

    Doc Test
    ----------
    >>> answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
    "did you see last night's episode?"

    >>> answer("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
    "Yeah! I can't believe Lance lost his job at the colony!!"
    """
    return ''.join(map(transform, s))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
