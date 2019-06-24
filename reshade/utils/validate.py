"""
The following functions are defined:
    validate_dimensions_image
    validate_dimensions_layer
    validate_same_dimensions_spectrum
    validate_same_dimensions_image
    validate_same_dimensions_layer
    validate_receptive_parameters_image
    validate_receptive_parameters_layer
    validate_receptive_parameters_layer_image
"""


def validate_dimensions_image(inputs):
    """
    Checks that the input image's dimensions are consistent.

    Args:
        inputs: A 2-dimensional list-like, or an object of type Image. The
            input image.

    Raises:
        TypeError: If the input image's dimensions are not consistent.
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
    Checks that the input layer's dimensions are consistent.

    Args:
        inputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The input layer.

    Raises:
        TypeError: If the input layer's dimensions are not consistent.
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
    Checks that the output spectrum's dimension matches the input spectrum.

    Args:
        inputs: A 1-dimensional list-like, or an object of type Spectrum. The
            input spectrum.
        outputs: A 1-dimensional list-like, or an object of type Spectrum. The
            output spectrum.

    Raises:
        TypeError: If the output spectrum's dimension does not match the input
            spectrum.
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
    Checks that the output image's dimensions match the input image, under the
    precondition that both image's dimensions are consistent.

    Args:
        inputs: A 2-dimensional list-like, or an object of type Image. The
            input image.
        outputs: A 2-dimensional list-like, or an object of type Image. The
            output image.

    Raises:
        TypeError: If the output image's dimensions do not match the input
            image.
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
    Checks that the output layer's dimensions match the input layer, under the
    precondition that both layer's dimensions are consistent.

    Args:
        inputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The input layer.
        outputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The output layer.

    Raises:
        TypeError: If the output layer's dimensions do not match the input
            layer.
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
    Checks that the given receptive height, receptive width, stride height, and
    stride width are valid for the dimensions of the input and output images,
    under the precondition that both image's dimensions are consistent.

    In particular, the following are checked:
        - The height of the input is greater than or equal to the receptive
            height
        - The width of the input is greater than or equal to the receptive
            width
        - The height of the input modulo the stride height is equal to the
            receptive height modulo the stride height
        - The width of the input modulo the stride width is equal to the
            receptive width modulo the stride width
        - The height of the output is equal to the difference between the
            height of the input and the receptive height, divided by the stride
            height, plus one
        - The width of the output is equal to the difference between the width
            of the input and the receptive width, divided by the stride width,
            plus one
        - The receptive height is greater than or equal to the stride height
        - The receptive width is greater than or equal to the stride width

    Args:
        inputs: A 2-dimensional list-like, or an object of type Image. The
            input image.
        outputs: A 2-dimensional list-like, or an object of type Image. The
            output image.
        receptive_height: A positive integer. The receptive height.
        receptive_width: A positive integer. The receptive width.
        stride_height: A positive integer. The stride height.
        stride_width: A positive integer. The stride width.

    Raises:
        ValueError: If any of the above conditions do not hold.
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
    Checks that the given receptive height, receptive width, stride height, and
    stride width are valid for the dimensions of the input and output layers,
    under the precondition that both layer's dimensions are consistent.

    In particular, the following are checked:
        - The height of the input is greater than or equal to the receptive
            height
        - The width of the input is greater than or equal to the receptive
            width
        - The height of the input modulo the stride height is equal to the
            receptive height modulo the stride height
        - The width of the input modulo the stride width is equal to the
            receptive width modulo the stride width
        - The height of the output is equal to the difference between the
            height of the input and the receptive height, divided by the stride
            height, plus one
        - The width of the output is equal to the difference between the width
            of the input and the receptive width, divided by the stride width,
            plus one
        - The receptive height is greater than or equal to the stride height
        - The receptive width is greater than or equal to the stride width

    Args:
        inputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The input layer.
        outputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The output layer.
        receptive_height: A positive integer. The receptive height.
        receptive_width: A positive integer. The receptive width.
        stride_height: A positive integer. The stride height.
        stride_width: A positive integer. The stride width.

    Raises:
        ValueError: If any of the above conditions do not hold.
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
    Checks that the given receptive height, receptive width, stride height, and
    stride width are valid for the dimensions of the input layer and the output
    image, under the precondition that both the input layer's and the output
    image's dimensions are consistent.

    In particular, the following are checked:
        - The height of the input is greater than or equal to the receptive
            height
        - The width of the input is greater than or equal to the receptive
            width
        - The height of the input modulo the stride height is equal to the
            receptive height modulo the stride height
        - The width of the input modulo the stride width is equal to the
            receptive width modulo the stride width
        - The height of the output is equal to the difference between the
            height of the input and the receptive height, divided by the stride
            height, plus one
        - The width of the output is equal to the difference between the width
            of the input and the receptive width, divided by the stride width,
            plus one
        - The receptive height is greater than or equal to the stride height
        - The receptive width is greater than or equal to the stride width

    Args:
        inputs: A 3-dimensional list-like, or an object of type
            ConnectionLayer. The input layer.
        outputs: A 2-dimensional list-like, or an object of type Image. The
            output image.
        receptive_height: A positive integer. The receptive height.
        receptive_width: A positive integer. The receptive width.
        stride_height: A positive integer. The stride height.
        stride_width: A positive integer. The stride width.

    Raises:
        ValueError: If any of the above conditions do not hold.
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
