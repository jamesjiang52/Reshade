"""
The following classes are defined:
    Image
"""

from ..utils.validate import *
from .connection import Connection


class Image:
    def __init__(self, *, connections=None, height=None, width=None):
        if connections is not None:
            validate_dimensions_image(connections)
            self._connections = connections
        elif height is not None and width is not None:
            self._connections = [[Connection()
                                 for j in range(width)]
                                 for i in range(height)]
        else:  # only one of height or width was provided
            raise TypeError(
                "The height and width of the image must be specified."
            )

    @property
    def connections(self):
        return self._connections

    @property
    def values(self):
        return [[connection.value for connection in row]
                for row in self._connections]

    @values.setter
    def values(self, values):
        validate_dimensions_image(values)
        validate_same_dimensions_image(self._connections, values)

        for i in range(len(self._connections)):
            for j in range(len(self._connections[i])):
                self._connections[i][j].value = values[i][j]

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self._connections[i]
                    for i in range(*key.indices(len(self._connections)))]
        if (key >= 0) and (key < len(self._connections)):
            return self._connections[key]
        else:
            raise IndexError("Image height exceeded.")

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
