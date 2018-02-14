__author__ = 'Ali Hajimirza'
__email__ = 'ali@alihm.net'
__license__ = 'MIT'

"""
En Route Salute
===============

Commander Lambda loves efficiency and hates anything that wastes time. She's a
busy lamb, after all! She generously rewards henchmen who identify sources of
inefficiency and come up with ways to remove them. You've spotted one such
source, and you think solving it will help you build the reputation you need to
get promoted.

Every time the Commander's employees pass each other in the hall, each of them
must stop and salute each other - one at a time - before resuming their path.
A salute is five seconds long, so each exchange of salutes takes a full ten
seconds (Commander Lambda's salute is a bit, er, involved).
You think that by removing the salute requirement, you could save several
collective hours of employee time per day. But first, you need to show her how
bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical
walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>',
an employee walking to the right; '<', an employee walking to the left;
and '-', an empty space. Every employee walks at the same speed either to right
or to the left, according to their direction. Whenever two employees cross,
each of them salutes the other. They then continue walking until they reach the
end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function answer(s) which takes a string representing employees walking
along a hallway and returns the number of times the employees will salute.
s will contain at least 1 and at most 100 characters, each one of -, >, or <.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) s = ">----<"
Output:
    (int) 2

Inputs:
    (string) s = "<<>><"
Output:
    (int) 4
"""


def answer(s):
    """
    Calculates the number of salutes in the hallway
    ----------
    s : string
        Hallway formation containing chars <,>,-

    Returns
    -------
    solute_count : int
        Number of salutes

    Doc Test
    ----------
    >>> answer('>----<')
    2

    >>> answer('<<>><')
    4

    >>> answer('--->-><-><-->-')
    10
    """
    solute_count = 0
    for i, c in enumerate(s):
        if c == '>':
            solute_count += s[i+1:].count('<')
    return solute_count * 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
