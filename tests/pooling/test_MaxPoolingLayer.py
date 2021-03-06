import reshade as rs


class TestMaxPoolingLayer:
    def test_MaxPoolingLayer(self):
        inputs = rs.ConnectionLayer(depth=1, height=12, width=12)
        inputs.values = [
            [[0.23, -0.41, -0.1, -0.19, -1.26, -0.07, 1.53, -1.11, 0.03, 1.66, 1.88, -0.62],
             [-1.63, 0.26, 0.21, 0.29, -1.56, -1.79, -0.08, -0.74, -1.52, -0.82, -1.5, 1.41],
             [-0.32, -1.99, 0.74, -1.27, -1.59, -1.7, 1.28, -1.51, 0.11, 0.14, 0.03, 1.53],
             [0.18, 0.78, -0.06, -0.46, -0.05, 0.67, -0.12, 0.96, -1.5, -0.16, 1.94, -1.26],
             [1.65, -0.23, 1.86, 1.79, 0.99, -0.09, 0.11, 1.63, -1.37, -0.75, 0.54, -0.25],
             [1.47, -0.08, 0.89, 1.79, -1.55, 0.16, -0.55, -1.12, 0.95, -0.18, -0.05, -1.07],
             [1.59, -1.59, 1.53, 0.43, 0.07, 0.71, 0.75, 1.92, 0.07, 0.13, -1.28, -0.69],
             [-1.24, -1.15, 0.89, 1.9, 0.2, 1.73, -1.64, -1.6, -1.78, -1.1, -0.27, 0.5],
             [1.03, 1.84, 1.3, -1.59, 1.91, -1.31, -0.58, -1.95, 1.26, 1.57, 0.68, -0.99],
             [-1.75, -1.63, 0.36, 1.68, 1.55, 0.67, 0.12, -1.84, -1.55, -1.91, -1.26, -0.56],
             [-1.31, -1.57, -1.74, 0.21, -0.18, 1.22, -0.74, 0.92, 1.27, -0.44, -0.47, -1.04],
             [0.96, -1.0, -0.46, 0.32, -1.59, -1.08, 1.81, 1.27, -0.38, 1.48, -1.51, -1.07]]
        ]

        outputs = rs.ConnectionLayer(depth=1, height=6, width=6)
        rs.pooling.MaxPoolingLayer(inputs, outputs, 2, 2, 2, 2)

        assert [[[round(value, 2) for value in row]
                 for row in depth_slice]
                for depth_slice in outputs.values] == [
            [[0.26, 0.29, -0.07, 1.53, 1.66, 1.88],
             [0.78, 0.74, 0.67, 1.28, 0.14, 1.94],
             [1.65, 1.86, 0.99, 1.63, 0.95, 0.54],
             [1.59, 1.90, 1.73, 1.92, 0.13, 0.50],
             [1.84, 1.68, 1.91, 0.12, 1.57, 0.68],
             [0.96, 0.32, 1.22, 1.81, 1.48, -0.47]]
        ]

        outputs = rs.ConnectionLayer(depth=1, height=10, width=10)
        rs.pooling.MaxPoolingLayer(inputs, outputs, 3, 3, 1, 1)

        assert [[[round(value, 2) for value in row]
                 for row in depth_slice]
                for depth_slice in outputs.values] == [
            [[0.74, 0.74, 0.74, 0.29, 1.53, 1.53, 1.53, 1.66, 1.88, 1.88],
             [0.78, 0.78, 0.74, 0.67, 1.28, 1.28, 1.28, 0.96, 1.94, 1.94],
             [1.86, 1.86, 1.86, 1.79, 1.28, 1.63, 1.63, 1.63, 1.94, 1.94],
             [1.86, 1.86, 1.86, 1.79, 0.99, 1.63, 1.63, 1.63, 1.94, 1.94],
             [1.86, 1.86, 1.86, 1.79, 0.99, 1.92, 1.92, 1.92, 0.95, 0.54],
             [1.59, 1.90, 1.90, 1.90, 1.73, 1.92, 1.92, 1.92, 0.95, 0.50],
             [1.84, 1.90, 1.91, 1.91, 1.91, 1.92, 1.92, 1.92, 1.57, 1.57],
             [1.84, 1.90, 1.91, 1.91, 1.91, 1.73, 1.26, 1.57, 1.57, 1.57],
             [1.84, 1.84, 1.91, 1.91, 1.91, 1.22, 1.27, 1.57, 1.57, 1.57],
             [0.96, 1.68, 1.68, 1.68, 1.81, 1.81, 1.81, 1.48, 1.48, 1.48]]
        ]
