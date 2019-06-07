import reshade as rs


class TestReLUActivationLayer:
    def test_ReLUActivationLayer(self):
        inputs = rs.ConnectionLayer(depth=1, height=2, width=2)
        outputs = rs.ConnectionLayer(depth=1, height=2, width=2)

        rs.activation.ReLUActivationLayer(inputs, outputs)

        assert inputs.values == [
            [[0, 0],
             [0, 0]]
        ]
        assert outputs.values == [
            [[0, 0],
             [0, 0]]
        ]

        inputs.values = [
            [[-1, -2],
             [1, 2]]
        ]
        assert outputs.values == [
            [[0, 0],
             [1, 2]]
        ]
