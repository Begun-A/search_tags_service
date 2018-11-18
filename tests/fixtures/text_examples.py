import pytest


@pytest.fixture
def tree_sentences_text_with_difficult_punctuation():
    return """\nNew Toyota Corolla LE 2007, Air Toyota ^Conditioning, *Leather seaters, $.
    \nAlso Available in Different Colours.
    \nBeware Om Fraudsters,, Please See What You Want To.\n"""


@pytest.fixture
def tree_sentences_list_with_difficult_punctuation():
    return [["new", "toyota", "corolla", "le", "2007", "air", "toyota", "conditioning", "leather", "seaters"],
            ["also", "available", "in", "different", "colours"],
            ["beware", "om", "fraudsters", "please", "see", "what", "you", "want", "to"]]


@pytest.fixture
def same_tag_words():
    return "toyota avensys toyota toyota"


@pytest.fixture
def tags_combinations_indents():
    return ["toyota corolla 2007",  # w 0 w 0 w
            "toyota w1 corolla 2007",  # w 1 w 0 w
            "toyota w1 w2 corolla 2007",  # w 2 w 0 w
            "toyota w1 w2 corolla w3 2007",  # w 2 w 1 w
            "toyota w1 w2 corolla w3 w4 2007",  # w 2 w 2 w
            "toyota w1 corolla w2 w3 2007",  # w 1 w 2 w
            "toyota corolla w1 2007",  # w 0 w 1 w
            "toyota corolla w1 w2 2007",  # w 0 w 2 w
            "toyota w1 corolla w2 2007"]  # w 1 w 1 w


@pytest.fixture
def tags_combination_words():
    result_tags = ['toyota corolla 2007',
                   'toyota corolla',
                   'corolla 2007',
                   'toyota 2007',
                   '2007',
                   'corolla',
                   'toyota']
    text = 'toyota corolla 2007'
    tree_tags = {'corolla': {False: {}, '2007': {False: {}}},
                 'toyota': {False: {},
                            'corolla': {False: {},
                                        '2007': {False: {}}},
                            '2007': {False: {}}},
                 '2007': {False: {}}}
    return text, tree_tags, result_tags
