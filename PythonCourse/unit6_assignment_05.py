__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by spaces. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if sentence is None:
        return None
    if sentence.__class__ is not str:
        raise TypeError,"Only string type allowed,"
    end_index = len(sentence)
    sentence_actual = sentence
    sentence = sentence.lower()
    start_pos_either = None
    required_chars = "either"
    processing_index = 0
    hit = False
    while (not hit) and (processing_index < end_index):
        for x in required_chars:
            if x == sentence[processing_index]:
                processing_index += 1
            else:
                break
        else:
            hit = True
            start_pos_either = processing_index - 7
        processing_index += 1

    if start_pos_either is None:
        return sentence_actual
    required_chars = "or"
    start_pos_or = None
    hit = False

    while not hit:
        for x in required_chars:
            if x == sentence[processing_index]:
                processing_index += 1
            else:
                break
        else:
            hit = True
            start_pos_or = processing_index - 3
        processing_index += 1
    if start_pos_or is None:
        return sentence_actual

    result = sentence.replace(sentence_actual[start_pos_either :], sentence_actual[start_pos_either+7 : start_pos_or])
    return result
    pass


def test_prune_either_or_student():
    assert 'we could go to a movie' == prune_either_or("we could either go to a movie or a hotel")
    assert "Whatever happens, happens" == prune_either_or("Whatever happens, happens")
    pass


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit6_server_tests")
    servertests.test_prune_either_or(prune_either_or)
