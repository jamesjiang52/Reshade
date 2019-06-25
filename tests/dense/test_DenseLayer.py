import reshade as rs


class TestDenseLayer:
    def test_DenseLayer(self):
        inputs = rs.Spectrum(width=3)
        outputs = rs.Spectrum(width=4)
        dense_layer = rs.dense.DenseLayer(inputs, outputs)

        assert inputs.values == [0, 0, 0]
        assert [round(value, 2) for value in outputs.values] == [0, 0, 0, 0]

        inputs.values = [0.1, 0.2, 0.3]
        assert [round(value, 2) for value in outputs.values] == [
            0.6, 0.6, 0.6, 0.6]

        dense_layer.neurons[0].weights = [1, 0, 0]
        assert [round(value, 2) for value in outputs.values] == [
            0.1, 0.6, 0.6, 0.6]

        dense_layer.neurons[1].weights = [0, 1, 0]
        assert [round(value, 2) for value in outputs.values] == [
            0.1, 0.2, 0.6, 0.6]

        dense_layer.neurons[2].weights = [0, 0, 1]
        assert [round(value, 2) for value in outputs.values] == [
            0.1, 0.2, 0.3, 0.6]

        dense_layer.neurons[3].weights = [0, 0, 0]
        assert [round(value, 2) for value in outputs.values] == [
            0.1, 0.2, 0.3, 0]

        inputs.values = [3, 2, 1]
        assert [round(value, 2) for value in outputs.values] == [3, 2, 1, 0]
