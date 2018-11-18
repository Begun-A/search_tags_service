def generate_million_tags():
    return ['tag' + str(i) for i in range(10 ** 6)]


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
