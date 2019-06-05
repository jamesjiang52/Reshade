"""
The following classes are defined:
    SigmoidActivationNeuron
    SigmoidActivationLayer
"""

from math import exp


class SigmoidActivationNeuron:
    def __init__(self, input, output):
        self._input = input
        self._output = output

        self._input.bind_to(self._update_input)
        self._update_input()

    def _update_input(self):
        self._output.value = 1/(1 + exp(-self._input.value))


class SigmoidActivationLayer:
    def __init__(self, inputs, outputs):
        if len(outputs) != len(inputs):
            raise TypeError(
                "Expected {0} outputs, received {1}.".format(
                    len(inputs),
                    len(outputs)
                )
            )

        self._inputs = inputs
        self._outputs = outputs
        self._neurons = [
            SigmoidActivationNeuron(inputs[i], outputs[i])
            for i in range(len(inputs))
        ]
