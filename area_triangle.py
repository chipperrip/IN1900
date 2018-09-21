"""
Exercise 3.16: Compute the area of an arbitrary triangle

An arbitrary triangle can be described by the coordinates of its three vertices:
(x1,y1), (x2,y2), (x3,y3) numbered in a counterclockwise direction. The area of
the triangle is given by the formula:

A = 1/2 |x2y3 - x3y2 - x1y3 + x3y1 - x1y2 - x2y1|
"""

from numpy import  abs

# function that calculates the area of a triangle. Takes a list of vertices as an argument.
def triangle_area(vertices):
    # get coordinates from vertices
    x1 = vertices [0][0]
    y1 = vertices [0][1]

    x2 = vertices [1][0]
    y2 = vertices [1][1]

    x3 = vertices [2][0]
    y3 = vertices [2][1]

    #compute area
    A = 0.5 * abs((x2*y3 - x3*y2 - x1*y3 + x3*y1 - x1*y2 - x2*y1))

    return A


# manually test triangle
v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
vertices = [v1, v2, v3]
print ()
print ('The result of triangle_area(vertices) with\nv1 = [0,0]; v2 = [1,0]; v3 = [0,2] as vertices:')
print ()
print (triangle_area(vertices))
print ()
# expected output: 1.0



#test function
def test_triangle_area():
    """
    Verify the area of a triangle with vertex
    (0,0), (1,0), and (0,2).
    """
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed area=%g != %g (expected)' %(computed, expected)
    assert success, msg

#perform test
test_triangle_area()

"""
OUTPUT:

The result of triangle_area(vertices) with
v1 = [0,0]; v2 = [1,0]; v3 = [0,2] as vertices:

1.0

"""
