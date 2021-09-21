import pytest
import logging


@pytest.fixture
def foo():
    logging.warning('a warning')
    return 1


@pytest.fixture(scope='session')
def bar():
    logging.error('an error')
    return 2


