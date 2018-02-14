from collections import deque
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

__author__ = 'Ali Hajimirza'
__email__ = 'ali@alihm.net'
__license__ = 'MIT'

"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be
resourceful, smart, and a quick thinker. It's not easy building a doomsday
device and capturing bunnies at the same time, after all! In order to make
sure that everyone working for her is sufficiently quick-witted, Commander
Lambda has installed new flooring outside the henchman dormitories. It looks
like a chessboard, and every morning and evening you have to solve a new
movement puzzle in order to cross the floor. That would be fine if you got to
be the rook or the queen, but instead, you have to be the knight. Worse, if you
take too much time solving the puzzle, you get "volunteered" as a test subject
for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called
answer(src, dest) which takes in two parameters: the source square, on which
you start, and the destination square, which is where you need to land to solve
the puzzle.  The function should return an integer representing the smallest
number of moves it will take for you to travel from the source square to the
destination square using a chess knight's moves (that is, two squares in any
direction immediately followed by one square perpendicular to that direction,
or vice versa, in an "L" shape).  Both the source and destination squares will
be an integer between 0 and 63, inclusive, and are numbered like the example
chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1

Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3
"""


def get_coordinates(value):
    """
    Given the value of a chess cell return the corresponding Point
    ----------
    value : int
        value of a cell between 0 and 63

    Returns
    -------
    node : tuple
        x and y coordinates

    Doc Test
    ----------
    >>> get_coordinates(0)
    Point(x=0, y=0)

    >>> get_coordinates(63)
    Point(x=7, y=7)

    >>> get_coordinates(37)
    Point(x=4, y=5)

    >>> get_coordinates(-1)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> get_coordinates(78)
    Traceback (most recent call last):
    ...
    AssertionError

    """
    assert (value >= 0 and value <= 63)
    return Point(value // 8, value % 8)


def is_valid_node(point):
    """
    Returns if a point belongs to on the chess board or not.
    ----------
    point : Point tuple
        Knight's position

    Returns
    -------
    is_valid : boolean
        If the point is on the chess board

    Doc Test
    ----------
    >>> is_valid_node(Point(0, 0))
    True

    >>> is_valid_node(Point(4, 5))
    True

    >>> is_valid_node(Point(8, 0))
    False

    >>> is_valid_node(Point(0, 10))
    False

    >>> is_valid_node(Point(-1, 0))
    False

    >>> is_valid_node(Point(8, -2))
    False
    """
    return (point.x >= 0 and point.x <= 7) and (point.y >= 0 and point.y <= 7)


def possible_moves(point):
    """
    Calculates the set of value knight moves
    ----------
    point : Point tuple
        Knight's position

    Returns
    -------
    moves : list of tuples
        Set of possible moves by knight

    Doc Test
    ----------
    >>> possible_moves(Point(0, 0))
    [Point(x=2, y=1), Point(x=1, y=2)]

    >>> possible_moves(Point(7, 7))
    [Point(x=5, y=6), Point(x=6, y=5)]

    >>> possible_moves(Point(4, 3))
    [Point(x=6, y=4), Point(x=6, y=2), Point(x=2, y=4), Point(x=2, y=2), Point(x=5, y=5), Point(x=5, y=1), Point(x=3, y=5), Point(x=3, y=1)]
    """

    moves = [
        Point(point.x + 2, point.y + 1), Point(point.x + 2, point.y - 1),
        Point(point.x - 2, point.y + 1), Point(point.x - 2, point.y - 1),
        Point(point.x + 1, point.y + 2), Point(point.x + 1, point.y - 2),
        Point(point.x - 1, point.y + 2), Point(point.x - 1, point.y - 2)
    ]

    return list(filter(is_valid_node, moves))


def answer(src, dest):
    """
    Calculates the minimum number of knight moves to get from src to dest
    ----------
    src : int
        Starting position

    dest : int
        Ending position

    Returns
    -------
    min_dist : int
        Minimum number of moves

    Doc Test
    ----------
    >>> answer(19, 36)
    1

    >>> answer(0, 1)
    3
    """
    src = get_coordinates(src)
    dest = get_coordinates(dest)

    min_dist = float('inf')
    visited = {}
    moves = deque()

    visited[src] = 0
    moves.append(src)

    while moves:
        current = moves.popleft()
        if current == dest:
            min_dist = min(min_dist, visited[current])

        for adjecent in possible_moves(current):
            if adjecent not in visited:
                visited[adjecent] = visited[current] + 1
                moves.append(adjecent)

    return min_dist


if __name__ == "__main__":
    import doctest
    doctest.testmod()
