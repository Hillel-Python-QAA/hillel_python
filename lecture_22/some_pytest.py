import platform
from time import sleep

import pytest


def tc_check_print():
    sleep(4)
    assert True


@pytest.mark.smoke
def tc_verify():
    sleep(4)
    assert True


def tc_verify1():
    sleep(4)
    assert True


def tc_verify2():
    sleep(4)
    assert True


def tc_verify3():
    sleep(4)
    assert True


def tc_verify4():
    sleep(4)
    assert True


def tc_verify5():
    sleep(4)
    assert True


@pytest.mark.skip(reason="Because")
def tc_verify6():
    sleep(4)
    assert True


@pytest.mark.smoke
def tc_verify7():
    sleep(4)
    assert True


@pytest.mark.smoke
@pytest.mark.skipif(platform.system() != "Windows", reason="Not a Windows")
def tc_verify8():
    sleep(4)
    assert True
