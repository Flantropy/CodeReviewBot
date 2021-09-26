import logging

import pytest


@pytest.fixture
def foo():
    return 1


@pytest.fixture(scope='session')
def bar():
    return 2


@pytest.fixture
def baz():
    logging.info('baz setup')
    yield 3
    logging.info('baz teardown')
