import pytest

""" Test cases that are in a class inherit this class """
@pytest.mark.usefixtures("driver_for_class")
class BaseTest:
    pass