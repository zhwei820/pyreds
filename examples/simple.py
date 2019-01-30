# coding: utf-8
# 19-1-30 下午12:10

try:
    import pyreds
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
        '博比是猫',
        '看到附件',
        '劳动法律的力量知道',
        '刚洗完澡在取暖器边的猫咪 Mustachio is a cat',

        '打车回家，跟司机师傅聊天，我说您过年休息吗，师傅说休啊，休个十几天。我说哎呀，您休的比我们多多了。师傅说钱再多也挣不完，别说过年了，平常都过双休日。',
    ]
    for i, v in enumerate(strs):
        search.index(v, i)

    def search_test(s):
        ids = search.query(s).end()
        print('Search results for ' + s)
        for id in ids:
            print('  - {}'.format(strs[int(id)]))

    search_test('猫')
    search_test('了')
    search_test('猫咪')
    search_test('猫 咪')
    search_test('知道')
    search_test('cat')
    search_test('Loki')


if __name__ == '__main__':
    simple()
