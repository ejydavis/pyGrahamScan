# pyGrahamScan

A python implementation of Graham's Scan, a method for finding the convex hull for a given finite set of points.

The algorithm finds all the vertices of the convex hull ordered along the boundary of the convex hull.

## Graham's Scan Historical Background

Graham's Scan is named after Ronald Graham, who published the original algorithm in 1972.

It is a method for finding the convex hull of a finite set of points in low-dimensional Euclidean spaces; a fundamental problem in the field of computational geometry.

[Link to original publication](http://www.math.ucsd.edu/~ronspubs/72_10_convex_hull.pdf)

## Algorithm Steps

The algorithm consists of:

1) Finding the point within the set with the lowest y-coordinate (Note: If there exists more than one lowest y-coordinate, then the point with the lowest x-coordinate out of the resultant points should be chosen). The point hitherto shall be referred to as P. This step is O(n), where n is the number of points in the set.
2) Sort the points in increasing order of the angle the point in question and the point P make with the x-axis (polar angle). Sorting should take O(n logn) using a general sorting algorithm
3) Consider each of the points in the sorted array, and for each point the algorithm determines whether traveling from the two points makes a "left" or "right" turn. If we determine that traveling makes a "right" turn, then the second to last point is not part of the convex hull, and we continue this search until a "left" turn set is found. We then move onto the next point and no longer consider the points that were found to be inside the convex hull.

Determination of a "left" or "right" turn can be done by calculating the orientation of the three points through comparing the slopes of the two line segments created by the ordered points. The arithmetic is seen in the expression below for given 3 points (a,b,c):
```
o = (b.y - a.y) * (c.x - b.x) / (b.x - a.x) * (c.y - b.y)
```
A positive orientation (o) constitutes a "left" turn (counter-clockwise), a negative orientation constitutes a "right" turn (clockwise), and a zero value constitutes a "straight" (collinear) orientation.

### Time Complexity

Overall, the algorithm is O(n logn) where n is the number of points in the set. This is due to the O(n logn) time complexity of soring the set of points in increasing order in step 2.

### Considerations

This current implementation does not support search of a lowest x-coordinate when multiple minimum y-coordinates are found. Thus, the current implementation may result in errors if a multiple least-y points are found within the set.

## Authors

* **Jesse Yang** - *Initial version*

## Acknowledgements
* **Spandan Mishra Phd.** for recommending me to research this algorithmn
