from search_tags_service.services.v1.utils import generate_million_tags

config_tags = [
    'Toyota',
    'Toyota Corolla 2007',
    'Toyota Corolla LE',
    '4 Wheel Drive',
    'Air Conditioner'
]

list_of_tags = config_tags + generate_million_tags()
