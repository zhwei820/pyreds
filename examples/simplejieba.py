# coding: utf-8
# 19-1-30 下午12:36

import jieba


def simple():
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

    seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("""
Home - BBC News
http://www.bbc.com/news
Visit BBC News for up-to-the-minute news, breaking news, video, audio and feature stories. BBC News provides trusted World and UK news as well as local and regional perspectives.

World
Get the latest BBC World News: …
Latin America · World News TV
UK
Get the latest BBC News: breaking news, …
England · Scotland · Northern Ireland · Wales
Us & Canada
Get the latest American and Canadian news from BBC News in the US and Canada: …

Sport
Breaking news & live sports coverage including results, video, audio and analysis on …

Africa
Get the latest African news from BBC News …
Bobi Wine · War Zone
Europe
Get the latest European news from BBC News in Europe: headlines, features and analysis …

Asia
Get the latest Asian news from BBC News in Asia: breaking news, features, analysis and …

Business
The latest BBC Business News: breaking …
Markets · Economy · Companies
Middle East
Get the latest BBC News from the Middle East: breaking news, features, analysis and …

Technology
Get the latest BBC Technology News: breaking news and analysis on computing, the web, …


Search results from bbc.com
BBC News - Home | Facebook
https://www.facebook.com/bbcnews
BBC News, London. 48,167,492 likes · 1,431,186 talking about this. Welcome to BBC News on Facebook - for the stories that matter to you. Something to...

BBC News - Wikipedia
https://en.wikipedia.org/wiki/BBC_News
BBC News is an operational business division of the British Broadcasting Corporation responsible for the gathering and broadcasting of news and current affairs.The department is the world's largest broadcast news organisation and generates about 120 hours of radio and television output each day, as well as online news coverage.
    """)  # 搜索引擎模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("""
        '刚洗完澡在取暖器边的猫咪',""")  # 搜索引擎模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("""'猫咪',""")  # 搜索引擎模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("""打车回家，跟司机师傅聊天，我说您过年休息吗，师傅说休啊，休个十几天。我说哎呀，您休的比我们多多了。师傅说钱再多也挣不完，别说过年了，平常都过双休日。

这可惊到我了。我喜欢跟人聊天，见谁跟谁聊，以前聊的出租车司机恨不得一个月不休一天，从没见过休双休日的。

我说您这心态太好了，太难得。师傅说，心态必须好，我开出租二十多年，别人挑活儿，我从不挑，多近都走。一天活儿多就多拉一会儿，活儿少就回家歇着。中午吃完饭出来，干到晚上八九点钟，滴滴上抢一个通州的回家了。

我说您双休日都干啥啊，师傅说打打麻将，开车拉着看夫人老妈出去转转。别人一放假，我就放假，到处玩儿。

我说您没压力吗，我看很多师傅都很有压力，也经常会抱怨。师傅说有压力啊，我夫人从生完孩子就没上过班，养家，养两个孩子，孩子上学结婚，都是我一个人在挣钱。

我问现在一个月要给公司交多少啊。师傅说交五千多，政府给发一千多油补，公司给打回来，挺好。

我说，您家在通州哪儿啊，师傅说了个地名，我不知道。师傅说，我通州有三个院子，市里有两套房子，还可以。""")  # 搜索引擎模式
    print(", ".join(seg_list))


if __name__ == '__main__':
    simple()
