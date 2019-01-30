from pyreds.reds import (
    create_client,
    create_search,
    Search
)

__version__ = '0.1.3'
VERSION = tuple(map(int, __version__.split('.')))

__all__ = [
    'create_client', 'create_search', 'Search'
]
