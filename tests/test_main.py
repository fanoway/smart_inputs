import pytest  # noqa
from core import hello_world


def test_hello_world(capfd):
    x = hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello World\n"
    assert x is None
