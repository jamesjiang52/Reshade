import reshade as rs


class TestSigmoidActivationLayer:
    def test_SigmoidActivationLayer(self):
        inputs = rs.ConnectionLayer(depth=1, height=2, width=2)
        outputs = rs.ConnectionLayer(depth=1, height=2, width=2)

        rs.activation.SigmoidActivationLayer(inputs, outputs)

        assert inputs.values == [
            [[0, 0],
             [0, 0]]
        ]
        assert [[[round(value, 2) for value in row]
                 for row in depth_slice]
                for depth_slice in outputs.values] == [
            [[0.50, 0.50],
             [0.50, 0.50]]
        ]

        inputs.values = [
            [[-1, -2],
             [1, 2]]
        ]
        assert [[[round(value, 2) for value in row]
                 for row in depth_slice]
                for depth_slice in outputs.values] == [
            [[0.27, 0.12],
             [0.73, 0.88]]
        ]
