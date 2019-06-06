import pytest
import reshade as rs


class TestTanhActivationLayer:
    def test_TanhActivationLayer(self):
        inputs = rs.Spectrum(height=4)
        outputs = rs.Spectrum(height=4)

        rs.activation.TanhActivationLayer(inputs, outputs)

        assert inputs.values == [0, 0, 0, 0]
        assert [round(value, 2) for value in outputs.values] == \
            [0.00, 0.00, 0.00, 0.00]

        inputs.values = [-1, -2, 1, 2]
        assert [round(value, 2) for value in outputs.values] == \
            [-0.76, -0.96, 0.76, 0.96]

        inputs = rs.Spectrum(height=8)

        with pytest.raises(TypeError) as e:
            rs.activation.TanhActivationLayer(inputs, outputs)
        assert "Expected 8 outputs, received 4." in str(e)
