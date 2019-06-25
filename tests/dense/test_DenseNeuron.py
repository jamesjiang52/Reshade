import reshade as rs


class TestDenseNeuron:
    def test_DenseNeuron(self):
        inputs = rs.Spectrum(width=4)
        output = rs.Connection()
        neuron = rs.dense.DenseNeuron(inputs, output)

        assert inputs.values == [0, 0, 0, 0]
        assert neuron.weights == [1, 1, 1, 1]
        assert output.value == 0

        inputs.values = [0.1, 0.2, 0.3, 0.4]
        assert round(output.value, 2) == 1.0

        neuron.weights = [4, 3, 2, 1]
        assert round(output.value, 2) == 2.0

        neuron.weights = [0.5, 1, 1.5, 2]
        assert round(output.value, 2) == 1.5

        inputs.values = [2, 2, 1, 1]
        assert round(output.value, 2) == 6.5
