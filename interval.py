"""
This code defines the Interval class.
@Author:  Qiuyang Wang
@Date:  2023-3-12
"""


class Interval:
    def __init__(self, low, high):
        if low > high:                        # check if the input is valid
            raise Exception("invalid input")
        self.low = low
        self.high = high

    def __add__(self, other):
        return Interval(self.low + other.low, self.high + other.high)

    def __sub__(self, other):
        return Interval(self.low - other.high, self.high - other.low)

    def __mul__(self, other):
        return Interval(min(self.low * other.low, self.low * other.high, self.high * other.low, self.high * other.high),
                        max(self.low * other.low, self.low * other.high, self.high * other.low, self.high * other.high))

    def __truediv__(self, other):
        if other.low == 0 or other.high == 0:           # check if the input is valid
            raise Exception("interval division by zero")
        return Interval(min(self.low / other.low, self.low / other.high, self.high / other.low, self.high / other.high),
                        max(self.low / other.low, self.low / other.high, self.high / other.low, self.high / other.high))

    def union(self, other):
        return Interval(min(self.low, other.low), max(self.high, other.high))

    def intersect(self, other):
        return Interval(max(self.low, other.low), min(self.high, other.high))

    def intersects(self, other):
        return self.low <= other.high and other.low <= self.high

    def unions(self, other):
        return self.high >= other.low and other.high >= self.low

    def __str__(self):
        return f"[{self.low}, {self.high}]"
