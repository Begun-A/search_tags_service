import string

from .data_example import list_of_tags


def split_text_by_words(text):
    """Split a text by words.

    Another approach:
    `[word.strip(string.punctuation) for word in input_text.split() if word not in string.punctuation]`
    This approach faster but not include case, when punctuations in word 'foo,bar'. Need some recursion for split
    by punctuations in word.
    """
    new_text = ""
    for char in text.lower():
        if char in string.punctuation:
            new_text += " "
            continue
        new_text += char
    return new_text.split()


def prepare_tags_list(list_of_tags):
    tags_set, layers = set(), dict()
    for _ in list_of_tags:
        tag = _.lower()
        ttag = tuple(tag.split())
        tags_set.add(tag.lower())
        for i, word in enumerate(ttag):
            if not layers.get(i):
                layers[i] = set((word,))
            layers[i].add(word)
    return tags_set, layers


def get_tags(input_text):
    result_tags = []
    text = split_text_by_words(input_text)
    tags_set, layers = prepare_tags_list(list_of_tags)
    print(tags_set)
    for index, _ in enumerate(text):
        if text[index] not in layers[0]:
            continue
        new_tag = text[index]
        if new_tag in tags_set:
            result_tags.append(text[index])
        d, lindex = 0, 1
        index += 1
        while d <= 2 and index <= len(text):
            if text[index] not in layers[lindex]:
                d += 1
                index += 1
                continue
            new_tag += " " + text[index]
            print(new_tag)
            if new_tag in tags_set:
                result_tags.append(new_tag)
            lindex += 1
            index += 1
            d = 0
    return {
        # 'text': text,
        'tags': result_tags,
        # 'layers': list([(k, list(s)) for k, s in layers.items()])
    }
