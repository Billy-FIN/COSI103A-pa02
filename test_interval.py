'''
test_interval runs a few tests on the interval methods
Will test for exceptions and for correct results
'''

from interval import Interval
import pytest


def test_init():
    ''' constructor should create a printable object '''
    x = Interval(4, 5)
    expected = '[4, 5]'
    assert str(x) == expected
    with pytest.raises(Exception):
        x = Interval(5, 4)


def test_add():
    x1 = Interval(4, 5)
    x2 = Interval(2.2, 3.3)
    expected = '[6.2, 8.3]'
    assert str(x1+x2) == expected


def test_mul():
    x1 = Interval(4, 5)
    x2 = Interval(2.2, 3.3)
    expected = '[8.8, 16.5]'
    assert str(x1*x2) == expected


def test_div():
    x1 = Interval(4, 8)
    x2 = Interval(2, 16)
    x3 = Interval(0, 3.3)
    x4 = Interval(-3.3, 0)
    with pytest.raises(Exception):
        x = x1/x3
    with pytest.raises(Exception):
        x = x1/x4
    expected = '[0.25, 4.0]'
    assert str(x2/x1) == expected


def test_sub():
    x1 = Interval(4, 5)
    x2 = Interval(2.2, 3)
    expected = '[1, 2.8]'
    assert str(x1-x2) == expected


def test_union():
    x1 = Interval(4, 5)
    x2 = Interval(2.2, 3.3)
    x3 = Interval(6, 7)
    expected = '[2.2, 5]'
    assert str(x1.union(x2)) == expected
    assert x1.unions(x3) == False


def test_intersction():
    x1 = Interval(3, 5)
    x2 = Interval(2.2, 3.3)
    x3 = Interval(6, 7)
    expected = '[3, 3.3]'
    assert str(x1.intersect(x2)) == expected
    assert x1.intersects(x3) == False
