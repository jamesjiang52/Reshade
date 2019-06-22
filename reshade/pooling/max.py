"""
The following classes are defined:
    MaxPoolingNeuron
    MaxPoolingLayer
"""

from ..utils.validate import *


class MaxPoolingNeuron:
    def __init__(self, inputs, output):
        validate_dimensions_image(inputs)

        self._inputs = inputs
        self._output = output

        for row in self._inputs:
            for input_ in row:
                input_.bind_to(self._update_inputs)

        self._update_inputs()

    def _update_inputs(self):
        self._output.value = max([
            input_.value for row in self._inputs for input_ in row
        ])


class MaxPoolingLayer:
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
            MaxPoolingNeuron(
                [row[x:x + receptive_width]
                    for row in self._inputs[d][y:y + receptive_height]],
                self._outputs[d][y//stride_height][x//stride_width]
            )
            for x in range(0, len(self._inputs[d][y]) - receptive_width + 1,
                           stride_width)]
            for y in range(0, len(self._inputs[d]) - receptive_height + 1,
                           stride_height)]
            for d in range(len(inputs))]
