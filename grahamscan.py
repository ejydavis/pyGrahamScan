from supportlib import Point, orientation, Stack
from collections import OrderedDict


class GrahamScan:
    """The Graham-Scan algorithm forms a convex hull from a finite collection of points

    Note:
        The algorithm works as follows,
        1) Find the Point (s) with the least y-coordinate
        2) Sort all the Points by the polar angle they make with (s)
        3) Init a Stack, stack points by orientation in counter-clockwise direction

    Args:
        points: a collection of points to form a convex hull
    """

    def __init__(self, points):
        self._points = points
        self.new_points(points)

    def new_points(self, points):
        self._points = points
        self._least_point()
        self._calculate_polars()
        self._calculate_hull()

    def _least_point(self):
        """Finds the point with the least y-value in the cartesian plane"""
        self._least = min(self._points, key=lambda obj: obj.y)

    def _calculate_polars(self):
        """Calculate and sort points by polar angle with least point"""
        polar_angles = {}
        for point in self._points:
            polar_angle = self._least.polar_angle(point)
            polar_angles[polar_angle] = point
        sorted_angles = OrderedDict(sorted(polar_angles.items(), key=lambda k: k[0]))
        self._sorted_angle_array = [angle for angle in sorted_angles.values()]

    def _calculate_hull(self):
        """Calculate the convex hull by pushing onto a Stack in order of counter-clockwise direction"""
        angles = self._sorted_angle_array
        num_angles = len(angles)
        st = Stack()
        if num_angles < 3:
            raise Exception("Not enough points to form a convex hull")
        for i in range(0, 3):
            st.push(angles[i])
        for i in range(3, num_angles):
            while orientation(
                st.peek_further(),
                st.peek(),
                angles[i]
            ) <= 0:
                _ = st.pop()
            st.push(angles[i])
        self._hull = st

    def hull(self):
        return self._hull
