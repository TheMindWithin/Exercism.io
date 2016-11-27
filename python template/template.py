#!/usr/bin/env python

'''Python template file for examples of good use of code and convention.

PEP 8 -- Style Guide: https://www.python.org/dev/peps/pep-0008/
PEP 8 -- Style Guide Checker: https://pypi.python.org/pypi/pep8
Flyke8 Style Guide Checker: http://flake8.readthedocs.io/en/latest/

Author: Julius Mayer (jmayer@uos.de)
'''

# File names: Modules should have short, all-lowercase names. Underscores can be
#             used in the module name if it improves readability. 
# No encoding declaration. (-*- coding: utf-8 -*-) if UTF-8 or ASCII is used
# Limit all lines to a maximum of 80 characters.


################################################################################
##########################          Imports          ###########################
################################################################################

# Imports are always put at the top of the file, just after any module comments 
# and docstrings, and before module globals and constants and should usually be 
# on separate lines. Wildcard imports ( from <module> import * ) should be 
# avoided

# standard library imports
import os
import logging
import ConfigParser #python3: import configparser
import argparse
import warnings
import exception
import timeit
import time
import threading
import numpy as np
from abc import ABCMeta, abstractmethod

# related third party imports
from matplotlib.image import imread
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# local application/library specific imports
from resources.null import Null


################################################################################
##########          Argument parser, config parser & logging          ##########
################################################################################

# Argument parser
parser = argparse.ArgumentParser(description='Descrition here.')
parser.add_argument(
    "-r", 
    "--repetitions", 
    type   =int,
    default=1,
    nargs  ="*", 
    help   ="number of experiment repetitions"
)
parser_args = parser.parse_args()

# Config parser
config = ConfigParser.ConfigParser()
config.readfp(open('defaults.cfg'))
config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])

# Logging configuration
logging.basicConfig(
    filename='log.log', 
    filemode='w', 
    level   =logging.DEBUG, # Everything from debug to critical is logged
    format  ='%(asctime)s - %(name)s - %(module)s - %(levelname)s: '\
             '[%(lineno)d] %(message)s'
)
logger = logging.getLogger(__name__)


################################################################################
######################          ExampleClassName          ######################
################################################################################

# Class names: should normally use the CapWords convention. (CamelCase)

class ExampleClass(object):
    '''A simple example class with a name property and a setter function'''
    
    def __init__(self, name='Usr'):
        self.name = name

    def __str__(self):          # “informal” string representation of the object
        return self.name

    def __repr__(self):         # “official” string representation of the object
        return __str__

    @property
    def name(self):
        return self._name       # use _ for 'private' variables

    @name.setter
    def name(self, name):
        self._name = 'the incredible %s' %name
        logger.info('Changed name to %s' %self._name)


################################################################################
##################          AbstractExampleClassName          ##################
################################################################################

class AbstractExampleClass(object):
    '''Definition docstring'''

    __metaclass__ = ABCMeta

    @abstractmethod
    def abstract_example_method(self):
        raise NotImplementedError()


################################################################################
##################          DerivedExampleClassName          ###################
################################################################################

class DerivedExampleClass(AbstractExampleClass):
    '''Definition docstring'''

    @classmethod
    def abstract_example_method(self):
        pass


################################################################################
#########################          Threading          ##########################
################################################################################

class MyThread(threading.Thread):
    '''Definition docstring'''

    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

    def run(self):
        while not self.stopped():
            print("Looping around here with")
            time.sleep(3)
            pass

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

################################################################################
#########################          Functions          ##########################
################################################################################

# Function names: should be lowercase, with words separated by underscores as 
#                 necessary to improve readability.

# No spaces when indicating keyword arguments or a default parameter values.
def hello(name='World'): 
    '''Returns a welcoming string'''
    return 'Hello, %s!' %(name or "World")

def img2array(path, name):
    '''Nom nom nom, me like tasty images.'''
    return np.array(img.append(imread('%s/%s.png' %(path, name))))


################################################################################
########################          Program body          ########################
################################################################################

my_class = ExampleClass('Your name')
print(hello(my_class))
print(timeit.timeit("test()", setup="from __main__ import hello"))

################################################################################
############################          Main          ############################
################################################################################

if __name__ == '__main__':

    n = raw_input("Hit enter to start.")


################################################################################
#######################          Initialisation          #######################
################################################################################

    img = img2array('resources', 'img')
    data = pd.read_csv('resources/TitanicPassengers.csv')

################################################################################
#########################          Evaluation          #########################
################################################################################