import string
from itertools import chain


def split_text_by_sentences(text):
    """Split a text by words.

    Another approach:
    `[word.strip(string.punctuation) for word in input_text.split() if word not in string.punctuation]`
    """
    sentences = []
    for sent in text.split('.'):
        new_sent = ''
        for char in sent:
            if char in string.punctuation:
                new_sent += " "
                continue
            new_sent += char.lower()
        new_sent = new_sent.split()
        if new_sent:
            sentences.append(new_sent)
    return sentences


def generate_tags(sent, tags, word, ctag='', added_words=[]):
    new_sent = sent[1:]
    if word in tags:
        new_word = ctag + ' ' + word if ctag else word
        if tags[word] == {False: {}}:
            added_words.append(new_word)
            return added_words
        if False in tags[word]:
            added_words.append(new_word)
        for i, w in enumerate(new_sent[0:3]):
            generate_tags(new_sent[i:], tags[word], w, new_word, added_words)
    return added_words


def get_tags(sent, tags):
    while sent:
        yield generate_tags(sent, tags, sent[0], ctag='', added_words=[])
        sent = sent[1:]


def get_tags_from_text(input_text, tags):
    text = split_text_by_sentences(input_text)
    result_tags = [t for sent in text for t in get_tags(sent, tags)]
    return {'tags': list(set(chain.from_iterable(result_tags)))}
