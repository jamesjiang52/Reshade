import reshade as rs
import pytest


class Test_ConnectionLayer:
    def test_ConnectionLayer(self):
        layer = rs.ConnectionLayer(height=3, width=4, depth=2)
        assert layer.values == [
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],
        ]

        with pytest.raises(TypeError) as e:
            layer = rs.ConnectionLayer()
        assert "The depth, height, and width of the layer must be specified."\
            in str(e)

        connection1 = rs.Connection(0)
        connection2 = rs.Connection(1)
        connection3 = rs.Connection(0)
        connection4 = rs.Connection(1)
        connection5 = rs.Connection(0)
        connection6 = rs.Connection(1)
        layer = rs.ConnectionLayer(
            connections=[
                [[connection1],
                 [connection2],
                 [connection3]],

                [[connection4],
                 [connection5],
                 [connection6]]
            ]
        )
        assert layer.connections == [
            [[connection1],
             [connection2],
             [connection3]],

            [[connection4],
             [connection5],
             [connection6]]
        ]
        assert layer.values == [
            [[0],
             [1],
             [0]],

            [[1],
             [0],
             [1]]
        ]

        layer.values = [
            [[0.5],
             [1],
             [1.5]],

            [[2],
             [2.5],
             [3]]
        ]
        assert layer.values == [
            [[0.5],
             [1],
             [1.5]],

            [[2],
             [2.5],
             [3]]
        ]

        assert layer[0][1][0] == connection2
        assert layer[1:][0][1][0] == connection5
        with pytest.raises(IndexError) as e:
            connection = layer[2][0][0]
        assert "Layer depth exceeded." in str(e)

        test_list = []
        for image in layer:
            for spectrum in image:
                for connection in spectrum:
                    test_list.append(connection)
        assert test_list == [
            connection1,
            connection2,
            connection3,
            connection4,
            connection5,
            connection6
        ]

        assert len(layer) == 2
