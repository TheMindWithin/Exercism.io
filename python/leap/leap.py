"""Exercism.io's python "Leap" exercise"""


def is_leap_year(year):
    """Test if the year is a leap year"""
    return year % 400 is 0 or year % 4 is 0 and not year % 100 is 0