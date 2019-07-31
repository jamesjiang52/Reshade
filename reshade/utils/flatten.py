"""
The following functions are defined:
    flatten_image
    flatten_layer

The following classes are defined:
    FlattenLayer
"""

from ..connection.spectrum import Spectrum
from .validate import *


def flatten_image(inputs):
    """
    Flatten the input image to a spectrum, row-by-row.
    Args:
        inputs: An object of type Image. The input image.

    Returns: An object of type Spectrum. The flattened input image.
    """
    return Spectrum(
        connections=[input_ for row in inputs for input_ in row]
    )


def flatten_layer(inputs):
    """
    Flatten the input layer to a spectrum, depth-slice-by-depth-slice, row-by-
    row.

    Args:
        inputs: An object of type ConnectionLayer. The input layer.

    Returns: An object of type Spectrum. The flattened input layer.
    """
    return Spectrum(
        connections=[input_ for depth_slice in inputs
                     for row in depth_slice
                     for input_ in row]
    )


class FlattenLayer:
    """
    Construct a new flattening layer. The input layer is flattened to form the
    output spectrum.

    Args:
        inputs: An object of type ConnectionLayer. The input layer.
        outputs: An object of type Spectrum. The output spectrum.
    """
    def __init__(self, inputs, outputs):
        validate_dimensions_layer(inputs)
        validate_same_dimensions_flatten(inputs, outputs)

        self._inputs = flatten_layer(inputs)
        self._outputs = outputs

        for input_ in self._inputs:
            input_.bind_to(self._update_inputs)

        self._update_inputs()

    def _update_inputs(self):
        self._outputs.values = self._inputs.values
