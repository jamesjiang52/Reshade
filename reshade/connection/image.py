"""
The following classes are defined:
    Image
"""

from ..utils.validate import *
from .connection import Connection
from .spectrum import Spectrum


class Image:
    def __init__(self, spectra=None, *, height=None, width=None):
        if spectra is not None:
            validate_dimensions_image(spectra)
            self._spectra = spectra
        elif height is not None and width is not None:
            self._spectra = [Spectrum(width=width) for i in range(height)]
        else:  # only one of height or width was provided
            raise TypeError(
                "The height and width of the image must be specified."
            )

    @property
    def spectra(self):
        return self._spectra

    @property
    def values(self):
        return [[connection.value for connection in row]
                for row in self._spectra]

    @values.setter
    def values(self, values):
        validate_dimensions_image(values)
        validate_same_dimensions_image(self._spectra, values)

        for i in range(len(self._spectra)):
            for j in range(len(self._spectra[i])):
                self._spectra[i][j].value = values[i][j]

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self._spectra[i]
                    for i in range(*key.indices(len(self._spectra)))]
        if (key >= 0) and (key < len(self._spectra)):
            return self._spectra[key]
        else:
            raise IndexError("Image height exceeded.")

    def __len__(self):
        return len(self._spectra)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == len(self._spectra):
            raise StopIteration

        self._index += 1
        return self._spectra[self._index - 1]
