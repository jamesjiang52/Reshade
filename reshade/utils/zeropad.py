"""
The following functions are defined:
    zeropad_image
    zeropad_layer
"""

from ..connection.connection import Connection
from ..connection.image import Image
from ..connection.layer import ConnectionLayer


def zeropad_image(inputs, left=0, right=0, top=0, bottom=0):
    """
    """
    return Image(
        spectra=[[Connection(0) for j in range(len(inputs[0]) + left + right)]
            for i in range(top)] + \
            [[Connection(0) for j in range(left)] + list(row) +
            [Connection(0) for j in range(right)] for row in inputs] + \
            [[Connection(0) for j in range(len(inputs[0]) + left + right)]
            for i in range(bottom)]
    )


def zeropad_layer(inputs, left=0, right=0, top=0, bottom=0):
    """
    """
    return ConnectionLayer(
        images=[
            [[Connection(0) for j in range(len(inputs[0]) + left + right)]
            for i in range(top)] + \
            [[Connection(0) for j in range(left)] + list(row) +
            [Connection(0) for j in range(right)] for row in depth_slice] + \
            [[Connection(0) for j in range(len(inputs[0]) + left + right)]
            for i in range(bottom)]
            for depth_slice in inputs
        ]
    )
