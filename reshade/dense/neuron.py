"""
The following classes are defined:
    Neuron
"""


class Neuron:
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
