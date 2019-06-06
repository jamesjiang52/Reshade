import pytest
import reshade as rs


class TestIdentityActivationLayer:
    def test_IdentityActivationLayer(self):
        inputs = rs.Spectrum(height=4)
        outputs = rs.Spectrum(height=4)

        rs.activation.IdentityActivationLayer(inputs, outputs)

        assert inputs.values == [0, 0, 0, 0]
        assert outputs.values == [0, 0, 0, 0]

        inputs.values = [-1, -2, 1, 2]
        assert outputs.values == [-1, -2, 1, 2]

        inputs = rs.Spectrum(height=8)

        with pytest.raises(TypeError) as e:
            rs.activation.IdentityActivationLayer(inputs, outputs)
        assert "Expected 8 outputs, received 4." in str(e)
