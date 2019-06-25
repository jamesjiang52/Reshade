"""
The following classes are defined:
    DenseNeuron
    DenseLayer
"""

from ..utils.validate import *


class DenseNeuron:
    def __init__(self, inputs, output):
        self._inputs = inputs
        self._weights = [1]*len(inputs)
        self._output = output

        for input_ in self._inputs:
            input_.bind_to(self._update_inputs)

        self._update_inputs()

    def _update_inputs(self):
        self._output.value = sum([
            self._weights[i]*self._inputs[i].value
            for i in range(len(self._inputs))
        ])

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, weights):
        validate_same_dimensions_spectrum(self._weights, weights)

        self._weights = weights
        self._update_inputs()


class DenseLayer:
    def __init__(self, inputs, outputs):
        self._inputs = inputs
        self._outputs = outputs
        self._neurons = [DenseNeuron(inputs, output) for output in outputs]

    @property
    def neurons(self):
        return self._neurons
