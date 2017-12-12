import numpy as np


def extract_sentence_containing_word(paragraph, word):
    """ Document and test me"""
    sentences = paragraph.split(".")
    selected = [s.strip() for s in sentences if word in s]
    return selected


def integrate_trapz(xs, ys):
    """ Document and test me"""
    widths = np.diff(xs)
    midpoints = 0.5 * (ys[1:] + ys[:-1])
    area = np.sum(widths * midpoints)
    return area
