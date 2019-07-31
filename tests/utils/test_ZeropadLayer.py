import reshade as rs


class TestZeropadLayer:
    def test_ZeropadLayer(self):
        inputs = rs.ConnectionLayer(depth=2, height=3, width=3)
        inputs.values = [
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],

            [[10, 11, 12],
             [13, 14, 15],
             [16, 17, 18]]
        ]

        outputs = rs.ConnectionLayer(depth=2, height=8, width=8)
        rs.utils.ZeropadLayer(inputs, outputs, 3, 2, 4, 1)

        assert outputs.values == [
            [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 2, 3, 0, 0],
             [0, 0, 0, 4, 5, 6, 0, 0],
             [0, 0, 0, 7, 8, 9, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 10, 11, 12, 0, 0],
             [0, 0, 0, 13, 14, 15, 0, 0],
             [0, 0, 0, 16, 17, 18, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
        ]

        outputs = rs.ConnectionLayer(depth=2, height=5, width=5)
        rs.utils.ZeropadLayer(inputs, outputs, 1, 1, 1, 1)

        assert outputs.values == [
            [[0, 0, 0, 0, 0],
             [0, 1, 2, 3, 0],
             [0, 4, 5, 6, 0],
             [0, 7, 8, 9, 0],
             [0, 0, 0, 0, 0]],

             [[0, 0, 0, 0, 0],
             [0, 10, 11, 12, 0],
             [0, 13, 14, 15, 0],
             [0, 16, 17, 18, 0],
             [0, 0, 0, 0, 0]],
        ]
