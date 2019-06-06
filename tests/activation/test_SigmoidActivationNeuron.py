import reshade as rs


class TestSigmoidActivationNeuron:
    def test_SigmoidActivationNeuron(self):
        input = rs.Connection()
        output = rs.Connection()

        rs.activation.SigmoidActivationNeuron(input, output)

        assert input.value == 0
        assert round(output.value, 2) == 0.50

        input.value = -1
        assert round(output.value, 2) == 0.27

        input.value = -2
        assert round(output.value, 2) == 0.12

        input.value = 1
        assert round(output.value, 2) == 0.73

        input.value = 2
        assert round(output.value, 2) == 0.88
