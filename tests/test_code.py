import numpy as np
import pytest

from some_module import integrate_trapz
from some_module import extract_sentence_containing_word

def test_extract_simple():
    para = "This is my paragraph. It is very interesting. Told you so."
    word = "very"
    sent = extract_sentence_containing_word(para, word)
    assert sent == ["It is very interesting"]

# Testing the zero case. Plenty of other tests to write!
def test_integrate_trapz_1():
    xs, ys = np.linspace(0, 10, 10), np.zeros(10)
    assert integrate_trapz(xs, ys) == 0

def test_integrate_trapz_2():
    width = 10
    height = 1
    xs, ys = np.linspace(0, width, 10), np.zeros(10) + height
    assert integrate_trapz(xs, ys) == width * height

def test_integrate_trapz_tri():
    width = 10
    slope = 2
    xs = np.linspace(0, width, 10)
    ys = np.array([slope * x for x in xs])
    assert integrate_trapz(xs, ys) == 0.5 * width * (slope * width)

# Testing too much - ensuring it fails on weird input
# Normally this would be an AssertionException or a specific
# exception, not the general Exception class.
def test_integrate_trapz_failure():
    with pytest.raises(Exception):
        integrate_trapz("Some", "Values")
