"""
From the exercise collection:
Exercise 3.4. Half-wave rectifier

In a half-wave rectifier the positive part of a signal
passes, while the negative part is blocked. Thus, for a
signal passing through a half-wave rectifier, the
negative values are set to zero. Let us look at a
sine signal that has passed through a half-wave rectifier:

f(x) = { sin x if x >  0
             0 if x <= 0

Implement f(x) as a Python function f(x) and make a test
function for testing the implementation of f(x) in both cases.
"""

from numpy import sin, pi

# f(x) as a python function
def half_wave_rectifier(x):

    f = sin(x)
    if f > 0:
        return f
    else:
        return 0


# test of f(x)
def test_half_wave_rectifier():
    """
    tests for the 2 cases of the f(x) function.
     x > 0, x <= 0

    checks if sin(pi/2) == 1, and if (-pi/2) gets set to 0
    """
    input = [(pi/2), (-pi/2)]
    computed = [half_wave_rectifier(i) for i in input]
    expected = [1, 0]

    assert computed == expected, "The test failed!"

test_half_wave_rectifier()

"""
OUTPUT:
No output, but i have manually tested the test function, and it works

"""
