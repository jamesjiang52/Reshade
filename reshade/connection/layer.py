"""
The following classes are defined:
    ConnectionLayer
"""

from ..utils.validate import *
from .connection import Connection


class ConnectionLayer:
    def __init__(
        self, connections=None,
        *,
        depth=None,
        height=None,
        width=None
    ):
        if connections is not None:
            validate_dimensions_layer(connections)
            self._connections = connections
        elif height is not None and width is not None and depth is not None:
            self._connections = [[[Connection()
                                 for k in range(width)]
                                 for j in range(height)]
                                 for i in range(depth)]
        else:  # not all of depth, height, or width were provided
            raise TypeError(
                "The depth, height, and width of the layer must be specified."
            )

    @property
    def connections(self):
        return self._connections

    @property
    def values(self):
        return [[[connection.value for connection in row]
                for row in depth_slice]
                for depth_slice in self._connections]

    @values.setter
    def values(self, values):
        validate_dimensions_layer(values)
        validate_same_dimensions_layer(self._connections, values)

        for i in range(len(self._connections)):
            for j in range(len(self._connections[i])):
                for k in range(len(self._connections[i][j])):
                    self._connections[i][j][k].value = values[i][j][k]

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self._connections[i]
                    for i in range(*key.indices(len(self._connections)))]
        if (key >= 0) and (key < len(self._connections)):
            return self._connections[key]
        else:
            raise IndexError("Layer depth exceeded.")

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
