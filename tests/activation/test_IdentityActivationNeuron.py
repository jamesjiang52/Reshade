import reshade as rs


class TestIdentityActivationNeuron:
    def test_IdentityActivationNeuron(self):
        input = rs.Connection()
        output = rs.Connection()

        rs.activation.IdentityActivationNeuron(input, output)

        assert input.value == 0
        assert output.value == 0

        input.value = -1
        assert output.value == -1

        input.value = -2
        assert output.value == -2

        input.value = 1
        assert output.value == 1

        input.value = 2
        assert output.value == 2
