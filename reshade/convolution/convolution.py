"""
The following classes are defined:
    ConvolutionNeuron
    ConvolutionFilter
    ConvolutionLayer
"""

from ..dense import Neuron


class ConvolutionNeuron:
    def __init__(self, inputs, output):
        self._inputs = inputs
        self._output = output

        Neuron(
            [input_ for row in self._inputs for input_ in row],
            self._output
        )
        
        
class ConvolutionFilter:
    def __init__(
        self, 
        inputs, 
        outputs,
        filter_height,
        filter_width,
        stride_height,
        stride_width
    ):
        if len(inputs) < filter_height:
            raise ValueError(
                "Input height must be greater than or equal to filter height."
            )
        if len(inputs) % stride_height != filter_height % stride_height:
            raise ValueError(
                "Input height is not compatible with current filter height "
                "and stride height."
            )
        if len(outputs) != (len(inputs) - filter_height)/stride_height + 1:
            raise ValueError(
                "Output height does not match current input height, filter"
                "height, and stride height (received {0}, expected "
                "{1}).".format(
                    len(outputs),
                    (len(inputs) - filter_height)/stride_height + 1
                )
            )
        if filter_height < stride_height:
            raise ValueError(
                "Filter height must be greater than or equal to stride "
                "height."
            )

        if len(inputs[0]) < filter_width:
            raise ValueError(
                "Input width must be greater than or equal to filter width."
            )
        if len(inputs[0]) % stride_width != filter_width % stride_width:
            raise ValueError(
                "Input width is not compatible with current filter width and "
                "stride width."
            )
        if len(outputs[0]) != \
                (len(inputs[0]) - filter_width)/stride_width:
            raise ValueError(
                "Output width does not match current input width, filter "
                "width, and stride width (received {0}, expected {1}).".format(
                    len(outputs[0]),
                    (len(inputs[0]) - filter_width)/stride_width + 1
                )
            )
        if filter_width < stride_width:
            raise ValueError(
                "Filter width must be greater than or equal to stride width."
            )

        self._inputs = inputs
        self._outputs = outputs
        self._neurons = [
            ConvolutionNeuron(
                [row[x:x + filter_width] 
                    for row in self._inputs[y:y + filter_height]],
                self._outputs[y/stride_height][x/stride_width]
            )
            for y in range(0, len(self._inputs) - filter_height + 1,
                           stride_height)
            for x in range(0, len(self._inputs[0]) - filter_width + 1,
                           stride_width)
        ]
        
        
class ConvolutionLayer:
    def __init__(
        self,
        inputs,
        outputs,
        filter_height,
        filter_width,
        stride_height,
        stride_width
    ):
        self._inputs = inputs
        self._outputs = outputs
        self._filters = [
            ConvolutionFilter(
                self._inputs,
                self._outputs[depth],
                filter_height,
                filter_width,
                stride_height,
                stride_width
            )
            for depth in range(len(outputs))
        ]
