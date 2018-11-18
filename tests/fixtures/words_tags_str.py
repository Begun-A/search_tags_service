import pytest


@pytest.fixture
def one_word_tag_str():
    return ['toyota']


@pytest.fixture
def two_words_tag_str():
    return ['toyota corolla']


@pytest.fixture
def three_words_tag_str():
    return ['toyota corolla 2007']


@pytest.fixture
def four_words_tag_str():
    return ['camera And navigation system']
