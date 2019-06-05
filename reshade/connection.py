"""
The following classes are defined:
    Connection
"""


class Connection:
    def __init__(self, value=0):
        self._value = value
        self._callbacks = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value != self._value:
            self._value = value
            for callback in self._callbacks:
                callback()

    def bind_to(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)
