"""
The following classes are defined:
    ConvolutionNeuron
    ConvolutionFilter
    ConvolutionLayer
"""

from ..dense import DenseNeuron
from ..utils.validate import *


class ConvolutionNeuron:
    def __init__(self, inputs, output):
        validate_dimensions_layer(inputs)

        self._inputs = inputs
        self._output = output

        DenseNeuron(
            [input_ for depth_slice in self._inputs
             for row in depth_slice
             for input_ in row],
            self._output
        )


class ConvolutionFilter:
    def __init__(
        self,
        inputs,
        outputs,
        receptive_height,
        receptive_width,
        stride_height,
        stride_width
    ):
        validate_dimensions_layer(inputs)
        validate_dimensions_image(outputs)
        validate_receptive_parameters_layer_image(
            inputs,
            outputs,
            receptive_height,
            receptive_width,
            stride_height,
            stride_width
        )

        self._inputs = inputs
        self._outputs = outputs
        self._neurons = [
            ConvolutionNeuron(
                inputs[:][y:y + receptive_height][x:x + receptive_width],
                self._outputs[y/stride_height][x/stride_width]
            )
            for y in range(0, len(self._inputs[0]) - receptive_height + 1,
                           stride_height)
            for x in range(0, len(self._inputs[0][0]) - receptive_width + 1,
                           stride_width)
        ]


class ConvolutionLayer:
    def __init__(
        self,
        inputs,
        outputs,
        receptive_height,
        receptive_width,
        stride_height,
        stride_width
    ):
        validate_dimensions_layer(inputs)
        validate_dimensions_layer(outputs)
        validate_receptive_parameters_layer(
            inputs,
            outputs,
            receptive_height,
            receptive_width,
            stride_height,
            stride_width
        )

        self._inputs = inputs
        self._outputs = outputs
        self._filters = [
            ConvolutionFilter(
                self._inputs,
                self._outputs[depth],
                receptive_height,
                receptive_width,
                stride_height,
                stride_width
            )
            for depth in range(len(outputs))
        ]
