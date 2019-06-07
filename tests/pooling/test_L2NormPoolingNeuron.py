import reshade as rs


class TestL2NormPoolingNeuron:
    def test_L2NormPoolingNeuron(self):
        inputs = rs.Image(height=4, width=4)
        output = rs.Connection()

        rs.pooling.L2NormPoolingNeuron(inputs, output)

        assert inputs.values == [[0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0]]
        assert round(output.value, 2) == 0.00

        inputs.values = [[0, 0, 0, 10],
                         [0, 0, -2, 0],
                         [2, 0, 0, 0],
                         [0, 6, 0, 0]]
        assert round(output.value, 2) == 12.00

        inputs.values = [[1, 2, 3, 4],
                         [-1, -4, -9, -16],
                         [2.79, 3.14, 1, 0],
                         [0, 0, 0, 0]]
        assert round(output.value, 2) == 20.07
