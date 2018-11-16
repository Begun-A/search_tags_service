import string

from .data_example import list_of_tags

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


def get_tags_tree(list_of_tags):
    tags_tree = dict()

    for tag in list_of_tags:
        level_tree = tags_tree
        for word in tag.lower().split():
            if word not in level_tree:
                level_tree[word] = {}
            level_tree = level_tree[word]
        else:
            level_tree[False] = {}
    return tags_tree


# def move_on_slice(sentece):
#     i, step, t_slice = 0, 1, True
#     while t_slice:
#         t_slice = sentece[i:i + step]
#         yield t_slice
#         i += 1
#         step += 2

def make_references(sentence):
    while sentence:
        yield sentence[1:4]
        sentence = sentence[1:]


def generate_tags(f, tags, word, words=''):
    next_words = next(f)
    print(word)
    if word not in tags:
        return words
    else:
        new_word = words + ' ' + word
        return [generate_tags(f, tags[word], w, new_word) for w in next_words]


def get_tags(text, tags):
    for sent in text[0:1]:
        while sent:
            yield generate_tags(make_references(sent), tags, sent[0])
            sent = sent[1:]


def get_tags_from_text(input_text):
    text = split_text_by_sentences(input_text)
    tags = get_tags_tree(list_of_tags)
    result_tags = []
    for t in get_tags(text, tags):
        result_tags.append(t)
    return {
        'tree': get_tags_tree(list_of_tags),
        'text': text,
        'tags': result_tags
    }
