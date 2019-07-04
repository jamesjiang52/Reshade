"""
The following functions are defined:
    flatten_image
    flatten_layer
"""

from ..connection.spectrum import Spectrum


def flatten_image(inputs):
    """
    Flatten the input image to a spectrum, row-by-row.

    Args:
        inputs: A 2-dimensional list-like, or an object of type Image. The
            input image.

    Returns: An object of type Spectrum.
    """
    return Spectrum(
        connections=[input_ for row in inputs for input_ in row]
    )


def flatten_layer(inputs):
    """
    Flatten the input layer to a spectrum, depth-slice-by-depth-slice, row-by-
    row.

    Args:
        inputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The input layer.

    Returns: An object of type Spectrum.
    """
    return Spectrum(
        connections=[input_ for depth_slice in inputs
                     for row in depth_slice
                     for input_ in row]
    )
