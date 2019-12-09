"""
Pytest檢查.

"""

# test_show.py
import pytest


def test_sample1():
    """測試1."""
    assert 1 == 1


def test_sample2():
    """測試2."""
    assert [1, 2, 3] != [3, 2, 1]


@pytest.mark.xfail()
def test_sample3():
    """測試3."""
    assert 1 != 1


@pytest.mark.xfail()
def test_sample4():
    """測試4."""
    assert 1 == 1
