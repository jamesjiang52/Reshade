"""
The following classes are defined:
    L2NormPoolingNeuron
    L2NormPoolingLayer
"""

from math import sqrt
from ..utils.validate import *
from ..utils.flatten import *


class L2NormPoolingNeuron:
    """
    Construct a new l2norm pooling neuron. The output takes on the square root
    of the sum of the squares of the values in the input image.

    Args:
        inputs: An object of type Image. The input image.
        output: An object of type Connection. The output.
    """
    def __init__(self, inputs, output):
        validate_dimensions_image(inputs)

        self._inputs = flatten_image(inputs)
        self._output = output

        for input_ in self._inputs:
            input_.bind_to(self._update_inputs)

        self._update_inputs()

    def _update_inputs(self):
        self._output.value = sqrt(
            sum([input_.value**2 for input_ in self._inputs])
        )


class L2NormPoolingLayer:
    """
    Construct a new l2norm pooling layer. Each neuron in the layer performs
    l2norm pooling on its receptive field in the input layer for the
    corresponding output in the output layer.

    Args:
        inputs: An object of type ConnectionLayer. The input layer.
        outputs: An object of type ConnectionLayer. The output layer.
        receptive_height: A positive integer. The height of the receptive
            field.
        receptive_width: A positive integer. The width of the receptive field.
        stride_height: A positive integer. The stride height across adjacent
            receptive fields.
        stride_width: A positive integer. The stride width across adjacent
            receptive fields.
    """
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
        self._neurons = [[[
            L2NormPoolingNeuron(
                [row[x:x + receptive_width]
                    for row in self._inputs[d][y:y + receptive_height]],
                self._outputs[d][y//stride_height][x//stride_width]
            )
            for x in range(0, len(self._inputs[d][y]) - receptive_width + 1,
                           stride_width)]
            for y in range(0, len(self._inputs[d]) - receptive_height + 1,
                           stride_height)]
            for d in range(len(inputs))]
