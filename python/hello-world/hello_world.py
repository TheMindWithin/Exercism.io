"""Exercism.io's python "Hello World" exercise"""


# Python 2
def hello(name='World'):
    """Return a welcoming string"""   
    return 'Hello, %s!' %(name or 'World')


# Python 3
def hello(name='World'):
    """Return a welcoming string"""
    return f'Hello, {name or "World"}!'