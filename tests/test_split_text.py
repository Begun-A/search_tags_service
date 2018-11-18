from search_tags_service.services.v1.tags import split_text_by_sentences


def test_three_sentences(tree_sentences_text_with_difficult_punctuation,
                         tree_sentences_list_with_difficult_punctuation):
    assert (split_text_by_sentences(tree_sentences_text_with_difficult_punctuation)
            == tree_sentences_list_with_difficult_punctuation)
