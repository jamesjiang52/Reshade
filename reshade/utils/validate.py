"""
The following function are defined:
    validate_dimensions_image
    validate_dimensions_layer
    validate_same_dimensions_spectrum
    validate_same_dimensions_image
    validate_same_dimensions_layer
    validate_receptive_parameters_image
"""


def validate_dimensions_image(inputs):
    """
    """
    width = len(inputs[0])
    for i in range(len(inputs)):
        if len(inputs[i]) != width:
            raise TypeError(
                "Expected {0} arguments for row {1}, "
                "received {2}.".format(
                    width,
                    i,
                    len(inputs[i])
                )
            )


def validate_dimensions_layer(inputs):
    """
    """
    height = len(inputs[0])
    width = len(inputs[0][0])
    for i in range(len(inputs)):
        if len(inputs[i]) != height:
            raise TypeError(
                "Expected {0} rows for depth slice {1}, "
                "received {2}.".format(
                    height,
                    i,
                    len(inputs[i])
                )
            )

        for j in range(len(inputs[i])):
            if len(inputs[i][j]) != width:
                raise TypeError(
                    "Expected {0} arguments for row {1} "
                    "of depth slice {2}, received {3}.".format(
                        width,
                        j,
                        i,
                        len(inputs[i][j])
                    )
                )


def validate_same_dimensions_spectrum(inputs, outputs):
    """
    """
    if len(outputs) != len(inputs):
        raise TypeError(
            "Expected {0} output arguments, received {1}.".format(
                len(inputs),
                len(outputs)
            )
        )


def validate_same_dimensions_image(inputs, outputs):
    """
    """
    if len(outputs) != len(inputs):
        raise TypeError(
            "Expected {0} output rows, received {1}.".format(
                len(inputs),
                len(outputs)
            )
        )

    for i in range(len(inputs)):
        if len(outputs[i]) != len(inputs[i]):
            raise TypeError(
                "Expected {0} output arguments for row {1}, "
                "received {2}.".format(
                    len(inputs[i]),
                    i,
                    len(outputs[i])
                )
            )


def validate_same_dimensions_layer(inputs, outputs):
    """
    """
    if len(outputs) != len(inputs):
        raise TypeError(
            "Expected {0} output depth slices, received {1}.".format(
                len(inputs),
                len(outputs)
            )
        )

    for i in range(len(inputs)):
        if len(outputs[i]) != len(inputs[i]):
            raise TypeError(
                "Expected {0} output rows for depth slice {1}, "
                "received {2}.".format(
                    len(inputs[i]),
                    i,
                    len(outputs[i])
                )
            )

        for j in range(len(inputs[i])):
            if len(outputs[i][j]) != len(inputs[i][j]):
                raise TypeError(
                    "Expected {0} output arguments for row {1} "
                    "of depth slice {2}, received {3}.".format(
                        len(inputs[i][j]),
                        j,
                        i,
                        len(outputs[i][j])
                    )
                )


def validate_receptive_parameters_image(
    inputs,
    outputs,
    receptive_height,
    receptive_width,
    stride_height,
    stride_width
):
    """
    """
    if len(inputs) < receptive_height:
        raise ValueError(
            "Input height must be greater than or equal to receptive height."
        )
    if len(inputs) % stride_height != receptive_height % stride_height:
        raise ValueError(
            "Input height is not compatible with current receptive height "
            "and stride height."
        )
    if len(outputs) != \
            (len(inputs) - receptive_height)//stride_height + 1:
        raise ValueError(
            "Output height does not match current input height, receptive"
            "height, and stride height (received {0}, expected "
            "{1}).".format(
                len(outputs),
                (len(inputs) - receptive_height)//stride_height + 1
            )
        )
    if receptive_height < stride_height:
        raise ValueError(
            "Receptive height must be greater than or equal to stride "
            "height."
        )

    if len(inputs[0]) < receptive_width:
        raise ValueError(
            "Input width must be greater than or equal to receptive width."
        )
    if len(inputs[0]) % stride_width != receptive_width % stride_width:
        raise ValueError(
            "Input width is not compatible with current receptive width and "
            "stride width."
        )
    if len(outputs[0]) != \
            (len(inputs[0]) - receptive_width)//stride_width + 1:
        raise ValueError(
            "Output width does not match current input width, receptive "
            "width, and stride width (received {0}, expected {1}).".format(
                len(outputs[0]),
                (len(inputs[0]) - receptive_width)//stride_width + 1
            )
        )
    if receptive_width < stride_width:
        raise ValueError(
            "Receptive width must be greater than or equal to stride width."
        )


