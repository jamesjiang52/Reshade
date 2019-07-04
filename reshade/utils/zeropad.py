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
    Zero-pad the input image.

    Args:
        inputs: A 2-dimensional list-like, or an object of type Image. The
            input image.
        left: A non-negative integer. The amount to zero-pad on the left. If
            not given, defaults to 0.
        right: A non-negative integer. The amount to zero-pad on the right. If
            not given, defaults to 0.
        top: A non-negative integer. The amount to zero-pad on the top. If not
            given, defaults to 0.
        bottom: A non-negative integer. The amount to zero-pad on the bottom.
            If not given, defaults to 0.

    Returns: An object of type Image. The zero-padded input image.
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
    Zero-pad the input layer.

    Args:
        inputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The input layer.
        left: A non-negative integer. The amount to zero-pad on the left. If
            not given, defaults to 0.
        right: A non-negative integer. The amount to zero-pad on the right. If
            not given, defaults to 0.
        top: A non-negative integer. The amount to zero-pad on the top. If not
            given, defaults to 0.
        bottom: A non-negative integer. The amount to zero-pad on the bottom.
            If not given, defaults to 0.

    Returns: An object of type ConnectionLayer. The zero-padded input layer.
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
