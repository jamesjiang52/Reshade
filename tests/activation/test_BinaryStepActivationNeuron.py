import reshade as rs


class TestBinaryStepActivationNeuron:
    def test_BinaryStepActivationNeuron(self):
        input = rs.Connection()
        output = rs.Connection()

        rs.activation.BinaryStepActivationNeuron(input, output)

        assert input.value == 0
        assert output.value == 0

        input.value = -1
        assert output.value == 0

        input.value = -2
        assert output.value == 0

        input.value = 1
        assert output.value == 1

        input.value = 2
        assert output.value == 1
