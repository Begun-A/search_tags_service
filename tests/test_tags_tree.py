from search_tags_service.services.v1.utils import get_tags_tree


def test_get_tag(one_word_tag_str, two_words_tag_str, three_words_tag_str, four_words_tag_str,
                 one_word_tag, two_words_tag, three_words_tag, four_words_tag, nested_words_tag):
    # one tag in list
    assert get_tags_tree(one_word_tag_str) == one_word_tag
    assert get_tags_tree(two_words_tag_str) == two_words_tag
    assert get_tags_tree(four_words_tag_str) == four_words_tag

    # nested two tag in list
    assert get_tags_tree(one_word_tag_str + three_words_tag_str) == nested_words_tag
