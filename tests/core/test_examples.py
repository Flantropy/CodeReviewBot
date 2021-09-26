import logging

import pytest


def test_f_one(foo):
    logging.warning('a warning')
    x = foo
    assert x == 1


def test_b_one(bar):
    logging.error('an error')
    assert True


def test_z_one(baz):
    x = baz
    assert x == 3


@pytest.mark.parametrize(
    'text_input, result', [('4+2', 6), ('7+1', 8), ('2*6', 12), ('5-6', -1)]
)
def test_simple_parametrize(text_input, result):
    assert eval(text_input) == result,\
        logging.error(f'text_input={text_input}')
