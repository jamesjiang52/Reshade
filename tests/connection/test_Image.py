import reshade as rs
import pytest


class TestImage:
    def test_Image(self):
        image = rs.Image(height=3, width=2)
        assert image.values == [
            [0, 0],
            [0, 0],
            [0, 0]
        ]

        with pytest.raises(TypeError) as e:
            image = rs.Image()
        assert "The height and width of the image must be specified." in str(e)

        connection1 = rs.Connection(0)
        connection2 = rs.Connection(1)
        connection3 = rs.Connection(0)
        connection4 = rs.Connection(1)
        
        spectrum1 = rs.Spectrum([connection1, connection2])
        spectrum2 = rs.Spectrum([connection3, connection4])

        image = rs.Image(spectra=[spectrum1, spectrum2])

        assert image.spectra == [spectrum1, spectrum2]
        assert image.values == [
            [0, 1],
            [0, 1]
        ]

        image.values = [
            [0.5, 1],
            [1.5, 2]
        ]
        assert image.values == [
            [0.5, 1],
            [1.5, 2]
        ]

        assert image[0][0] == connection1
        assert image[1:][0][1] == connection4
        with pytest.raises(IndexError) as e:
            connection = image[2][0]
        assert "Image height exceeded." in str(e)

        test_list = []
        for spectrum in image:
            for connection in spectrum:
                test_list.append(connection)
        assert test_list == [
            connection1, connection2, connection3, connection4]

        assert len(image) == 2
