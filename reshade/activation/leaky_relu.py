"""
The following classes are defined:
    LeakyReLUActivationNeuron
    LeakyReLUActivationLayer
"""

from ..utils.validate import *


class LeakyReLUActivationNeuron:
    def __init__(self, input, output):
        self._input = input
        self._output = output

        self._input.bind_to(self._update_input)
        self._update_input()

    def _update_input(self):
        if self._input.value > 0:
            self._output.value = self._input.value
        else:
            self._output.value = self._input.value*0.01


class LeakyReLUActivationLayer:
    def __init__(self, inputs, outputs):
        validate_dimensions_layer(inputs)
        validate_dimensions_layer(outputs)
        validate_same_dimensions_layer(inputs, outputs)

        self._inputs = inputs
        self._outputs = outputs
        self._neurons = [[[
            LeakyReLUActivationNeuron(inputs[i][j][k], outputs[i][j][k])
            for k in range(len(inputs[0][0]))]
            for j in range(len(inputs[0]))]
            for i in range(len(inputs))]
