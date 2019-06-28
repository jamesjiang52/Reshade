"""
The following classes are defined:
    TanhActivationNeuron
    TanhActivationLayer
"""

from math import tanh
from ..utils.validate import *


class TanhActivationNeuron:
    """
    Construct a new tanh activation neuron. The output takes on the hyperbolic
    tangent of the input.

    Args:
        input: An object of type Connection. The input.
        output: An object of type Connection. The output.
    """
    def __init__(self, input, output):
        self._input = input
        self._output = output

        self._input.bind_to(self._update_input)
        self._update_input()

    def _update_input(self):
        self._output.value = tanh(self._input.value)


class TanhActivationLayer:
    """
    Construct a new tanh activation layer. Each neuron in the layer performs
    tanh activation on its input in the input layer for the corresponding
    output in the output layer.

    Args:
        inputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The input layer.
        outputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The output layer.
    """
    def __init__(self, inputs, outputs):
        validate_dimensions_layer(inputs)
        validate_dimensions_layer(outputs)
        validate_same_dimensions_layer(inputs, outputs)

        self._inputs = inputs
        self._outputs = outputs
        self._neurons = [[[
            TanhActivationNeuron(inputs[i][j][k], outputs[i][j][k])
            for k in range(len(inputs[0][0]))]
            for j in range(len(inputs[0]))]
            for i in range(len(inputs))]
