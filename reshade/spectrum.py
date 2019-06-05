"""
The following classes are defined:
	Spectrum
"""

from .connection import Connection


class Spectrum:
    def __init__(self, *, connections=None, height=None):
        if connections is not None:
            self._connections = connections
        elif height is not None:
            self._connections = [Connection() for i in range(height)]
        else:
            raise TypeError("The height of the spectrum must be specified.")

    @property
    def connections(self):
        return self._connections

    @property
    def values(self):
        return [connection.value for connection in self._connections]

    @values.setter
    def values(self, values):
        if len(values) != len(self._connections):
            raise TypeError(
                "Expected {0} arguments, received {1}.".format(
                    len(self._connections),
                    len(values)
                )
            )

        for i in range(len(self._connections)):
            self._connections[i].value = values[i]

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self._connections[i]
                    for i in range(*key.indices(len(self._connections)))]
        if (key >= 0) and (key < len(self._connections)):
            return self._wires[key]
        else:
            raise IndexError("Spectrum height exceeded.")

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
