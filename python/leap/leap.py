#!/usr/bin/env python3

'''Leap year test exercise'''


def is_leap_year(year):
    '''Tests if the year is a leap year'''
    return year % 400 is 0 or year % 4 is 0 and not year % 100 is 0