import os


class Config(object):
    SQLALCHEMY_DATABASE_PATH = os.path.join('/db', 'nn_search.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + SQLALCHEMY_DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ANN_INDEX_LENGTH = int(os.environ.get('ANN_INDEX_LENGTH', 2))
    ANN_INDEX_PATH = os.path.join('/db', 'ann_ix.ann')
