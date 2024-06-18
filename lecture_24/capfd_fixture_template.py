import pytest


def f(name):
    print("hello " + name)


def test_f(capfd):
    f('Tom')

    out, err = capfd.readouterr()
    assert out == "hello Tom\n"




