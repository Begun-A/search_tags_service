from search_tags_service.services.v1.tags import get_tags_from_text


def test_same_tags_result(mg_tag_2, same_tag_words, one_word_tag):
    assert get_tags_from_text(same_tag_words, one_word_tag, mg_tag_2) == {'tags': ['toyota']}


def test_combinations_indents(mg_tag_2, tags_combinations_indents, three_words_tag, three_words_tag_str):
    for text in tags_combinations_indents:
        assert get_tags_from_text(text, three_words_tag, mg_tag_2) == {'tags': three_words_tag_str}


def test_combinations_words(mg_tag_2, tags_combination_words):
    text, tree_tags, result_tags = tags_combination_words
    generated_tags = get_tags_from_text(text, tree_tags, mg_tag_2)['tags']
    for tag in result_tags:
        assert tag in generated_tags
