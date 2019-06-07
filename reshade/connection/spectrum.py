"""
The following classes are defined:
    Spectrum
"""

from ..utils.validate import *
from .connection import Connection


class Spectrum:
    def __init__(self, *, connections=None, width=None):
        if connections is not None:
            self._connections = connections
        elif width is not None:
            self._connections = [Connection() for i in range(width)]
        else:
            raise TypeError("The width of the spectrum must be specified.")

    @property
    def connections(self):
        return self._connections

    @property
    def values(self):
        return [connection.value for connection in self._connections]

    @values.setter
    def values(self, values):
        validate_same_dimensions_spectrum(self._connections, values)

        for i in range(len(self._connections)):
            self._connections[i].value = values[i]

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self._connections[i]
                    for i in range(*key.indices(len(self._connections)))]
        if (key >= 0) and (key < len(self._connections)):
            return self._connections[key]
        else:
            raise IndexError("Spectrum width exceeded.")

    def __len__(self):
        return len(self._connections)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == len(self._connections):
            raise StopIteration

        self._index += 1
        return self._connections[self._index - 1]
