"""Tests for `python_unpaywall` package."""

import pytest
from pkg_resources import parse_version

import python_unpaywall


def test_valid_version():
    """Check that the package defines a valid __version__"""
    assert parse_version(python_unpaywall.__version__) >= parse_version("0.1.0")
