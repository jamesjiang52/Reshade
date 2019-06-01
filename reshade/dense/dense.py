"""
The following classes are defined:
    DenseLayer
"""

from neuron import Neuron


class DenseLayer:
    def __init__(self, inputs, outputs):
        self._inputs = inputs
        self._outputs = outputs
        self._neurons = [Neuron(inputs, output) for output in outputs]
