# coding: utf-8
# 19-1-30 下午4:38

try:
    import pyreds
except Exception:
    import nltk

    nltk.download('stopwords')
    import pyreds

search_cli = pyreds.create_search('pets')
