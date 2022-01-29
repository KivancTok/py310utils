from functools import lru_cache


class Frac:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.result = self.numerator / self.denominator

    def __add__(self, other):
        if other.denominator != self.denominator:
            s_denominator = self.denominator
            self.numerator *= other.denominator
            self.denominator *= other.denominator
            other.numerator *= s_denominator
            other.denominator *= s_denominator

        return (self.numerator + other.numerator) / self.denominator

    def __sub__(self, other):
        if other.denominator != self.denominator:
            s_denominator = self.denominator
            self.numerator *= other.denominator
            self.denominator *= other.denominator
            other.numerator *= s_denominator
            other.denominator *= s_denominator

        return (self.numerator - other.numerator) / self.denominator

    def __mul__(self, other):
        return (self.numerator * other.numerator) / (self.denominator * other.denominator)

    def __truediv__(self, other):
        return ((self.numerator / other.numerator) / (self.denominator / other.numerator)) / ((other.numerator / self.numerator) / (other.denominator / self.numerator))

    def __eq__(self, other):
        return self.result == other.result

    def __ne__(self, other):
        return self.result != other.result

    def __lt__(self, other):
        return self.result < other.result

    def __gt__(self, other):
        return self.result > other.result

    def __le__(self, other):
        return self.result <= other.result

    def __ge__(self, other):
        return self.result >= other.result

    def __hash__(self):
        return hash(self.result)


@lru_cache
def fib(n):
    if n <= 1:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)
