import reshade as rs


class TestTanhActivationNeuron:
    def __init__(self):
        input = rs.Connection()
        output = rs.Connection()

        rs.activation.TanhActivationNeuron(input, output)

        assert input.value == 0
        assert round(output.value, 2) == 0.00

        input.value = -1
        assert round(output.value, 2) == -0.76

        input.value = -2
        assert round(output.value, 2) == -0.96

        input.value = 1
        assert round(output.value, 2) == 0.76

        input.value = 2
        assert round(output.value, 2) == 0.96
