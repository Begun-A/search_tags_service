import pytest


@pytest.fixture
def one_word_tag():
    return {'toyota': {False: {}}}


@pytest.fixture
def two_words_tag():
    return {'toyota': {'corolla': {False: {}}}}


@pytest.fixture
def three_words_tag():
    return {'toyota': {'corolla': {'2007': {False: {}}}}}


@pytest.fixture
def four_words_tag():
    return {'camera': {'and': {'navigation': {'system': {False: {}}}}}}


@pytest.fixture
def nested_words_tag():
    return {'toyota': {False: {}, 'corolla': {'2007': {False: {}}}}}
