import pytest
import reshade as rs


class TestSigmoidActivationLayer:
    def test_SigmoidActivationLayer(self):
        inputs = rs.Spectrum(height=4)
        outputs = rs.Spectrum(height=4)

        rs.activation.SigmoidActivationLayer(inputs, outputs)

        assert inputs.values == [0, 0, 0, 0]
        assert [round(value, 2) for value in outputs.values] == \
            [0.50, 0.50, 0.50, 0.50]

        inputs.values = [-1, -2, 1, 2]
        assert [round(value, 2) for value in outputs.values] == \
            [0.27, 0.12, 0.73, 0.88]

        inputs = rs.Spectrum(height=8)

        with pytest.raises(TypeError) as e:
            rs.activation.SigmoidActivationLayer(inputs, outputs)
        assert "Expected 8 outputs, received 4." in str(e)
