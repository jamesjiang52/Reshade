"""
The following classes are defined:
    ConnectionLayer
"""

from ..utils.validate import *
from .connection import Connection
from .image import Image


class ConnectionLayer:
    def __init__(
        self, images=None,
        *,
        depth=None,
        height=None,
        width=None
    ):
        if images is not None:
            validate_dimensions_layer(images)
            self._images = images
        elif height is not None and width is not None and depth is not None:
            self._images = [
                Image(height=height, width=width) for i in range(depth)
            ]
        else:  # not all of depth, height, or width were provided
            raise TypeError(
                "The depth, height, and width of the layer must be specified."
            )

    @property
    def images(self):
        return self._images

    @property
    def values(self):
        return [[[connection.value for connection in row]
                for row in depth_slice]
                for depth_slice in self._images]

    @values.setter
    def values(self, values):
        validate_dimensions_layer(values)
        validate_same_dimensions_layer(self._images, values)

        for i in range(len(self._images)):
            for j in range(len(self._images[i])):
                for k in range(len(self._images[i][j])):
                    self._images[i][j][k].value = values[i][j][k]

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self._images[i]
                    for i in range(*key.indices(len(self._images)))]
        if (key >= 0) and (key < len(self._images)):
            return self._images[key]
        else:
            raise IndexError("Layer depth exceeded.")

    def __len__(self):
        return len(self._images)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == len(self._images):
            raise StopIteration

        self._index += 1
        return self._images[self._index - 1]
