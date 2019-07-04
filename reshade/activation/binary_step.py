"""
The following classes are defined:
    BinaryStepActivationNeuron
    BinaryStepActivationLayer
"""

from ..utils.validate import *


class BinaryStepActivationNeuron:
    """
    Construct a new binary step activation neuron. The output takes on the
    value of 1 if the input is greater than or equal to 0, and 0 otherwise.

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
        if self._input.value >= 0:
            self._output.value = 1
        else:
            self._output.value = 0


class BinaryStepActivationLayer:
    """
    Construct a new binary step activation layer. Each neuron in the layer
    performs binary step activation on its input in the input layer for the
    corresponding output in the output layer.

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
            BinaryStepActivationNeuron(inputs[i][j][k], outputs[i][j][k])
            for k in range(len(inputs[0][0]))]
            for j in range(len(inputs[0]))]
            for i in range(len(inputs))]
