import math


class Point:
    """ Custom Point class

    The Point class represents a point on a cartesian plane
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __add__(self, other):
        added_x = self.x + other.x
        added_y = self.y + other.y
        return Point(added_x, added_y)

    def __sub__(self, other):
        subbed_x = self.x - other.x
        subbed_y = self.y - other.y
        return Point(subbed_x, subbed_y)

    def distance(self, other):
        distance = math.sqrt((other.y - self.y)**2 + (other.x - self.x)**2)
        return distance

    def polar_angle(self, other):
        """Calculates the polar angle of the current Point with another"""
        if isinstance(other, Point):
            dy = other.y - self.y
            dx = other.x - self.x
            polar_angle = math.atan2(dy, dx)
            return polar_angle
        else:
            return Exception('Comparator object is not a Point!')

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Stack:
    """Custom Stack class

    The Stack class is a data structure where insertion of elements
    are the results of pushes, and removal of elements are from popping from the
    stack in a FIFO fashion. Supports peek of the top of the stack, but not random
    access into data structure
    """
    def __init__(self):
        self._stack = list()
        self._size = 0

    def push(self, element):
        self._stack.append(element)
        self._size += 1
        return True

    def pop(self):
        if self.is_empty():
            raise Exception('Attempting to pop from an empty stack!')
        self._size -= 1
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Attempting to peek from an empty stack!')
        return self._stack[-1]

    def peek_further(self):
        if self._size < 2:
            raise Exception('Attempting to peek from an empty or lone stack!')
        return self._stack[-2]

    def is_empty(self):
        if self._size != 0:
            return False
        return True

    def size(self):
        return self._size

    def __str__(self):
        return "[" + "".join(str(ele) for ele in self._stack) + "]"


def orientation(a, b, c) -> int:
    """Return an int

    Function determines the orientation of 3 ordered points

    Args:
        a: First ordered point
        b: Second ordered point
        c: Third ordered Point

    Returns:
        1: counter-clockwise
        0: collinear
        -1: clockwise
    """
    slope_diff = (b.y - a.y) * (c.x - b.x) / (b.x - a.x) * (c.y - b.y)
    if slope_diff > 0:
        return 1
    elif slope_diff < 0:
        return -1
    else:
        return 0
