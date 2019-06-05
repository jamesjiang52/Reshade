import reshade as rs


class TestLeakyReLUActivationNeuron:
    def __init__(self):
        input = rs.Connection()
        output = rs.Connection()

        rs.activation.LeakyReLUActivationNeuron(input, output)

        assert input.value == 0
        assert output.value == 0

        input.value = -1
        assert output.value == -0.01

        input.value = -2
        assert output.value == -0.02

        input.value = 1
        assert output.value == 1

        input.value = 2
        assert output.value == 2
