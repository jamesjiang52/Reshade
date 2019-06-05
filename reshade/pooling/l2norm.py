"""
The following classes are defined:
    L2NormPoolingNeuron
    L2NormPoolingLayer
"""

from math import sqrt


class L2NormPoolingNeuron:
    def __init__(self, inputs, output):
        self._inputs = inputs
        self._output = output

        for row in self._inputs:
            for input_ in row:
                input_.bind_to(self._update_inputs)

        self._update_inputs()

    def _update_inputs(self):
        self._output.value = sqrt(
            sum([input_.value**2 for row in self._inputs for input_ in row])
        )


class L2NormPoolingLayer:
    def __init__(
        self,
        inputs,
        outputs,
        pooling_height,
        pooling_width,
        stride_height,
        stride_width
    ):
        if len(inputs) < pooling_height:
            raise ValueError(
                "Input height must be greater than or equal to pooling height."
            )
        if len(inputs) % stride_height != pooling_height % stride_height:
            raise ValueError(
                "Input height is not compatible with current pooling height "
                "and stride height."
            )
        if len(outputs) != (len(inputs) - pooling_height)/stride_height + 1:
            raise ValueError(
                "Output height does not match current input height, pooling"
                "height, and stride height (received {0}, expected "
                "{1}).".format(
                    len(outputs),
                    (len(inputs) - pooling_height)/stride_height + 1
                )
            )
        if pooling_height < stride_height:
            raise ValueError(
                "Pooling height must be greater than or equal to stride "
                "height."
            )

        if len(inputs[0]) < pooling_width:
            raise ValueError(
                "Input width must be greater than or equal to pooling width."
            )
        if len(inputs[0]) % stride_width != pooling_width % stride_width:
            raise ValueError(
                "Input width is not compatible with current pooling width and "
                "stride width."
            )
        if len(outputs[0]) != \
                (len(inputs[0]) - pooling_width)/stride_width:
            raise ValueError(
                "Output width does not match current input width, pooling "
                "width, and stride width (received {0}, expected {1}).".format(
                    len(outputs[0]),
                    (len(inputs[0]) - pooling_width)/stride_width + 1
                )
            )
        if pooling_width < stride_width:
            raise ValueError(
                "Pooling width must be greater than or equal to stride width."
            )

        self._inputs = inputs
        self._outputs = outputs
        self._neurons = [
            L2NormPoolingNeuron(
                [row[x:x + pooling_width]
                    for row in self._inputs[y:y + pooling_height]],
                self._outputs[y/stride_height][x/stride_width]
            )
            for y in range(0, len(self._inputs) - pooling_height + 1,
                           stride_height)
            for x in range(0, len(self._inputs[0]) - pooling_width + 1,
                           stride_width)
        ]
