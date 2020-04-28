import os
import pickle
import gensim.downloader as api

"""
api.info()["models"].keys()\
...
dict_keys(['fasttext-wiki-news-subwords-300', 'conceptnet-numberbatch-17-06-300', 'word2vec-ruscorpora-300', 'word2vec-google-news-300', 'glove-wiki-gigaword-50', 'glove-wiki-gigaword-100', 'glove-wiki-gigaword-200', 'glove-wiki-gigaword-300', 'glove-twitter-25', 'glove-twitter-50', 'glove-twitter-100', 'glove-twitter-200', '__testing_word2vec-matrix-synopsis'])
"""

MODELS = [
    #'fasttext-wiki-news-subwords-300',
    'glove-twitter-200',
    'glove-twitter-25',
    #'glove-twitter-50',
]

MODELS_PATH = '/models'


def download():
    print(api.info()['models'])
    os.makedirs(MODELS_PATH)
    for model_name in MODELS:
        if model_name.startswith('_'):
            continue
        print('Downloading `{}` model...'.format(model_name))
        model = api.load(model_name)
        with open(os.path.join(MODELS_PATH, model_name), 'wb') as file:
            pickle.dump(model, file)

if __name__ == "__main__":
    download()
