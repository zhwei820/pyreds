# coding: utf-8
# 19-1-30 下午12:10

from pyreds import reds_ch as pyreds

search = pyreds.create_search('pets')

s = search.client.zrevrange('pets:word:猫', 0, 1)
print(s)

def simple():
    strs = [
        '博比是猫',
        '看到附件',
        '了的看法和东方',
        '劳动法律的力量副',
        '刚洗完澡在取暖器边的猫咪',
        '''
打车回家，跟司机师傅聊天，我说您过年休息吗，师傅说休啊，休个十几天。我说哎呀，您休的比我们多多了。师傅说钱再多也挣不完，别说过年了，平常都过双休日。

这可惊到我了。我喜欢跟人聊天，见谁跟谁聊，以前聊的出租车司机恨不得一个月不休一天，从没见过休双休日的。

我说您这心态太好了，太难得。师傅说，心态必须好，我开出租二十多年，别人挑活儿，我从不挑，多近都走。一天活儿多就多拉一会儿，活儿少就回家歇着。中午吃完饭出来，干到晚上八九点钟，滴滴上抢一个通州的回家了。

我说您双休日都干啥啊，师傅说打打麻将，开车拉着看夫人老妈出去转转。别人一放假，我就放假，到处玩儿。

我说您没压力吗，我看很多师傅都很有压力，也经常会抱怨。师傅说有压力啊，我夫人从生完孩子就没上过班，养家，养两个孩子，孩子上学结婚，都是我一个人在挣钱。

我问现在一个月要给公司交多少啊。师傅说交五千多，政府给发一千多油补，公司给打回来，挺好。

我说，您家在通州哪儿啊，师傅说了个地名，我不知道。师傅说，我通州有三个院子，市里有两套房子，还可以。
        '''
    ]
    for i, v in enumerate(strs):
        search.index(v, i)

    ids = search.query('猫').end()
    print('Search results for "猫"')
    for id in ids:
        print('  - {}'.format(strs[int(id)]))

    ids = search.query('猫咪').end()
    print('Search results for "猫咪"')
    for id in ids:
        print('  - {}'.format(strs[int(id)]))

    ids = search.query('知道').end()
    print('Search results for "知道"')
    for id in ids:
        print('  - {}'.format(strs[int(id)]))


if __name__ == '__main__':
    simple()
