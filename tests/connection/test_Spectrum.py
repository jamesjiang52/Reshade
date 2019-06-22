import reshade as rs
import pytest


class TestSpectrum:
    def test_Spectrum(self):
        spectrum = rs.Spectrum(width=2)
        assert spectrum.values == [0, 0]

        with pytest.raises(TypeError) as e:
            spectrum = rs.Spectrum()
        assert "The width of the spectrum must be specified." in str(e)

        connection1 = rs.Connection(0)
        connection2 = rs.Connection(1)
        connection3 = rs.Connection(0)
        spectrum = rs.Spectrum(
            connections=[connection1, connection2, connection3]
        )
        assert spectrum.connections == [connection1, connection2, connection3]
        assert spectrum.values == [0, 1, 0]

        spectrum.values = [0.5, 1, 1.5]
        assert spectrum.values == [0.5, 1, 1.5]

        assert spectrum[0] == connection1
        assert spectrum[1:] == [connection2, connection3]
        with pytest.raises(IndexError) as e:
            connection = spectrum[3]
        assert "Spectrum width exceeded." in str(e)

        test_list = []
        for connection in spectrum:
            test_list.append(connection)
        assert test_list == [connection1, connection2, connection3]

        assert len(spectrum) == 3
