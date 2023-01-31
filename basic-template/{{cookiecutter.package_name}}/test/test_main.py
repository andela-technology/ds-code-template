
"""
Unit tests for main.py file.
"""

from {{ cookiecutter.module_name }}.main import my_function


def test_my_function():
    """
    Test for my_function in main file.
    """
    assert my_function(3.14) == "3.14"