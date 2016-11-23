#!/usr/bin/env python3

'''Simple clock exercise'''


class Clock(object):
    '''Clock that handles times without dates'''

    def __init__(self, hours, minutes):
        self._time = minutes +hours *60
    
    def __str__(self):
        return '%02d:%02d' %(self._time //60 %24, self._time %60)

    def __eq__(self, other):
        return isinstance(other, Clock) and str(self) == str(other)

    def add(self, minutes):
        self._time += minutes
        return str(self)