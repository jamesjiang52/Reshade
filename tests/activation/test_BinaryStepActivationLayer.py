import reshade as rs


class TestBinaryStepActivationLayer:
    def test_BinaryStepActivationLayer(self):
        inputs = rs.ConnectionLayer(depth=1, height=2, width=2)
        outputs = rs.ConnectionLayer(depth=1, height=2, width=2)

        rs.activation.BinaryStepActivationLayer(inputs, outputs)

        assert inputs.values == [
            [[0, 0],
             [0, 0]]
        ]
        assert outputs.values == [
            [[1, 1],
             [1, 1]]
        ]

        inputs.values = [
            [[-1, -2],
             [1, 2]]
        ]
        assert outputs.values == [
            [[0, 0],
             [1, 1]]
        ]
