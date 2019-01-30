# coding: utf-8
# 19-1-30 下午12:36

import jieba


def simple():
    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(seg_list)

    seg_list = jieba.cut_for_search('''
Home - BBC News
打车回家，
http://www.bbc.com/news
跟司机师傅聊天，
Visit BBC News for up-to-the-minute news, breaking news, video, audio and feature stories. BBC News provides trusted World and UK news as well as local and regional perspectives.
我说您过年休息吗，
World
师傅说休啊，
Get the latest BBC World News: …
休个十几天。
Latin America · World News TV
我说哎呀，
UK
您休的比我们多多了。师傅说钱再多也挣不完，别说过年了，平常都过双休日

    ''')  # 搜索引擎模式
    # print(seg_list)

    seg_list = jieba.cut_for_search('刚洗完澡在取暖器边的猫咪 Mustachio is a cat',)  # 搜索引擎模式
    print(seg_list)

    seg_list = jieba.cut_for_search('''打车回家，跟司机师傅聊天，我说您过年休息吗，师傅说休啊，休个十几天。我说哎呀，您休的比我们多多了。师傅说钱再多也挣不完，别说过年了，平常都过双休日。''')

    # print(seg_list)


if __name__ == '__main__':
    simple()
