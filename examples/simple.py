# coding: utf-8
# 19-1-30 下午12:10

try:
    from pyreds import reds_en as pyreds
except Exception:
    import nltk

    nltk.download('stopwords')

search = pyreds.create_search('pets')


def simple():
    strs = [
        'Tobi wants four dollars',
        'Tobi only wants $4',
        'Loki is really fat',
        'Loki, Jane, and Tobi are ferrets',
        'Manny is a cat',
        'Luna is a cat',
        'Mustachio is a cat',
    ]
    for i, v in enumerate(strs):
        search.index(v, i)
    ids = search.query('Tobi').end()
    print('Search results for "Tobi"')
    for id in ids:
        print('  - {}'.format(strs[int(id)]))


if __name__ == '__main__':
    simple()
