"""
The following classes are defined:
    SigmoidActivationNeuron
    SigmoidActivationLayer
"""

from math import exp
from ..utils.validate import *


class SigmoidActivationNeuron:
    """
    Construct a new sigmoid activation neuron. The output takes on the
    reciprocal of one plus e raised to the power of the negative input,
    otherwise known as the logistic function.

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
        self._output.value = 1/(1 + exp(-self._input.value))


class SigmoidActivationLayer:
    """
    Construct a new sigmoid activation layer. Each neuron in the layer performs
    sigmoid activation on its input in the input layer for the corresponding
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
            SigmoidActivationNeuron(inputs[i][j][k], outputs[i][j][k])
            for k in range(len(inputs[0][0]))]
            for j in range(len(inputs[0]))]
            for i in range(len(inputs))]
