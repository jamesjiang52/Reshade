"""
The following classes are defined:
    ZeropadLayer
"""

from .validate import *


class ZeropadLayer:
    """
    Construct a new zero-padding layer. The input layer is zero-padded by
    the specified amount to form the output layer.

    Args:
        inputs: An object of type ConnectionLayer. The input layer.
        outputs: An object of type ConnectionLayer. The output layer.
        left: A non-negative integer. The amount to zero-pad on the left. If
            not given, defaults to 0.
        right: A non-negative integer. The amount to zero-pad on the right. If
            not given, defaults to 0.
        top: A non-negative integer. The amount to zero-pad on the top. If not
            given, defaults to 0.
        bottom: A non-negative integer. The amount to zero-pad on the bottom.
            If not given, defaults to 0.
    """
    def __init__(self, inputs, outputs, left=0, right=0, top=0, bottom=0):
        validate_dimensions_layer(inputs)
        validate_dimensions_layer(outputs)
        validate_same_dimensions_zeropad(
            inputs,
            outputs,
            left,
            right,
            top,
            bottom
        )

        self._inputs = inputs
        self._outputs = outputs
        self._left = left
        self._right = right
        self._top = top
        self._bottom = bottom

        for depth_slice in self._inputs:
            for row in depth_slice:
                for input_ in row:
                    input_.bind_to(self._update_inputs)

        self._update_inputs()

    def _update_inputs(self):
        self._outputs.values = [
            [[0 for j in range(len(self._inputs[0][0]) +
                               self._left + self._right)]
                for i in range(self._top)] +
            [[0 for j in range(self._left)] + row.values +
                [0 for j in range(self._right)]
                for row in depth_slice] +
            [[0 for j in range(len(self._inputs[0][0]) +
                               self._left + self._right)]
                for i in range(self._bottom)]
            for depth_slice in self._inputs
        ]