def validate_receptive_parameters_layer(
    inputs,
    outputs,
    receptive_height,
    receptive_width,
    stride_height,
    stride_width
):
    """
    """
    if len(inputs[0]) < receptive_height:
        raise ValueError(
            "Input height must be greater than or equal to receptive height."
        )
    if len(inputs[0]) % stride_height != receptive_height % stride_height:
        raise ValueError(
            "Input height is not compatible with current receptive height "
            "and stride height."
        )
    if len(outputs[0]) != \
            (len(inputs[0]) - receptive_height)//stride_height + 1:
        raise ValueError(
            "Output height does not match current input height, receptive"
            "height, and stride height (received {0}, expected "
            "{1}).".format(
                len(outputs[0]),
                (len(inputs[0]) - receptive_height)//stride_height + 1
            )
        )
    if receptive_height < stride_height:
        raise ValueError(
            "Receptive height must be greater than or equal to stride "
            "height."
        )

    if len(inputs[0][0]) < receptive_width:
        raise ValueError(
            "Input width must be greater than or equal to receptive width."
        )
    if len(inputs[0][0]) % stride_width != receptive_width % stride_width:
        raise ValueError(
            "Input width is not compatible with current receptive width and "
            "stride width."
        )
    if len(outputs[0][0]) != \
            (len(inputs[0][0]) - receptive_width)//stride_width + 1:
        raise ValueError(
            "Output width does not match current input width, receptive "
            "width, and stride width (received {0}, expected {1}).".format(
                len(outputs[0][0]),
                (len(inputs[0][0]) - receptive_width)//stride_width + 1
            )
        )
    if receptive_width < stride_width:
        raise ValueError(
            "Receptive width must be greater than or equal to stride width."
        )


def validate_receptive_parameters_layer_image(
    inputs,
    outputs,
    receptive_height,
    receptive_width,
    stride_height,
    stride_width
):
    """
    """
    if len(inputs[0]) < receptive_height:
        raise ValueError(
            "Input height must be greater than or equal to receptive height."
        )
    if len(inputs[0]) % stride_height != receptive_height % stride_height:
        raise ValueError(
            "Input height is not compatible with current receptive height "
            "and stride height."
        )
    if len(outputs) != \
            (len(inputs[0]) - receptive_height)//stride_height + 1:
        raise ValueError(
            "Output height does not match current input height, receptive"
            "height, and stride height (received {0}, expected "
            "{1}).".format(
                len(outputs),
                (len(inputs[0]) - receptive_height)//stride_height + 1
            )
        )
    if receptive_height < stride_height:
        raise ValueError(
            "Receptive height must be greater than or equal to stride "
            "height."
        )

    if len(inputs[0][0]) < receptive_width:
        raise ValueError(
            "Input width must be greater than or equal to receptive width."
        )
    if len(inputs[0][0]) % stride_width != receptive_width % stride_width:
        raise ValueError(
            "Input width is not compatible with current receptive width and "
            "stride width."
        )
    if len(outputs[0]) != \
            (len(inputs[0][0]) - receptive_width)//stride_width + 1:
        raise ValueError(
            "Output width does not match current input width, receptive "
            "width, and stride width (received {0}, expected {1}).".format(
                len(outputs[0]),
                (len(inputs[0][0]) - receptive_width)//stride_width + 1
            )
        )
    if receptive_width < stride_width:
        raise ValueError(
            "Receptive width must be greater than or equal to stride width."
        )
