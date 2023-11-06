import pytest

from dist import hamming


def test_hamming_distance():
    """Test the Hamming distance function for  strings."""

    P1 = "++0-+"
    P2 = "-+--+"

    hamming_distance = hamming(P1, P2)

    assert hamming_distance == 0.25


def test_hamming_distance_equal_strings():
    """Test the Hamming distance function for equal strings."""

    P1 = "+-++"
    P2 = "+-++"

    hamming_distance = hamming(P1, P2)

    assert hamming_distance == 0.0


def test_hamming_distance_different_strings():
    """Test the Hamming distance function for different strings."""

    P1 = "+-++"
    P2 = "-++-"

    hamming_distance = hamming(P1, P2)

    assert hamming_distance == 0.75


def test_hamming_distance_exclude_0():
    """Test the Hamming distance function for strings with 0."""

    P1 = "+-0-"
    P2 = "+-0+"

    hamming_distance = hamming(P1, P2)

    assert round(hamming_distance, 2) == float(0.33)


def test_hamming_distance_2_items():

    P1 = "-+"
    P2 = "++"

    hamming_distance = hamming(P1, P2)

    assert hamming_distance == 0.5