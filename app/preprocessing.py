import pandas as pd

"""This file will take as input a dictionary with the following schema:

source: Source domain (domain.com)
author: The author, if provided
title: The title of the article
text: The text of the article
image_tag_1: The highest rated tag from the Clarifai API
image_tag_2: The 2nd highest rated tag from the Clarifai API
image_tag_3: The 3rd highest rated tag from the Clarifai API
spelling: 1 if 3+ spelling errors are identified from Azure, 0 otherwise
sentiment: 1-5, 1 being very negative, 5 being very positive

Output schema (list):

source - string
author - string
image_tag_1 - string
image_tag_2 - string
image_tag_3 - string
spelling - binary int (0,1)
sentiment_1 - binary int (0,1)
sentiment_2 - binary int (0,1)
sentiment_3 - binary int (0,1)
sentiment_4 - binary int (0,1)
title - text 
text - text
target (optional) - float
"""

def pickle_load():
    """Load bag of words parameters from pickled file.

     :returns: A np array of weights
     """
    pass


from sklearn import preprocessing
import os



def preprocess(t_d):

    tags = []
    with open(os.getcwd() + '/app/data/tags.txt') as f:
        for tag in f.readlines():
            tags.append(tag)

    for c in tags:
        t_d[c] = 0

    for i, r in t_d.iterrows():
        t_d.loc[i, t_d['image_tag_1'][i]] = 1
        t_d.loc[i, t_d['image_tag_2'][i]] = 1
        t_d.loc[i, t_d['image_tag_3'][i]] = 1

    t_d['sentiment_1'] = 0
    t_d['sentiment_2'] = 0
    t_d['sentiment_3'] = 0
    t_d['sentiment_4'] = 0

    sent = t_d['sentiment']

    for i, r in t_d.iterrows():
        if sent[i] != 5:
            t_d.loc[i, 'sentiment_{}'.format(sent[i])] = 1

    t_d = t_d.drop(['source', 'author', 'image_tag_1', 'image_tag_2', 'image_tag_3', 'title', 'sentiment'], axis=1)

    return t_d.as_matrix()