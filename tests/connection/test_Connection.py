import reshade as rs


class TestConnection:
    def test_Connection(self):
        self._test_value = 0

        connection = rs.Connection()
        assert connection.value == 0

        connection = rs.Connection(1)
        assert connection.value == 1

        connection.value = 0
        assert connection.value == 0

        connection.bind_to(self.__tester)
        assert self._test_value == 0

        connection.value = 1
        assert connection.value == 1
        assert self._test_value == 5

    def __tester(self):
        self._test_value = 5
