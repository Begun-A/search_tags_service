from search_tags_service.services.v1.tags import get_tags_from_text


def test_same_tags_result(same_tag_words, one_word_tag):
    assert get_tags_from_text(same_tag_words, one_word_tag) == {'tags': ['toyota']}


def test_combinations_indents(tags_combinations_indents, three_words_tag, three_words_tag_str):
    for text in tags_combinations_indents:
        assert get_tags_from_text(text, three_words_tag) == {'tags': three_words_tag_str}


def test_combinations_words(tags_combination_words):
    text, tree_tags, result_tags = tags_combination_words
    generated_tags = get_tags_from_text(text, tree_tags)['tags']
    for tag in result_tags:
        assert tag in generated_tags
