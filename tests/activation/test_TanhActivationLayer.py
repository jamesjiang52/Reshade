import reshade as rs


class TestTanhActivationLayer:
    def test_TanhActivationLayer(self):
        inputs = rs.ConnectionLayer(depth=1, height=2, width=2)
        outputs = rs.ConnectionLayer(depth=1, height=2, width=2)

        rs.activation.TanhActivationLayer(inputs, outputs)

        assert inputs.values == [
            [[0, 0],
             [0, 0]]
        ]
        assert [[[round(value, 2) for value in row]
                 for row in depth_slice]
                for depth_slice in outputs.values] == [
            [[0.00, 0.00],
             [0.00, 0.00]]
        ]

        inputs.values = [
            [[-1, -2],
             [1, 2]]
        ]
        assert [[[round(value, 2) for value in row]
                 for row in depth_slice]
                for depth_slice in outputs.values] == [
            [[-0.76, -0.96],
             [0.76, 0.96]]
        ]
