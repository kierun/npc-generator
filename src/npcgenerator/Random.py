# -*- coding: utf-8 -*-
"""A random generator."""
from random import randrange
import codecs


class Random(object):
    """Holds some data that can be randomly accessed."""

    def __init__(self, data=None):
        """Initiator.

        :type data: String / List
        :param data: The path to the file or a list containing the data.
        """
        self._data = []
        if isinstance(data, str):
            with codecs.open(data, 'r', 'utf-8') as fd:
                self._data = fd.read().splitlines()
        elif isinstance(data, list):
            self._data = data
        else:
            raise RuntimeError("Could not generate data from '%s'" % (data))
        self._size = len(self._data)

    def get_a_value(self):
        """Returns a random element from the data."""
        return self._data[randrange(0, self._size)]
