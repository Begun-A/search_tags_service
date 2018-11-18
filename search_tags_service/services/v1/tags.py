import string


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


def make_references(sentence):
    while sentence:
        yield sentence[1:4]
        sentence = sentence[1:]


def generate_tags(refers, tags, word, ctag='', added_words=[]):
    try:
        next_refers = next(refers)
    except StopIteration:
        return added_words

    if word in tags:
        new_word = ctag + ' ' + word if ctag else word
        if tags[word] == {False: {}}:
            added_words.append(new_word)
            return added_words
        if False in tags[word]:
            added_words.append(new_word)
        for w in next_refers:
            generate_tags(refers, tags[word], w, new_word, added_words)
    return added_words


def get_tags(sent, tags):
    while sent:
        yield generate_tags(make_references(sent), tags, sent[0], ctag='', added_words=[])
        sent = sent[1:]


def get_tags_from_text(input_text, tags):
    text = split_text_by_sentences(input_text)
    result_tags = []
    for sent in text:
        for t in get_tags(sent, tags):
            result_tags.extend(t)
    return {
        'tags': list(set(result_tags))
    }


{'corolla': {False: {}, '2007': {False: {}}},
 'toyota': {False: {},
            'corolla': {False: {},
                        '2007': {False: {}}},
            '2007': {False: {}}},
 '2007': {False: {}}}
