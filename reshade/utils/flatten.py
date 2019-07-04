"""
The following functions are defined:
    flatten_image
    flatten_layer
"""

from ..connection.spectrum import Spectrum


def flatten_image(inputs):
    """
    """
    return Spectrum(
        connections=[input_ for row in inputs for input_ in row]
    )


def flatten_layer(inputs):
    """
    """
    return Spectrum(
        connections=[input_ for depth_slice in inputs
                     for row in depth_slice
                     for input_ in row]
    )
